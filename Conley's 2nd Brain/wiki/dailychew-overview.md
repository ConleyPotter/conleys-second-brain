---
type: operations
domain: long-game-studios
tags: [dailychew, product, ai, podcast]
created: 2026-06-05
updated: 2026-06-05
sources: [daily-chew-ai]
---

# DailyChew.AI — Product Overview

DailyChew.AI is a $9.99/month AI-personalized daily news podcast with a post-episode conversation layer. Users set their interests during onboarding; each morning a 6-node pipeline generates a personalized audio episode, then notifies them it is ready. After listening, they can chat with an AI about the episode's content.

**Repo:** `ConleyPotter/daily-chew-ai` (private, TypeScript, Next.js)
**Stage:** Backend feature-complete for v0.1 MVP core loop (generate → listen → chat → notify)

---

## Architecture

### Episode generation pipeline (LangGraph, 6 nodes)

1. **Source Gathering** — GPT-5.4 Nano builds up to 3 personalized Exa search queries from the user's interest profile; fetches and summarizes results.
2. **Script Writer** — Claude Sonnet 4.6 Batch API (50% cost reduction) produces title, summary, show notes, and the episode script.
3. **Quality Gate** — GPT-5.4 Nano scores the script across 5 dimensions; halts pipeline if any score < 5.
4. **Question Generator** — GPT-5.4 Nano (Haiku 4.5 fallback) generates 3 typed reflection questions (comprehension, application, synthesis).
5. **TTS Renderer** — `gpt-4o-mini-tts`; splits scripts > 4096 chars at sentence boundaries; uploads concatenated audio to Cloudflare R2.
6. **Delivery Prep** — Estimates duration from word count, writes episode row with `audioSizeBytes` for COGS tracking, schedules notification.

### Orchestration (Inngest)

- `dailyEpisodeGeneration` — cron `0 6 * * *`, fans out `episode/generate` per premium user.
- `generateEpisode` — retries: 2, concurrency limit 5, durable `step.run` checkpoints, `mark-failed` handling.
- `sendEpisodeNotification` — triggered by `episode/notify` event, retries: 3; fetches user, calls `deliverEpisodeReady`.

### Conversation layer

- `ConversationSession` + `ConversationMessage` tables with cascade-delete foreign keys.
- Streaming API via Vercel AI SDK `streamText` with Claude Sonnet 4.6 primary + automatic fallback.
- System prompt assembled from episode title/summary, user career context, and memories.
- `questions` JSON field on Episode stores reflection questions for conversation prompts.

### Notification delivery

- Resend (ADR-0004): `resend.emails.send()` with HTML + plain-text. Free tier (3k/month) covers early beta at $0.
- React Email templates deferred to beta design phase.

### Audio storage

- Cloudflare R2 via `@aws-sdk/client-s3`. Key pattern: `episodes/{userId}/{timestamp}.mp3`.
- Signed URLs via `@aws-sdk/s3-request-presigner`; GET `/api/episodes/[id]/audio` returns 302 redirect.

---

## Tech stack

| Layer | Technology |
|-------|-----------|
| Framework | Next.js (App Router) |
| Language | TypeScript (strict) |
| Database | Postgres via Drizzle ORM |
| Auth | NextAuth.js |
| Orchestration | Inngest (cron + event-driven) |
| AI models | GPT-5.4 Nano, Claude Sonnet 4.6, Haiku 4.5, gpt-4o-mini-tts |
| AI SDK | Vercel AI SDK (`ai` package) |
| Audio storage | Cloudflare R2 |
| Email | Resend |
| Lint / Format | Biome (ultracite config) |
| Testing | Vitest (198 unit tests) |
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
| GET | `/api/episodes/[id]/audio` | 302 redirect to signed R2 audio URL |
| POST | `/api/conversations` | Create conversation session (Zod-validated) |
| GET | `/api/conversations/[id]` | Session + message history |
| POST | `/api/conversations/[id]/messages` | Stream AI reply |

## Development workflow

Repo uses a strict TDD discipline via two Claude Code skills:
- `/tdd-from-issue` — reads a GitHub issue, writes failing tests first.
- `/implement-from-issue` — reads existing tests and implements code to make them pass.

Biome lint + TypeScript typecheck gate CI. All paid-API dependencies are mocked in tests (no live calls).

---

*Last dev-log: [[lgs-devrecap-2026-06-05]]*
