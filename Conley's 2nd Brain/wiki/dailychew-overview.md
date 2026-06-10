---
type: operations
domain: long-game-studios
tags: [dailychew, product, ai, podcast]
created: 2026-06-05
updated: 2026-06-09
sources: [daily-chew-ai]
---

# DailyChew.AI — Product Overview

DailyChew.AI is a $14.99/month AI-personalized daily news podcast with a post-episode conversation layer. Users set their interests during onboarding; each morning a 6-node pipeline generates a personalized audio episode, then notifies them it is ready. After listening, they can chat with an AI about the episode's content.

**Repo:** `ConleyPotter/daily-chew-ai` (private, TypeScript, Next.js)
**Stage:** Backend + eval system feature-complete for v0.1 MVP; reflection UI landed with known bugs; R2→GCS migration complete

---

## Architecture

### Episode generation pipeline (LangGraph, 6 nodes)

1. **Source Gathering** — GPT-5.4 Nano builds up to 3 personalized Exa search queries from the user's interest profile; fetches and summarizes results.
2. **Script Writer** — gpt-4.1 produces title, summary, show notes, and the episode script.
3. **Quality Gate** — GPT-5.4 Nano scores the script across 5 dimensions; halts pipeline if any score < 5.
4. **Question Generator** — GPT-5.4 Nano (Haiku 4.5 fallback) generates 3 typed reflection questions (comprehension, application, synthesis).
5. **TTS Renderer** — `gpt-4o-mini-tts`; splits scripts > 4096 chars at sentence boundaries; uploads concatenated audio to Google Cloud Storage.
6. **Delivery Prep** — Estimates duration from word count, writes episode row with `audioSizeBytes` for COGS tracking, schedules notification.

### Post-delivery evaluation (Gemini judge)

- Default judge: `gemini-3.1-flash-lite` (Batch API, Paid tier). Scores episodes across 5 dimensions on an anchored 1–4 rubric with rationale and evidence per dimension.
- Escalation judge: `gemini-3.5-flash` for any dimension scoring ≤ 2.
- Deterministic pre-checks: duration band, audio rendered, source count, voice embedding cosine similarity, temporal flags.
- Cohen's κ calibration job runs weekly (threshold κ ≥ 0.6 per dimension).
- Golden-label system for building human-labeled eval sets.
- `EpisodeEval` and `GoldenLabel` tables via Drizzle migration `0002_next_sauron.sql`.

### Orchestration (Inngest)

- `dailyEpisodeGeneration` — cron `0 6 * * *`, fans out `episode/generate` per premium user.
- `generateEpisode` — retries: 2, concurrency limit 5, durable `step.run` checkpoints, `mark-failed` handling. Now calls `runPipeline` (LangGraph graph executor) directly.
- `sendEpisodeNotification` — triggered by `episode/notify` event, retries: 3; fetches user, calls `deliverEpisodeReady`.

### Conversation layer

- `ConversationSession` + `ConversationMessage` tables with cascade-delete foreign keys.
- Streaming API via Vercel AI SDK `streamText` with Claude Sonnet 4.6 primary + automatic fallback.
- System prompt assembled from episode title/summary, user career context, and memories.
- `questions` JSON field on Episode stores reflection questions for conversation prompts.
- `ReflectClient.tsx` — two-phase UI: Phase 1 renders reflection question cards; Phase 2 opens streaming chat. Three known `useChat` bugs documented (transport freeze, body format mismatch, no in-flight guard).

### Notification delivery

- Resend (ADR-0004): `resend.emails.send()` with HTML + plain-text. Free tier (3k/month) covers early beta at $0.
- React Email templates deferred to beta design phase.

### Audio storage

- Google Cloud Storage (migrated from Cloudflare R2 on 2026-06-08). Key pattern: `episodes/{userId}/{timestamp}.mp3`.
- Signed URLs; GET `/api/episodes/[id]/audio` returns 302 redirect.
- Egress cost ~$0.12/GB (R2 was $0); adds ~$0.001-0.0012/episode.

---

## Tech stack

| Layer | Technology |
|-------|-----------|
| Framework | Next.js (App Router) |
| Language | TypeScript (strict) |
| Database | Postgres via Drizzle ORM |
| Auth | NextAuth.js |
| Orchestration | Inngest (cron + event-driven) |
| AI models | GPT-5.4 Nano, gpt-4.1, Haiku 4.5, gpt-4o-mini-tts, Claude Sonnet 4.6, gemini-3.1-flash-lite, gemini-3.5-flash |
| AI SDK | Vercel AI SDK (`ai` package, v6) |
| Audio storage | Google Cloud Storage |
| Email | Resend |
| Lint / Format | Biome (ultracite config) |
| Testing | Vitest (~320 unit tests) |
| Deploy | Vercel (auto-deploy on merge to main) |

## ADRs

| # | Decision | Status |
|---|----------|--------|
| 0001 | OpenAI TTS over ElevenLabs | Accepted |
| 0002 | LangGraph pipeline + n8n orchestration (n8n superseded by Inngest) | Accepted (amended) |
| 0003 | Bootstrap to $1M ARR before raising | Accepted |
| 0004 | Resend for transactional email | Accepted |

## API surface (implemented)

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/api/episodes` | List user's episodes (supports `?latest=1`) |
| GET | `/api/episodes/[id]` | Single episode with reflection questions |
| GET | `/api/episodes/[id]/audio` | 302 redirect to signed GCS audio URL |
| POST | `/api/conversations` | Create conversation session (Zod-validated) |
| GET | `/api/conversations/[id]` | Session + message history |
| POST | `/api/conversations/[id]/messages` | Stream AI reply |

## Development workflow

Repo uses a strict TDD discipline via three Claude Code skills:
- `/tdd-from-issue` — reads a GitHub issue, writes failing tests first.
- `/implement-from-issue` — reads existing tests and implements code to make them pass.
- `/resolve-issues` — automates the full TDD-based issue resolution workflow.

Biome lint + TypeScript typecheck gate CI. All paid-API dependencies are mocked in tests (no live calls).

---

*Last dev-log: [[lgs-devrecap-2026-06-09]]*
