---
type: project
tags: [automation, ghostwriting, openclaw, commercial, social]
created: 2026-04-14
updated: 2026-04-14
sources: ["Personal Portfolio Website Current State 4.14.26.md", "Thought Leader Engine - Project ACE x OpenClaw.md"]
---

# Thought Leader Engine — The Proactive Ghost

**Related:** [[ace-overview]], [[tech-stack]], [[campaign-plan]], [[brand-voice]], [[phase-3-infrastructure]]

---

## What It Is (Current — May 2026)

The Thought Leader Engine is the content automation layer of the [[personal-brand-engine]] — it processes Conley's raw captures, observations, and build stories into platform-specific content across LinkedIn, X, Substack, and the portfolio blog. It is now focused entirely on Conley's own brand, not external clients.

**The Proactive Ghost commercial product** (the original TLE vision — a ghostwriting-as-a-service product for external clients at $997 setup + $497/month) has been archived. The architecture remains valid and may be revisited in future years when capacity exists, but it is not being pursued now. The archived commercial product documentation is preserved below this section for reference.

**Status:** Active — powering the PBE content pipeline

---

## Personal TLE Architecture

### Input Sources
- **JARVIS captures** from `01-CAPTURES/` — daily observations, reactions, patterns
- **Voice notes or short texts** — real-time takes on AI news, build experiments, BA work stories (sanitized)
- **GitHub activity** — what was shipped; feeds "built this week" content
- **Podcast/audio recordings** (when speaking is the source, transcripts feed written content)

### Processing Layer
n8n + Claude pipeline:
1. Raw input ingested (voice → transcript → clean text, or text directly)
2. SOUL.md injected as system context — ensures voice consistency with [[brand-voice]]
3. Platform-adapted drafts generated per channel (LinkedIn, X, Substack, blog)
4. Drafts routed to Slack/Telegram for async review before publishing

