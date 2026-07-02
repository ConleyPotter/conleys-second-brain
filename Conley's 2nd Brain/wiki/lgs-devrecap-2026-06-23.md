---
type: work-log
domain: long-game-studios
tags: [dailychew, the-grind, dev-log, weekly-recap]
created: 2026-06-23
updated: 2026-06-23
sources: [daily-chew-ai, lgs-the-grind]
---

# Long Game Studios Dev Recap — 2026-06-23

**Period:** June 10–23, 2026 (since last recap 2026-06-09)
**Products:** DailyChew.AI (`daily-chew-ai`), The Grind (`lgs-the-grind`)

---

## DailyChew.AI Changelog

### feat (user-facing)

- **Conversation memory extraction loop** (PR #64, issue #9) — Closes the personalization loop: `extractMemorySignals` runs GPT-5.4 Nano (Batch API) on listen-reflect-converse sessions, Zod-validates structured JSON output, and upserts into a new `UserInterestSignals` table (with embedding, weight, polarity, source episode). Consolidation merges near-identical signals by bumping weight + lastSeen. `getTopInterestSignals` feeds back into the Script Writer prompt so future episodes sharpen. Cold start degrades gracefully to the onboarding profile. Inngest function `extractMemoryOnSessionClose` orchestrates on `session/close`. 30 new tests.
- **Model fallback for inference-crunch resilience** (PR #63, issue #12) — `callWithFallback` in `lib/ai/fallback.ts`: Claude Sonnet 4.6 primary → GPT-5.4 fallback with circuit breaker (trips open after N consecutive failures, auto-recovers after cooldown). Classifies 429/529/5xx/timeout as failover triggers; non-trigger errors (400) rethrow. Script Writer tags each episode with `generatorModel` for downstream quality comparison. `model_fallback` analytics event for fallback-rate signal. All pipeline model IDs extracted to `lib/ai/pipeline-models.ts` (no hardcoded strings). 48 new tests.
- **Retention and trial-funnel instrumentation** (PR #62, issue #10) — Server-side analytics via `@vercel/analytics/server`: `trackAppOpened`, `trackEpisodePlayed` (primary retention signal with `dayIndex`), `trackReflectionSubmitted`, `trackConversationStarted`, trial lifecycle events (`trackTrialStarted/Converted/Lapsed`), push tracking (`trackTrialPushSent`). Cohort readouts via `getRetentionCohorts` (D2/D3/D7 return rates) and `getTrialFunnel` (started/converted/lapsed vs 10% base case). Auth-gated GET `/api/analytics/retention`. 39 new tests.
- **Inject current date + source publish dates into generation prompt** (PR #78, issue #38) — Grounds the Script Writer in real dates: `Today is <ISO date>` header, `Published: <date>` per source, and an explicit instruction forbidding recency language ("recently", "just", "this week") unless the cited source is within 14 days. Includes `failureAnalysis` injection for the judge retry loop. Part of the Doc 4D verification layer.
- **Regex temporal-consistency gate** (PR #79, issue #39) — Zero-cost post-generation check that catches temporal hallucinations without an LLM call. Splits script into sentences, scans against a recency-marker regex, attributes each flagged sentence to its backing source by stopword-filtered token overlap, flags when `daysElapsed > 30`. Returns `{ passed, flags[] }` for the judge gate. 7 new tests.
- **Faithfulness/temporal judge with ship/retry/block routing** (PR #80, issue #40) — The backstop gate between generation and delivery (Doc 4D). Separate Haiku-class judge (`anthropic/claude-haiku-4-5` primary, `gpt-4o-mini` fallback via `callModelWithFallback`) scores faithfulness and temporal accuracy. Aggregates regex gate flags (each deducts 0.15 from score). Routing: >= 0.85 ship, 0.65-0.85 retry (regenerate with feedback via `failureAnalysis`, re-judge once, hold if still failing), < 0.65 block (no TTS, safe fallback served). Never throws. 11 new tests (7 unit + 4 graph wiring).
- **Helicone observability for all LLM and TTS calls** (PR #65, issue #7) — All pipeline nodes, memory extraction, and conversation layer now route through Helicone proxy with `user_id` + `node` tags on every call. Caching enabled for non-personalized nodes (source-gathering, quality-gate, question-generator, eval); explicitly absent for personalized nodes. `callModelWithFallback` makes primary/fallback routing visible in Helicone. Degrades gracefully when `HELICONE_API_KEY` is not set. 57 new tests.
- **Expo app scaffold** (PR #81, issue #50) — First slice of the mobile pivot: `mobile/` module layer with `getApiBaseUrl` (from `EXPO_PUBLIC_API_URL`), `checkBackendHealth` hitting `GET /api/ping`, `fetchWithAuth` (Supabase session bearer token), `createConversationSessionWithGuard` (in-flight dedupe), and Expo Router route constants. Also adds the missing `app/api/ping/route.ts` health endpoint on the backend. 4 new tests. Full Expo project scaffold (create-expo-app, NativeWind) deferred.

### fix (security)

- **Fix XSS vulnerability in DiffView** (PR #69) — Replaced unsafe DOM manipulation with sanitized rendering in the diff viewer component.
- **Fix XSS vulnerability from innerHTML usage** (PR #70) — Removed innerHTML usage in editor functions, replaced with safe DOM APIs.
- **Fix raw SQL interpolation** (PR #72) — Replaced raw SQL string interpolation with Drizzle ORM parameterized update to prevent SQL injection.

### perf

- **Optimize calibration job N+1 query** (PR #67) — Replaced individual episode fetches with batch `getEpisodesByIds` in the calibration job.
- **Optimize nested loops in runCalibrationJob** (PR #68) — Reduced computational complexity of the calibration loop.
- **Optimize chat finish callback** (PR #73) — Eliminated N+1 database operations in the conversation finish handler.

### refactor

- **Simplify array chain in source.ts** (PR #71) — Reduced map/filter chain in source gathering.
- **Replace inline require with module import** (PR #76) — Replaced a CJS `require` with a proper ESM import in the AI module.
- **Extract WORDS_PER_MINUTE to shared constants** (PR #74) — Moved the words-per-minute constant to a shared module for reuse across pipeline nodes.

### test

- **Pipeline error handling test** (PR #66) — Added error handling test coverage for `runPipeline`.

### docs

- **Knowledge & Verification Layer document** (commit e5941f4e) — Added `docs/dc-engineering-4d.md` (Doc 4D), the engineering specification for the claim-based knowledge store and verification pipeline.

### New ADRs

- **ADR-0003: Bootstrap to ~$1M ARR before raising** — Decision to bootstrap through at least $1M ARR before pursuing institutional funding. Solo-founder operating model prioritizes ownership and discipline; revisit at each $250K ARR milestone.
- **ADR-0004: Resend for transactional email** — Selected Resend over SendGrid for episode-ready notifications. TypeScript-native SDK, React Email compatibility, free tier covers beta. `deliverEpisodeReady` calls `resend.emails.send()`. Env vars: `RESEND_API_KEY`, `RESEND_FROM_EMAIL`.

---

## The Grind Changelog

No commits, merged PRs, or releases in this period. The Grind remains at the core-loop-playable stage from the June 6-9 sprint.

---

## Build Log

### CI and code health

- **Google Jules bot** contributed a batch of automated code health PRs on June 19 (PRs #67-74, #76): 3 security fixes (XSS + SQL injection), 3 performance optimizations (N+1 queries + loop optimization), 3 refactors (array simplification, constant extraction, import cleanup). All merged same day.
- **Biome** (`biome.jsonc`) updated: Jules removed the unknown `noUnnecessaryConditions` setting that was causing lint warnings.
- **typecheck script** added to package.json (`tsc --noEmit`) — now part of standard PR verification.

### Test suite

- Test count grew from ~320 (last recap) to ~450+ (estimated from PR verification outputs). PR #65 reports 419 passing, PR #81 reports 396 passing with 53 pre-existing failures in eval tests — the discrepancy reflects different branch states.
- **53 pre-existing test failures** in `tests/eval/{calibration,scorer}.test.ts` persist across all branches. These are not regressions — they were broken before the period started and remain untouched.
- **Playwright e2e suite:** 18-24 tests passing consistently across PRs.

### Dependencies

- No major dependency updates noted in this period.
- Inngest remains at `^3.33.0`.

### Migrations

- `0002_next_sauron.sql` — Adds `EpisodeEval` and `GoldenLabel` tables (eval system, from PR #61 in prior period but migration landed in this window).
- `UserInterestSignals` table added via PR #64 — per-user signal store with weight, polarity, embedding, sourceEpisodeId. Note: may need reconciliation with issue #41's canonical migration.

### Model roster (current as of June 23)

| Node | Model | Provider |
|------|-------|----------|
| Source Gathering | GPT-5.4 Nano | OpenAI |
| Script Writer | gpt-4.1 (primary) | OpenAI |
| Script Writer Fallback | GPT-5.4 | OpenAI |
| Quality Gate | GPT-5.4 Nano | OpenAI |
| Question Generator | GPT-5.4 Nano (Haiku 4.5 fallback) | OpenAI / Anthropic |
| TTS Renderer | gpt-4o-mini-tts | OpenAI |
| Eval Judge (default) | gemini-3.1-flash-lite | Google |
| Eval Judge (escalation) | gemini-3.5-flash | Google |
| Temporal Judge (primary) | claude-haiku-4-5 | Anthropic |
| Temporal Judge (fallback) | gpt-4o-mini | OpenAI |
| Conversation | Claude Sonnet 4.6 (GPT-5.4 fallback) | Anthropic / OpenAI |
| Memory Extraction | GPT-5.4 Nano (Batch API) | OpenAI |
| Embedding | text-embedding model | OpenAI |

DailyChew now uses **6 model providers** across its pipeline: OpenAI (GPT-5.4 Nano, gpt-4.1, gpt-4o-mini, gpt-4o-mini-tts), Anthropic (Claude Sonnet 4.6, claude-haiku-4-5), and Google (gemini-3.1-flash-lite, gemini-3.5-flash). All routed through Helicone for per-node cost observability.

### Cost notes

- Helicone integration (PR #65) is free-tier for now; enables per-user and per-model cost slicing without manual tracking.
- Temporal judge adds ~$0.001/episode (Haiku-class, only fires post-generation). Combined with the ~$0.0006/episode eval judge, total post-delivery verification cost is ~$0.0016/episode — well under the $0.002 target.
- Memory extraction uses GPT-5.4 Nano Batch API — batch pricing applies (~50% cheaper than standard).

### Deployment

- Vercel auto-deploy on merge to main continues.
- No releases cut in either repo.
- Expo/EAS build pipeline not yet configured (scaffold only, PR #81).

---

## Status summary

| Dimension | DailyChew | The Grind |
|-----------|-----------|-----------|
| Stage | Temporal verification pipeline complete; Helicone wired; memory loop closed; mobile scaffold landed | Core loop playable (unchanged) |
| Issues closed this period | #7, #9, #10, #12, #38, #39, #40, #50 | None |
| Test count | ~450+ (up from ~320) | 103 (unchanged) |
| ADR count | 4 (was 2) | 1 (unchanged) |
| Open tech debt | 53 eval test failures, 3 ReflectClient useChat bugs, UserInterestSignals table reconciliation with #41 | None identified |

---

*Previous recap: [[lgs-devrecap-2026-06-09]]*
