---
type: operations
domain: long-game-studios
tags: [dailychew, product, ai, podcast]
created: 2026-06-05
updated: 2026-06-23
sources: [daily-chew-ai]
---

# DailyChew.AI — Product Overview

DailyChew.AI is a $14.99/month AI-personalized daily news podcast with a post-episode conversation layer. Users set their interests during onboarding; each morning a 6-node pipeline generates a personalized audio episode, then notifies them it is ready. After listening, they can chat with an AI about the episode's content.

**Repo:** `ConleyPotter/daily-chew-ai` (private, TypeScript, Next.js + Expo mobile)
**Stage:** Backend pipeline feature-complete for v0.1 MVP; temporal verification pipeline shipped; Helicone observability wired; memory personalization loop closed; mobile scaffold landed (Expo module layer, no full app yet)

---

## Architecture

### Episode generation pipeline (LangGraph, 6 nodes + verification layer)

1. **Source Gathering** — GPT-5.4 Nano builds up to 3 personalized Exa search queries from the user's interest profile + memory signals; fetches and summarizes results with publish dates.
2. **Script Writer** — gpt-4.1 (GPT-5.4 fallback via circuit breaker) produces title, summary, show notes, and the episode script. Prompt includes today's date, per-source publish dates, and a temporal-accuracy instruction forbidding unjustified recency language. Injects top user interest signals as personalization constraints.
3. **Quality Gate** — GPT-5.4 Nano scores the script across 5 dimensions; halts pipeline if any score < 5.
4. **Temporal Verification** (Doc 4D, issues #38/#39/#40) — Two-stage post-generation gate:
   - *Regex gate* (`runRegexTemporalGate`): zero-cost sentence scan against recency markers, attributes flagged sentences to their backing source by token overlap, flags when `daysElapsed > 30`.
   - *Judge gate* (`runJudgeGate`): claude-haiku-4-5 primary (gpt-4o-mini fallback) scores faithfulness and temporal accuracy. Aggregates regex flags (each deducts 0.15). Routes: >= 0.85 ship, 0.65-0.85 retry (regenerate with feedback once), < 0.65 block (no TTS, safe fallback).
5. **Question Generator** — GPT-5.4 Nano (Haiku 4.5 fallback) generates 3 typed reflection questions (comprehension, application, synthesis).
6. **TTS Renderer** — `gpt-4o-mini-tts`; splits scripts > 4096 chars at sentence boundaries; uploads concatenated audio to Google Cloud Storage.
7. **Delivery Prep** — Estimates duration from word count, writes episode row with `audioSizeBytes` for COGS tracking, schedules notification.

### Post-delivery evaluation (Gemini judge)

- Default judge: `gemini-3.1-flash-lite` (Batch API, Paid tier). Scores episodes across 5 dimensions on an anchored 1-4 rubric with rationale and evidence per dimension.
- Escalation judge: `gemini-3.5-flash` for any dimension scoring <= 2.
- Deterministic pre-checks: duration band, audio rendered, source count, voice embedding cosine similarity, temporal flags.
- Cohen's kappa calibration job runs weekly (threshold kappa >= 0.6 per dimension).
- Golden-label system for building human-labeled eval sets.
- `EpisodeEval` and `GoldenLabel` tables via Drizzle migration `0002_next_sauron.sql`.

### Memory and personalization loop (issue #9)

- `extractMemorySignals` runs GPT-5.4 Nano (Batch API) on completed listen-reflect-converse sessions. Zod-validates structured JSON output; rejects invalid output rather than storing it.
- `UserInterestSignals` table: per-user signal store with `weight`, `polarity`, `embedding`, `sourceEpisodeId`, `firstSeen`/`lastSeen`.
- Upsert consolidation: merges near-identical signals (same user/type/subject) by bumping weight + lastSeen.
- `getTopInterestSignals` retrieves top-N by weight + recency, fed back into the Script Writer prompt.
- Cold start degrades gracefully to onboarding profile.
- Orchestrated by `extractMemoryOnSessionClose` Inngest function on `session/close` event.

### Model fallback and resilience (issue #12)

- `callWithFallback` in `lib/ai/fallback.ts`: primary model -> fallback with circuit breaker.
- Trigger classification: 429 (rate limit), 529/5xx (server error), timeouts -> failover. Non-trigger errors (400) rethrow.
- Circuit breaker: trips open after N consecutive failures, skips primary during cooldown, auto-recovers.
- Scripts tagged with `generatorModel` for downstream quality comparison.
- `model_fallback` analytics event for fallback-rate tracking via Helicone/PostHog.
- All pipeline model IDs in `lib/ai/pipeline-models.ts` (no hardcoded strings).

### Observability (Helicone, issue #7)

- All LLM + TTS calls proxy through Helicone with `user_id` + `node` tags.
- Per-user and per-model cost sliceable via Helicone dashboard.
- Caching enabled for non-personalized nodes (source-gathering, quality-gate, question-generator, eval); absent for personalized nodes (script-writer, conversation, memory-extraction, TTS).
- `callModelWithFallback` makes primary/fallback routing visible.
- Degrades gracefully when `HELICONE_API_KEY` is not set.

### Orchestration (Inngest)

- `dailyEpisodeGeneration` — cron `0 6 * * *`, fans out `episode/generate` per premium user.
- `generateEpisode` — retries: 2, concurrency limit 5, durable `step.run` checkpoints, `mark-failed` handling. Calls `runPipeline` (LangGraph graph executor) directly.
- `sendEpisodeNotification` — triggered by `episode/notify` event, retries: 3; fetches user, calls `deliverEpisodeReady`.
- `extractMemoryOnSessionClose` — triggered by `session/close` event; idempotent, embeds each signal before persisting.

### Conversation layer

- `ConversationSession` + `ConversationMessage` tables with cascade-delete foreign keys.
- Streaming API via Vercel AI SDK v6 `streamText` with Claude Sonnet 4.6 primary + GPT-5.4 automatic fallback.
- System prompt assembled from episode title/summary, user career context, and retrieved interest signals.
- `questions` JSON field on Episode stores reflection questions for conversation prompts.
- `ReflectClient.tsx` — two-phase UI: Phase 1 renders reflection question cards; Phase 2 opens streaming chat. Three known `useChat` bugs documented (transport freeze, body format mismatch, no in-flight guard).

### Analytics and instrumentation (issue #10)

- Server-side analytics via `@vercel/analytics/server`: app opens, episode plays (with `dayIndex`), reflections, conversations, trial lifecycle events, push tracking.
- Cohort readouts: `getRetentionCohorts` (D2/D3/D7 return rates), `getTrialFunnel` (started/converted/lapsed vs 10% base case).
- Auth-gated GET `/api/analytics/retention`.

### Notification delivery

- Resend (ADR-0004): `resend.emails.send()` with HTML + plain-text. Free tier (3k/month) covers early beta at $0.
- React Email templates deferred to beta design phase.

### Audio storage

- Google Cloud Storage (migrated from Cloudflare R2 on 2026-06-08). Key pattern: `episodes/{userId}/{timestamp}.mp3`.
- Signed URLs; GET `/api/episodes/[id]/audio` returns 302 redirect.
- Egress cost ~$0.12/GB (R2 was $0); adds ~$0.001-0.0012/episode.

### Mobile scaffold (issue #50)

- `mobile/` module layer: `getApiBaseUrl` (from `EXPO_PUBLIC_API_URL`), `checkBackendHealth`, `fetchWithAuth` (Supabase session bearer token), `createConversationSessionWithGuard` (in-flight dedupe), Expo Router route constants.
- Backend `GET /api/ping` health endpoint added for mobile health checks.
- Full Expo project scaffold (create-expo-app, NativeWind, EAS) deferred to subsequent issues (#51-#53).

---

## Tech stack

| Layer | Technology |
|-------|-----------|
| Framework | Next.js (App Router) + Expo/React Native (mobile, scaffolding) |
| Language | TypeScript (strict) |
| Database | Postgres via Drizzle ORM |
| Auth | NextAuth.js |
| Orchestration | Inngest (cron + event-driven) |
| AI models | GPT-5.4 Nano, gpt-4.1, Haiku 4.5, gpt-4o-mini, gpt-4o-mini-tts, Claude Sonnet 4.6, claude-haiku-4-5, gemini-3.1-flash-lite, gemini-3.5-flash |
| AI SDK | Vercel AI SDK (`ai` package, v6) |
| Audio storage | Google Cloud Storage |
| Email | Resend |
| Observability | Helicone (LLM/TTS proxy) |
| Lint / Format | Biome (ultracite config) |
| Testing | Vitest (~450+ unit tests), Playwright (~24 e2e tests) |
| Deploy | Vercel (auto-deploy on merge to main) |

## ADRs

| # | Decision | Status |
|---|----------|--------|
| 0001 | OpenAI TTS over ElevenLabs | Accepted |
| 0002 | LangGraph pipeline + n8n orchestration (n8n superseded by Inngest) | Accepted (amended) |
| 0003 | Bootstrap to $1M ARR before raising | Accepted |
| 0004 | Resend for transactional email | Accepted |

## Engineering docs

| Doc | Description |
|-----|-------------|
| Doc 4D | Knowledge & Verification Layer (`docs/dc-engineering-4d.md`) — claim-based knowledge store, temporal verification pipeline, post-generation judge routing |

## API surface (implemented)

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/api/episodes` | List user's episodes (supports `?latest=1`) |
| GET | `/api/episodes/[id]` | Single episode with reflection questions |
| GET | `/api/episodes/[id]/audio` | 302 redirect to signed GCS audio URL |
| POST | `/api/conversations` | Create conversation session (idempotent per episode) |
| GET | `/api/analytics/retention` | Retention cohorts + trial funnel (auth-gated) |
| GET | `/api/analytics/activation` | Activation rate metrics (TDD contract, not yet implemented) |
| POST | `/api/analytics/events` | Track analytics events (TDD contract, not yet implemented) |
| GET | `/api/ping` | Health check for mobile client |
| POST | `/api/inngest` | Inngest webhook receiver |

## Known tech debt

- 53 pre-existing test failures in `tests/eval/{calibration,scorer}.test.ts` across all branches
- 3 `useChat` bugs in ReflectClient.tsx (transport freeze, body format mismatch, no in-flight guard) — will be resolved or superseded by RN port (#52)
- `UserInterestSignals` table (PR #64) may need reconciliation with issue #41's canonical migration
- 4 broken tests from R2-to-GCS migration (source.test.ts, audio/upload.test.ts) still pending cleanup

---

*Last dev-log: [[lgs-devrecap-2026-06-23]]*
