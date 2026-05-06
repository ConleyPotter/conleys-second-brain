---
type: strategy
tags: [strategy, core-concept]
created: 2026-04-14
updated: 2026-04-16
sources: [ACE Business Plan_ Autonomous Freelance Agent.md, ACE Phase 1 Reference Brief.md, ACE Pivot Explanation.md, Personal Portfolio Website Current State 4.14.26.md]
---

# ACE Overview

**Related:** [[ace-legacy]], [[tech-stack]], [[financial-projections]], [[phase-1-lead-enrichment]], [[phase-2-content-vectors]], [[phase-3-infrastructure]], [[conley-potter]], [[portfolio-website]]

---

## ACE History — Three Pivots

ACE has evolved through three distinct phases. Understanding this is essential to reading any document in the wiki accurately.

**Pivot 1 — Original ACE (Fall 2025–Feb 2026):** An autonomous creative studio — 8 specialized agents in a closed learning loop (research → create → test → measure → learn → decide). Sunsetted because full autonomy sacrificed quality and the bandwidth constraint made it the wrong abstraction. See [[ace-legacy]].

**Pivot 2 — Freelance Arbitrage (Feb–May 2026):** HITL-based Upwork arbitrage business. One workflow was built (the Upwork job discovery pipeline). Never pursued past that first build because available time for side hustle work was near-zero given BA workload and wedding preparation. The commercial plans (Phase I–III, The Proactive Ghost) were designed but never executed.

**Pivot 3 — Personal Brand Engine (May 2026, current):** ACE and the Thought Leader Engine (TLE) have been merged into the **Personal Brand Engine (PBE)** — an AI-powered system for building public presence, shipping open source portfolio projects, and generating the career capital that powers Conley's transition to a $150–200K+ role in AI, MarTech, or RevOps leadership. See [[personal-brand-engine]] for the full architecture.

---

## What ACE Is Now

ACE is the operating name for the Personal Brand Engine — the unified AI infrastructure Conley uses to amplify his public presence and build career credentials.

**The strategic logic of the pivot:** The same AI infrastructure that was designed to run a freelance business is more valuable pointed at personal brand building. A career transition worth $30–50K+/year in comp lift produces a better ROI on the same 5–10 hours/week than Upwork contract revenue — and the content, portfolio projects, and GitHub activity compound permanently rather than disappearing after each contract closes.

See [[personal-brand-engine]] for the full system description, architecture, and success metrics.

---

## What Survived the Pivot

- **The Upwork job discovery pipeline** — the one deployed ACE workflow. Being repurposed as Portfolio Project #1: open-sourced, documented, and used as the first piece of PBE content. See [[portfolio-projects]].
- **The technical foundation** — n8n, Apify, Gemini API, Claude API, Slack webhooks. All of it transfers directly to the PBE.
- **The brand voice work** — [[brand-voice]] and the SOUL.md concept are now applied to Conley's own content production rather than client ghostwriting.

## What Was Archived

The following pages documented plans that were never executed and are no longer the active direction:

| Page | What it was |
|---|---|
| [[phase-1-lead-enrichment]] | B2B lead enrichment pipeline (Apollo + Cleanlist) — designed, never built |
| [[phase-2-content-vectors]] | SEO/YouTube/e-commerce content vectors — planned, never built |
| [[phase-3-infrastructure]] | High-ticket infrastructure cloning and RevOps retainers — never pursued |
| [[financial-projections]] | Upwork-based revenue projections — superseded |
| [[client-acquisition]] | Upwork proposal pipeline and Spartan Tone Protocol — Upwork pipeline repurposed as OSS |
| [[upwork-portfolio]] | Upwork freelance portfolio copy — Upwork pursuit deprioritized |
| [[platform-comparison]] | Upwork vs. Fiverr analysis — no longer relevant |
| [[thought-leader-engine]] | The Proactive Ghost commercial product — archived; TLE now powers Conley's own PBE |

---

## Current Tech Stack

The active stack is a subset of what was planned. See [[tech-stack]] for full details including deployment status.

**Active:** n8n, Apify (jupri/upwork actor), Gemini API, Claude API, Slack webhooks, Google Docs/Drive API  
**Planned (not yet subscribed):** Apollo.io, Cleanlist/Prospeo, Supabase  
**Designed but not deployed:** OpenClaw, LangGraph
