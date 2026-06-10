---
type: work-log
domain: long-game-studios
tags: [dailychew, the-grind, dev-log, weekly-recap]
created: 2026-06-05
updated: 2026-06-05
sources: [daily-chew-ai, lgs-the-grind]
---

# Long Game Studios Dev Recap — 2026-06-05

**Period:** First capture — repo creation through June 5, 2026
**Products:** DailyChew.AI (`daily-chew-ai`), The Grind (`lgs-the-grind`)

---

## DailyChew.AI Changelog

### feat (user-facing)

- **Full 6-node episode generation pipeline** (PRs #22, #24) — Source gathering (GPT-5.4 Nano + Exa API) → script writing (Claude Sonnet 4.6 Batch) → quality gate (5-dimension scoring, halt on failure) → question generator (GPT-5.4 Nano with Haiku 4.5 fallback, 3 typed reflection questions) → TTS renderer (`gpt-4o-mini-tts`, chunk splitting at sentence boundaries, R2 upload) → delivery prep (duration estimate, DB write with `audioSizeBytes` COGS tracking, notification scheduling). Sequential graph executor; halts on quality gate failure or node error; never throws. 61 pipeline acceptance-criteria tests.
- **Conversation layer** (PRs #23, #26, #29) — `ConversationSession` and `ConversationMessage` tables with cascade-delete foreign keys, `questions` JSON field on Episode, 6 query helpers with user-ownership enforcement. Streaming API: POST `/api/conversations` (auth-gated, Zod-validated), GET `/api/conversations/[id]` (session + message history), POST `/api/conversations/[id]/messages` (Claude Sonnet 4.6 primary with automatic fallback via Vercel AI SDK `streamText`; system prompt assembled from episode context, user career, and memories). 36 + 23 tests covering DB layer and API routes.
- **Episode retrieval API** (PR #28) — GET `/api/episodes/[id]` with auth, ownership validation (403→404 collapse to avoid UUID leak), reflection question persistence in delivery node (non-fatal on missing questions).
- **Inngest notification pipeline** (PR #32) — `scheduleEpisodeNotification` sends `episode/notify` Inngest event with `ts` for future delivery. `sendEpisodeNotification` handler fetches user, calls `deliverEpisodeReady`. 17 TDD tests, 198/198 suite total.
- **Resend email delivery** (PR #32) — `deliverEpisodeReady` calls `resend.emails.send()` with HTML + plain-text email. Env: `RESEND_API_KEY`, `RESEND_FROM_EMAIL`. React Email templates deferred to beta.
- **Cloudflare R2 audio storage** — `uploadEpisodeAudio` via PutObject, `getSignedAudioUrl` via GetObject presigning. GET `/api/episodes/[id]/audio` returns 302 redirect to signed CDN URL. 18 TDD tests.
- **OpenAI / OpenRouter model integration** — `@ai-sdk/openai` wired for multi-provider completions.
- **RLS + ownership policies** on conversation tables (Supabase-level enforcement).

### test

- Test suite grew from 0 to 198 passing unit tests across pipeline nodes, DB layer, API routes, Inngest functions, and notification scheduling.
- Consistent TDD discipline: red tests committed as separate PRs/commits before implementation.

### chore / infra

- **ADR-0004** — Resend over SendGrid for transactional email. Decisive factors: TypeScript-native SDK, React Email compatibility, 3k/month free tier covers beta at $0, stack coherence. Revisit trigger: deliverability <95% or >10k DAU.
- **ADR-0002 note** — n8n scheduling role superseded by Inngest; recorded in ADR README.
- **CLAUDE.md tech stack** — Replaced n8n with Inngest; added Resend and `lib/inngest/` + `lib/notifications/` to directory map.
- **`/implement-from-issue` Claude Code skill** (PR #27) — Complement to `/tdd-from-issue`; reads existing tests and implements code to make them pass. 6-phase workflow.
- **Vault Keeper dev-log notify** (PR #31) — GitHub Action workflow for push-to-main and release-publish triggers.

### fix

- Biome lint: `noNegationElse` + trailing comma formatting in notification tests.
- 403→404 collapse for wrong-user episode access (consistent with audio endpoint; no UUID info leak).
- Questions write made non-fatal in delivery node (episode already inserted; retry would create duplicate).

### Architecture decisions recorded

| ADR | Decision | Date |
|-----|----------|------|
| 0001 | OpenAI TTS over ElevenLabs | pre-May 29 |
| 0002 | LangGraph pipeline + n8n orchestration (n8n superseded by Inngest) | pre-May 29 |
| 0003 | Bootstrap to $1M ARR before raising | pre-May 29 |
| 0004 | Resend for transactional email | 2026-06-04 |

---

## The Grind Changelog

### feat

- **Repository bootstrapped** (May 30) — Vite + Phaser 3 + TypeScript + Vitest. `package.json` with dev/build/test scripts, `tsconfig.json` with strict mode, `vitest.config.ts` with alias resolution. Unit tests for game config and GameScene. Project structure validation tests.
- **Claude Code skills** — `/implement-from-issue` SKILL.md added for GitHub-issue-driven development.

### docs

- **CLAUDE.md** (PR #23) — AI operating contract. Brand golden rules (Juni spelling, 7-color palette, soft failure language, pixel-art-only-in-game, cats-as-warmth, gold = MRR including $0). Scope contract: vertical-slice-is-the-contract, never steal hours from DailyChew. `/tdd-from-issue` → `/implement-from-issue` workflow. Architecture map, coding conventions, per-slice Definition of Done.
- **README.md** (PR #23) — Human entry point. What it is (content asset, not revenue product), where it lives in the LGS world (Campfire region, $0–$1K MRR), status + P0–P3 roadmap.
- **DEVOPS.md** (PR #23) — Build/deploy/CI runbook. Static build, no-backend/no-PII/localStorage posture, gold = MRR scoreboard honesty rule, CI gate outline (build + unit + Juni-spelling/soft-failure/palette gates).

### chore

- **Vault Keeper dev-log notify** (PR #25) — GitHub Action for dev-log triggers (staged in `automation/` pending manual move to `.github/workflows/`).
- 22-issue backlog seeded (#1–#22) in Now (#1–#7) / Next (#8–#16) / Later (#17–#22) with Priority/Effort/Theme/Horizon fields.

### Architecture decisions recorded

*None yet. `docs/adr/` directory created with `.gitkeep`.*

---

## Build Log

### CI / Deploy

- **DailyChew:** Biome lint + TypeScript typecheck as CI gates. `pnpm check` and `pnpm test:unit` both green at 198/198 tests. Vercel auto-deploy on merge to main (not yet confirmed live). Two CI-red incidents caught and fixed in-PR (Biome formatting in delivery tests and notification tests).
- **The Grind:** No CI pipeline configured yet — `npm test` runs Vitest locally. CI outline documented in DEVOPS.md (build + unit + brand gates) but `.github/workflows/ci.yml` is a planned-not-yet-built item.

### Dependencies added (DailyChew)

| Package | Purpose | Category |
|---------|---------|----------|
| `resend` | Transactional email delivery | Production |
| `@aws-sdk/client-s3` | Cloudflare R2 audio upload | Production |
| `@aws-sdk/s3-request-presigner` | Signed CDN URLs | Production |
| `vitest` | Unit test framework | Dev |

### Migration

- `0001_slow_grim_reaper.sql` — ConversationSession + ConversationMessage tables, `questions` column on Episode, foreign key constraints with cascade delete.

### Cost notes

- Episode generation uses multi-provider LLM calls: GPT-5.4 Nano (source queries, quality gate, questions), Claude Sonnet 4.6 Batch (script writing, 50% cost reduction), `gpt-4o-mini-tts` (TTS). No cost data yet — no live episodes generated.
- R2 audio storage: `audioSizeBytes` tracked per episode for COGS attribution.
- Resend: free tier (3k/month) covers early beta at $0.
- No releases cut. No GitHub Releases on either repo.

---

## Status summary

| Metric | DailyChew | The Grind |
|--------|-----------|-----------|
| Merged PRs | 11 (#21–#32) | 2 (#23, #25) |
| Test count | 198 passing | Basic project structure tests |
| ADRs | 4 (0001–0004) | 0 |
| Releases | None | None |
| Stage | Backend feature-complete for v0.1 MVP core loop (generate → listen → chat → notify) | Bootstrapped; backlog seeded; docs written; no game code yet |