### Memory System
**`SOUL.md` (Conley's voice identity):** The machine-readable version of [[brand-voice]]. Captures tone spectrum, signature language patterns, what to avoid, platform-specific adaptations. Must stay in sync with the brand-voice wiki page.

**`STRATEGY.md` (performance log):** Tracks which posts perform, which get edited heavily, which fall flat. Monthly auto-diff suggestions for SOUL.md refinement.

### Output Channels
See [[content-strategy]] for full channel breakdown and cadence.

---

## Archived: The Proactive Ghost Commercial Product

> The following section documents the original TLE commercial product design. It is preserved as historical record and a potential future concept, not an active plan.

### Original Commercial Concept

---

## The Core Mechanic: Proactive, Not Reactive

Most AI writing tools wait for a prompt. The Proactive Ghost doesn't.

OpenClaw's **Heartbeat** feature proactively reaches out to the client — prodding them for thoughts, opinions, reactions to news — on a schedule. The client responds with a 60-second voice note or quick text. That raw input triggers the content waterfall.

**One voice note → full content ecosystem:**
- 1,200–1,500 word newsletter
- 1× LinkedIn "Authority" post
- 3× X/Threads "Hook" posts
- 1× Instagram caption + Midjourney image prompt
- 1× Lead-gen DM or outreach email

---

## Architecture

### Input Channels

OpenClaw is headless — it routes through any messaging app the client already uses:

| Channel | Best For | Notes |
|---|---|---|
| Telegram | Default / power users | Native OpenClaw support |
| Slack | B2B / corporate clients | Agent lives in a private channel; team (VA/manager) can see drafts |
| iMessage | High-end creators | Requires Mac cloud server (MacStadium) — feels like a real contact |
| SMS/MMS | Non-Telegram clients | Via Twilio, ~$0.01–0.02/msg |
| Email | Passive input | Creator BCCs the agent; agent replies with a draft |
| WhatsApp | International creators | Broad reach |

### Content Waterfall Pipeline

Four-stage sequential multi-agent pipeline:

```
Raw Input (Voice / Text)
    └─> Transcription Agent
            └─> Ghostwriter (Lead Agent)
                    ├─> Social Atomizer
                    │       ├─> LinkedIn Post
                    │       ├─> X Thread (3 tweets)
                    │       └─> IG Caption + Image Prompt
                    ├─> Newsletter Draft
                    └─> Outreach Agent
                            └─> Lead-Gen DM / Email
```

| Agent | Model | Cost Tier | Purpose |
|---|---|---|---|
| Transcription Cleaner | Gemini Flash | 💚 Cheap | Remove filler words, fix grammar |
| Ghostwriter | Claude Opus | 🔴 Premium | Core newsletter draft, voice-aligned to SOUL.md |
| Social Atomizer | GPT-5.3-mini | 🟡 Mid | Break newsletter into social posts (JSON output) |
| Outreach Drafter | GPT-5.0-mini | 💚 Cheap | Generate lead-gen DM/email (150 words max) |

**Estimated cost per run: ~$0.15.** At 5 runs/week per client ≈ $3/month in API costs — well under the $30/month pass-through estimate.

### Memory System

Each client tenant has two persistent Markdown files that improve output quality over time:

**`SOUL.md` — Voice Identity Blueprint**
The client's "digital DNA." Captures:
- Identity: name, role, niche, audience, mission
- Voice profile: tone spectrum (casual ↔ authoritative ↔ vulnerable ↔ contrarian, etc.), signature patterns, formatting preferences
- Worldview: core beliefs, hot takes, topics they love and avoid
- Writing samples with analysis
- Anti-patterns: what NOT to sound like, phrases to avoid, misconceptions to guard against
- Platform adaptations: LinkedIn, X, newsletter, Instagram

**`STRATEGY.md` — Performance Log**
Tracks which outputs the client approves, edits heavily, or rejects. Every 30 days, the system auto-generates a SOUL.md diff suggestion based on observed editing patterns. Client approves or rejects refinements.

### Deployment

Each client gets a **private Dockerized OpenClaw instance** on a managed tenant. Funded by the $997 setup fee. Client connects their own OpenAI/Anthropic API key — API costs are pass-through, not operator overhead.

---

## Economics

| Item | Price | Notes |
|---|---|---|
| Setup fee | $997 (one-time) | OpenClaw tenant build, custom SOUL.md, Heartbeat tuning |
| Monthly subscription | $497/month | Ongoing service |
| Client API costs | ~$30/month | Pass-through — client connects own API keys |
| Operator profit | $497/month per client | Near-zero overhead once built |

Revenue model is monthly recurring. Overhead is front-loaded into the build. This means each additional client adds $497/month at nearly zero marginal cost — unlike ACE Phase I, where each contract requires pipeline execution overhead.

---

## Onboarding Process: Building a Client's SOUL.md

1. **Intake call (30 min)** — Voice Discovery Interview. Sample questions: "How would your best friend describe the way you talk?" / "What 3 creators do you admire — specifically about their style?" / "What's a post you've written that felt most *you*?"
2. **Sample collection** — 5–10 writing samples across platforms. Prioritize high-engagement posts and writing the client is most proud of.
3. **AI analysis pass** — Feed samples to Lead Agent. Extract: dominant tone (with confidence score), sentence length, vocabulary complexity (Flesch-Kincaid), recurring phrases, structural patterns, emotional register. Output: draft SOUL.md.
4. **Calibration loop** — Generate 3 sample posts → client rates 1–10 → iterate until ≥ 8/10 → lock SOUL.md v1.0.
5. **Ongoing refinement** — 30-day auto-diff suggestions from editing patterns. Client approves or rejects changes.

---

## Output Delivery

After the waterfall completes:

1. **Immediate:** Summary message to client's channel — newsletter headline + social post previews
2. **Drafts folder:** All outputs saved to `/tenants/{client_id}/drafts/{date}/`
3. **Approval flow:** Client replies with ✅ (approve), ✏️ (edit), or ❌ (reject) per piece
4. **Auto-publish (optional):** Approved content pushed to scheduling tools (Buffer, Typefully, Beehiiv API)

---

## Relationship to ACE

The Proactive Ghost is built under the ACE umbrella but targets a different buyer and revenue structure than Phase I:

| | ACE Phase I | The Proactive Ghost |
|---|---|---|
| **Buyer** | B2B companies needing lead lists | Executives, creators, professionals |
| **Deliverable** | B2B contact CSV files | Ongoing content + distribution |
| **Revenue model** | Per-contract | Monthly recurring (MRR) |
| **Operator role** | Pipeline oversight | Client management + SOUL.md iteration |
| **Automation depth** | High (near-autonomous) | High, with proactive Heartbeat HITL |

In the ACE phase roadmap, this sits closest to Phase III — it's selling the machine, not the output. But the revenue model (recurring MRR) is more defensible than one-time infrastructure clones. It may represent a fourth commercial track rather than a pure Phase III play.

See [[phase-3-infrastructure]] for the broader Phase III infrastructure thesis.

---

## Implementation Checklist (Outstanding)

**SOUL.md system:**
- [ ] Finalize SOUL.md YAML/Markdown schema
- [ ] Build Voice Discovery Interview script (for sales/onboarding calls)
- [ ] Build AI analysis prompt chain for sample ingestion
- [ ] Build calibration feedback loop (channel-agnostic response handler)
- [ ] Build 30-day auto-refinement cron job
- [ ] Store SOUL.md in `/tenants/{client_id}/SOUL.md` with version history

**Content waterfall:**
- [ ] Scaffold `content-waterfall` skill in OpenClaw
- [ ] Build and test `transcription-cleaner` agent
- [ ] Build and test `ghostwriter` agent with SOUL.md injection
- [ ] Build and test `social-atomizer` agent with JSON output parsing
- [ ] Build and test `outreach-drafter` agent
- [ ] Wire up approval flow (channel-agnostic ✅/✏️/❌ handler)
- [ ] Add cost tracking per run (log to STRATEGY.md)
- [ ] Integration test: voice note → all 5 outputs end-to-end

---

## Open Questions

- Is this a Phase II or Phase III product? It has a Phase III revenue model ($497 MRR) but requires Phase II prerequisites (OpenClaw deployed, multi-tenant infrastructure). May launch in parallel with Phase II.
- The original portfolio framing described the Thought Leader Engine as Conley's *personal* social automation tool. The new framing is commercial. Do both coexist? (Likely: Conley uses it for his own brand; the same infrastructure becomes the product he sells.)
- The iMessage channel requires MacStadium (cloud Mac). What's the ongoing cost, and is it worth the "feels like a real contact" premium for a high-end tier?
- How many clients can be handled simultaneously before per-client SOUL.md oversight becomes a bandwidth constraint?
- Pricing sensitivity: does $497/month hold at the creator/executive tier, or does it need a higher-touch positioning?
