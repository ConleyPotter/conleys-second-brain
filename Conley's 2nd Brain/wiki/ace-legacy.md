---
type: project
domain: ace
tags: [history, archived, ace, context]
created: 2026-04-14
updated: 2026-04-16
sources: [ACE What It Is, How It Works, and Why It Exists.md, ACE Business Plan_ Autonomous Freelance Agent.md]
---

# ACE — Legacy System (Pre-Pivot)

**Related:** [[ace-overview]], [[the-sentinel]]

---

## Status: Sunsetted

The system described on this page was built between fall 2025 and February 2026. It has been sunsetted. The current ACE is a different system — see [[ace-overview]] for the post-pivot version.

This page preserves the legacy design for historical context. Many of the ideas here still inform how Conley thinks about agentic systems, even though the specific implementation was abandoned.

---

## What It Was

The original ACE was a **fully autonomous, self-improving content creation engine** — not a freelance tool, not a co-pilot, but a closed-loop system that researched culture, generated media, published it, measured results, and updated its own creative strategy over time.

The description on Conley's portfolio website ("a multi-agent learning engine, not a prompt stack... infrastructure with memory — every output is an experiment, and the system adapts based on evidence over time") accurately describes this version. The portfolio copy was not updated after the pivot.

---

## Architecture: Eight Specialized Agents

The legacy ACE ran on a multi-agent architecture where each agent had exactly one job:

| Agent | Role |
|---|---|
| Research Agent | Watched platforms, ingested real-time trend signals |
| Script Writer Agent | Turned products, trends, and patterns into short-form scripts |
| Editor Agent | Transformed scripts into video assets or asset instructions |
| Publisher Agent | Posted to social platforms, handled retries and failures |
| Analytics Agent | Read performance data, determined what worked and why |
| Optimization Agent | Updated creative strategy based on results and trends |
| Meta Agent | Decided which workflows should run and when |
| Watchdog Agent | Monitored system health, recovered from errors or stalled work |

No agent was allowed to do everything. Explicit job boundaries, explicit contracts between agents.

---

## The Learning Loop

ACE operated in continuous loops, not one-off actions:

1. **Observe** — ingest trends and cultural signals
2. **Create** — generate scripts and assets
3. **Test** — publish as controlled experiments (every post = measurable test)
4. **Measure** — tie performance data back to specific creative choices
5. **Learn** — identify patterns, update strategy
6. **Decide** — choose what to try next

Then repeat.

Every piece of content was linked to: the product → the script → the asset → the platform → the results. The system accumulated evidence rather than guessing.

---

## Tech Stack (Legacy)

- **Supabase** — PostgreSQL storage for content, metadata, and agent state; real-time subscriptions for reactive workflows
- **n8n** — workflow orchestration, scheduling, error recovery
- **Railway Container-Deployed API** — custom API endpoints for various ACE functions

---

## Why It Was Sunsetted

Two reasons, per the pivot explanation:

1. **Constructive feedback** revealed that a human-in-the-loop approach was essential for maintaining quality and strategic intent. Full autonomy in content creation sacrificed something that mattered.

2. **Economic and operational necessity.** Under a strict 15-hour weekly bandwidth constraint, a fully autonomous creative studio was the wrong abstraction. The right abstraction for the constraint was automated output arbitrage — completing structured, objective tasks (not creative work) through agentic pipelines where the operator's time is spent directing the machine, not managing creative quality.

The pivot did not abandon the ideas — it redirected them. The multi-agent architecture, the HITL philosophy, the observability emphasis — all of these carry forward into the current system. What changed was the use case and the commercial model.

---

## What Carried Forward

The current ACE (see [[ace-overview]]) retained:
- Multi-agent orchestration (n8n, OpenClaw, LangGraph)
- HITL review gates (Slack/Telegram webhook routing)
- Observability and logging discipline
- The operator-as-director model (never fulfilling manually)

What was left behind:
- The autonomous content creation loop (research → create → test → measure → learn)
- The closed-loop self-improvement architecture
- The full Supabase + Railway stack
- The 8-agent creative studio model
