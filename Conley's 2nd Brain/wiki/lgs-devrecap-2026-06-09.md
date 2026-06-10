---
type: work-log
domain: long-game-studios
tags: [dailychew, the-grind, dev-log, weekly-recap]
created: 2026-06-09
updated: 2026-06-09
sources: [daily-chew-ai, lgs-the-grind]
---

# Long Game Studios Dev Recap — 2026-06-09

**Period:** June 6–9, 2026 (since last recap 2026-06-05)
**Products:** DailyChew.AI (`daily-chew-ai`), The Grind (`lgs-the-grind`)

---

## DailyChew.AI Changelog

### feat (user-facing)

- **Post-delivery episode eval with Gemini judge** (PR #61, issue #8) — Full `lib/eval/` module: anchored 1–4 rubric across 5 dimensions, deterministic pre-checks (duration band, audio rendered, source count, voice embedding cosine similarity, temporal flags), `gemini-3.1-flash-lite` (Batch API) as default judge, `gemini-3.5-flash` escalation on any dimension ≤ 2, Cohen's κ calibration job (weekly κ ≥ 0.6 check per dimension), golden-label system for building human-labeled eval sets. New `EpisodeEval` and `GoldenLabel` tables via Drizzle migration `0002_next_sauron.sql`. `getVoiceEmbedding` in `lib/audio/` for voice-consistency embedding pre-check. 69 new tests.
- **Post-episode reflection and conversation UI** (PR #34, issue #20) — `ReflectClient.tsx` two-phase client component: Phase 1 renders reflection question cards (skeleton/error fallback); Phase 2 opens streaming conversation via `/api/conversations`. Server-rendered page with auth guard, episode ownership check, redirect on 404. 16 new component tests via `@testing-library/react`. Three known `useChat` bugs documented in PR (transport frozen at first render, body format mismatch, no in-flight guard on session creation).
- **Script writer model swap** — `scriptWriter` model changed from `claude-sonnet-4-6` to `gpt-4.1` for episode script generation.
- **Resolve-issues Claude Code skill** — New `/resolve-issues` skill for TDD-based GitHub issue resolution; automates the read-issue → find-tests → implement → verify workflow.

### refactor

- **Cloudflare R2 → Google Cloud Storage migration** — All audio storage migrated from R2 to GCS. Updated tests, mocks, upload/retrieval methods, signed URL generation, and environment variables (`CLOUDFLARE_R2_*` → `GCS_*`). Satisfies the Google Gemini XPRIZE hackathon "use a Google Cloud product" requirement.
- **LangGraph pipeline integration** — `generateEpisode` Inngest function refactored to call `runPipeline` (the LangGraph graph executor) directly, removing deprecated standalone `script-writer` and `source-fetch` modules. Source gathering query logic improved with structured objects and better date handling.
- **AI SDK v6 compatibility** — Conversation messages route updated from `toDataStreamResponse` to `toUIMessageStreamResponse` for Vercel AI SDK v6.

### test

- **Activation instrumentation TDD** (PR #33, issue #6) — 31 failing TDD tests defining the contract for activation metrics: `getActivationRate()`, event tracking via `@vercel/analytics/server`, POST `/api/analytics/events`, GET `/api/analytics/activation`.
- Test suite grew from 198 to ~320 passing unit tests (252 after PR #34 + 69 eval tests from PR #61; 4 pre-existing failures in `source.test.ts` and `audio/upload.test.ts` from the R2→GCS migration).

### fix

- Biome lint auto-fixes across eval tests and migration meta JSON (import ordering, `Array()` → `new Array()`, unused imports).
- `toUIMessageStreamResponse` for AI SDK v6 compatibility (the previous `toDataStreamResponse` did not exist in v6).
- OpenAI client initialization error handling improved for missing API keys.
- JSON response cleaning in quality gate and question generation functions.

### chore

- Stale `feat+issue-18-3b` worktree removed from git index.
- `.gitignore` updated for generated language client JSON.
- Claude Code settings updated with additional Bash permissions for linting and GitHub actions.

### Architecture decisions recorded

| ADR | Decision | Date |
|-----|----------|------|
| 0001 | OpenAI TTS over ElevenLabs | pre-May 29 |
| 0002 | LangGraph pipeline + n8n orchestration (n8n superseded by Inngest) | pre-May 29 |
| 0003 | Bootstrap to $1M ARR before raising | pre-May 29 |
| 0004 | Resend for transactional email | 2026-06-04 |

*No new ADRs this period.*

---

## The Grind Changelog

### feat

- **P0 gray-box core loop** (PR #26, issue #3) — `RunManager` owns the full run lifecycle: `startRun`, `collectGold`, `applyDamage`, `advanceDepth`, `endRun` (banked or lost), `isPlayerDead`. Manages `RunState` (volatile, per-run) and `MetaState` (persistent banked gold). Pure `combat.ts` functions: `attack` (immutable, clamps health to 0), `isDefeated`, `computeGoldReward`. Three new Phaser scenes: `CampfireScene` (hub), `DungeonScene` (run), `GameOverScene` (soft failure: "Back to the grind..."). 69 new tests.
- **Campfire → Dungeon scene transitions** (PR #29, issue #4) — Full scene transition wiring with state handoff: `CampfireScene.init()` accepts returning `MetaState`, SPACE descends via `RunManager.startRun()`. `DungeonScene` binds B (bank) and L (lose). `GameOverScene` captures MetaState and soft-fail message, SPACE restarts at Campfire with preserved banked gold.

### refactor

- GameScene constructor test fix (PR #27) — Replaced broken `vi.spyOn(Phaser, "Scene")` with direct `config` property inspection pattern; eliminates the one pre-existing test failure from bootstrap.

### fix

- `requireRun()` guarded against completed runs to prevent double-banking — checks `isActive` so any call after `endRun()` throws.

### Architecture decisions recorded

| ADR | Decision | Date |
|-----|----------|------|
| 0001 | Phaser 3 over Godot 4 for The Grind | 2026-06-06 |

*First ADR.* Phaser 3 chosen for TypeScript-native web library fit, static-bundle deploy, and Vitest unit-testability. Godot 4 documented as the scaling alternative if a second arcade game enters build.

---

## Build Log

### CI / Deploy

- **DailyChew:** Biome lint + TypeScript typecheck as CI gates. Test suite at ~320 passing (4 known pre-existing failures from R2→GCS migration in `source.test.ts` and `audio/upload.test.ts`). Vercel auto-deploy on merge to main.
- **The Grind:** No CI pipeline yet. 103 tests passing locally via Vitest. Build and typecheck clean.

### Dependencies added (DailyChew)

| Package | Purpose | Category |
|---------|---------|----------|
| `@google-cloud/storage` | GCS audio upload (replacing `@aws-sdk/client-s3`) | Production |
| `@testing-library/react` | Component-level Vitest tests | Dev |
| `@testing-library/user-event` | User event simulation for component tests | Dev |
| `@testing-library/jest-dom` | DOM assertion matchers | Dev |
| `jsdom` | Browser environment for component tests | Dev |

### Migration

- `0002_next_sauron.sql` — `EpisodeEval` and `GoldenLabel` tables for the post-delivery evaluation system.

### Cost notes

- Episode eval judge cost: ~$0.0006/episode via `gemini-3.1-flash-lite` Batch API (under the ~$0.002 target). Escalation to `gemini-3.5-flash` for flagged episodes adds ~$0.005/escalation.
- GCS audio storage replaces R2: egress cost ~$0.12/GB (R2 was $0), adding ~$0.001-0.0012/episode for streaming. Episode infra COGS rises from ~$0.005 to ~$0.006-0.007/ep.
- Script writer model swap: `gpt-4.1` replaces `claude-sonnet-4-6` Batch API. Cost impact TBD — gpt-4.1 is likely comparable but loses the 50% batch discount.
- No releases cut. No GitHub Releases on either repo.

### Model roster (current)

| Role | Model | Notes |
|------|-------|-------|
| Source gathering | GPT-5.4 Nano | Exa query generation + summarization |
| Script writer | gpt-4.1 | Changed from Claude Sonnet 4.6 Batch this period |
| Quality gate | GPT-5.4 Nano | 5-dimension scoring |
| Question generator | GPT-5.4 Nano (Haiku 4.5 fallback) | 3 typed reflection questions |
| TTS renderer | gpt-4o-mini-tts | Chunk splitting at sentence boundaries |
| Conversation | Claude Sonnet 4.6 (automatic fallback) | Streaming via Vercel AI SDK |
| Eval judge (default) | gemini-3.1-flash-lite | Batch API, Paid tier |
| Eval judge (escalation) | gemini-3.5-flash | Flagged/ambiguous episodes |

---

## Status summary

| Metric | DailyChew | The Grind |
|--------|-----------|-----------| 
| Merged PRs (this period) | 3 (#33, #34, #61) | 3 (#26, #27, #29) |
| Test count | ~320 passing (4 known failures) | 103 passing |
| ADRs | 4 (unchanged) | 1 (new: engine choice) |
| Releases | None | None |
| Stage | Backend + eval system feature-complete; reflection UI landed with known bugs; R2→GCS migration complete | Core loop playable (gray-box): RunManager + combat + scene transitions wired; first ADR |
