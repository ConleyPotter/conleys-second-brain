---
type: strategy
domain: personal
tags: [pbe, personal-brand, career, content, portfolio, ace, tle]
created: 2026-05-06
updated: 2026-05-17
sources:
  - ace-overview.md
  - thought-leader-engine.md
  - content-strategy.md
  - brand-voice.md
  - career-transition-strategy.md
---

# Personal Brand Engine (PBE)

**Related:** [[ace-overview]], [[thought-leader-engine]], [[content-strategy]], [[portfolio-projects]], [[github-strategy]], [[building-out-loud]], [[career-transition-strategy]], [[brand-voice]], [[conley-potter]]

---

## What It Is

The Personal Brand Engine is the unified successor to ACE and the Thought Leader Engine (TLE), merged in May 2026. Rather than generating freelance revenue, the PBE generates career capital — the public proof-of-work, network visibility, and credibility that powers Conley's transition to a $150–200K+ role in AI, MarTech, or RevOps leadership.

**The core bet:** The same AI infrastructure designed to run a freelance business is more valuable pointed at personal brand building. A career comp lift of $30–50K+/year produces better ROI on the same 5–10 hours/week than Upwork contract revenue — and content, portfolio projects, and GitHub activity compound permanently rather than disappearing after each contract closes.

**Why the freelance model didn't work:** Available time for side hustle work was near-zero given BA workload and wedding preparation (June 12, 2026). The elaborate multi-phase commercial plans (ACE Phase I–III, The Proactive Ghost) required sustained execution time that didn't exist. The PBE is designed for the actual constraint: 5–10 hours/week, inconsistent availability, high leverage required on every hour spent.

---

## The Three Pillars

### 1. Content (Write + Speak)
Publishing consistently across LinkedIn, X, Substack, portfolio blog, and an audio/speaking channel (format TBD). The TLE is the processing layer — raw captures become polished, platform-specific content without requiring hours of writing per post. See [[content-strategy]] and [[building-out-loud]].

### 2. Code (Build + Ship)
Real, demonstrable open source projects on GitHub. Not toy projects — tools that solve actual problems in AI, MarTech, and RevOps. Each project is also a piece of content: build it, write about it, post about it. See [[portfolio-projects]] and [[github-strategy]].

### 3. Community (Engage + Connect)
Strategic relationship-building with people at target companies, in the AI/MarTech space, and in the open source community. Content and code create the surface area; showing up in comments, replies, and conversations is how the relationships form.

---

## Architecture

### Input Layer (~2–3 hrs/week of Conley's time)

- **JARVIS captures** from `01-CAPTURES/` — daily observations, reactions, patterns surfaced through the JARVIS workflow
- **Voice notes or short texts** — real-time reactions to AI news, build experiments, BA work stories (sanitized — never identifying client details)
- **GitHub commit activity** — automatic; feeds "what I built this week" content
- **Podcast/audio recordings** — transcripts feed the same processing pipeline as text input

### Processing Layer (automated — the TLE)

See [[thought-leader-engine]] for full architecture. Summary:
1. Raw input → transcription/clean text (if audio)
2. SOUL.md injected as system context (machine-readable [[brand-voice]])
3. Platform-adapted drafts generated per channel
4. Drafts routed to Slack for async review before publishing

### Output Layer

| Channel | Cadence | Purpose |
|---|---|---|
| LinkedIn | 3–4x/week | Career transition credibility; recruiter visibility |
| X (Twitter) | 5–7x/week | Building in public; real-time takes; volume |
| Substack | 2x/month | Deep credibility; shareable proof-of-work |
| Portfolio blog | 1x/month | Polished, evergreen, interview-ready |
| Audio/speaking | TBD | Trust, reach, differentiation |
| GitHub | Continuous | Hard proof-of-work; open source presence |

---

## The Upwork Pipeline: Portfolio Project #1

The one deployed ACE workflow — the Upwork job discovery pipeline — is being repurposed as the first open source portfolio project.

**The pipeline (what it does):**
1. Apify scrapes Upwork for matching job listings
2. Gemini scores each gig on a fit model; filters to top candidates
3. Claude drafts a Upwork proposal in Spartan Tone voice style
4. Claude generates an internal n8n workflow architecture document showing how to fulfill the gig
5. Top gigs delivered to Slack with proposal draft + implementation plan for review

**Why open-sourcing it is better than using it for revenue:** Publishing it as a GitHub repo + Substack article + LinkedIn series creates more career signal than quietly bidding on gigs. It demonstrates n8n automation, AI API orchestration, and practical systems thinking — exactly the skills the target roles value.

See [[portfolio-projects]] for full project list and build order.

---

## How ACE + TLE Merged

**ACE contributed:** The operational mindset (automate everything, HITL only for judgment calls), the n8n infrastructure, and the deployed Upwork pipeline as Portfolio Project #1.

**TLE contributed:** The content waterfall architecture (raw input → multi-channel output), SOUL.md voice alignment system, and STRATEGY.md performance tracking loop.

**What was archived:**
- ACE as a freelance arbitrage business — all commercial phases (I–III) deprioritized
- The Proactive Ghost as a client-facing product — architecturally sound, could be revisited in 2–3 years when there's capacity; archived for now

---

## Success Metrics (12-Month Horizon)

| Metric | Target |
|---|---|
| LinkedIn followers | 2,000+ |
| X followers | 1,000+ |
| Substack subscribers | 500+ |
| GitHub stars (across projects) | 200+ |
| External OSS contributions merged | 5+ |
| Portfolio projects shipped | 3+ |
| Published articles (Substack + blog) | 15+ |
| Inbound recruiter conversations (target companies) | 10+ |
| Job offer in target comp range | 1 |

The ultimate success metric is landing the job. Everything else is upstream signal.

---

## Relationship to Career Transition

The PBE is the primary mechanism for the career transition — not just a parallel project. Recruiters at target companies (Anthropic, Accenture, Palantir commercial, enterprise pharma/fintech) actively check GitHub, LinkedIn content cadence, and Substack for senior AI/MarTech candidates.

A candidate who has been posting consistently about AI implementation for 6 months, has open source projects with GitHub activity, and has published substantive technical articles is fundamentally different from a candidate who just submitted a resume.

See [[career-transition-strategy]] for the full job search strategy and how the PBE feeds it.
