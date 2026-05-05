---
type: operations
domain: ace
tags: [infrastructure, tools]
created: 2026-04-14
updated: 2026-04-17
sources: [ACE Business Plan_ Autonomous Freelance Agent.md, ACE Phase 1 Reference Brief.md, ACE Pivot Explanation.md]
---

# Tech Stack

**Related:** [[ace-overview]], [[ace-legacy]], [[client-acquisition]], [[phase-1-lead-enrichment]], [[phase-3-infrastructure]]

---

## Overview

ACE runs on a self-hosted VPS with n8n as the central orchestration layer. Phase I uses no agents — just n8n routing API calls. Phase III adds OpenClaw for multi-agent workflows requiring autonomous reasoning and dynamic tool selection.

**Post-pivot additions (as of Feb 2026):** The ACE pivot introduced LangGraph alongside OpenClaw as an orchestration option for more complex agentic workflows. HITL routing now explicitly includes Telegram as an alternative to Slack. See [[ace-overview]] for the pivot context.

---

## Full Stack by Layer

### Orchestration

**n8n** (self-hosted on VPS)
- Primary workflow engine for all ACE pipelines
- Handles API routing, loop control, error handling, HITL alerts
- Preferred over Make/Zapier because the operator already has deep expertise
- Phase I requires no agentic capabilities — n8n linear routing is sufficient
- Phase III complex tasks (autonomous reasoning, local file manipulation) graduate to OpenClaw

**OpenClaw** (on VPS — Phase III, post-pivot HITL workflows, and The Proactive Ghost)
- Code-first agentic framework for tasks requiring dynamic tool selection
- Deployed on Hostinger or Tencent Cloud Lighthouse ($4–$12/month, pre-built images)
- Agent identity defined in `soul.md`; tool access and cron scheduling in `agents.md`
- Memory architecture: Redis for short-term episodic memory + Qdrant or Supabase pgvector for long-term semantic memory
- Security: all external services connected via Model Context Protocol (MCP); `tools.allow` and `tools.deny` lists prevent destructive commands
- **Heartbeat feature:** proactive scheduled outreach to clients/users — pushes prompts on a cron schedule rather than waiting to be invoked. Central to [[thought-leader-engine]] (The Proactive Ghost) product design.
- **Router model strategy:** cheap models (Gemini Flash, GPT-4.5-mini) for lightweight tasks like heartbeat prompts and transcription; premium models (Claude Opus) for core creative output. Balances cost and quality per stage.
- **Multi-tenant deployment:** each client of The Proactive Ghost gets a private Dockerized OpenClaw instance. Per-client memory files (`SOUL.md` for voice identity, `STRATEGY.md` for performance logs) live under `/tenants/{client_id}/`. Clients connect their own API keys; API costs are pass-through.

**LangGraph** (considered post-pivot — not yet in active use)
- Graph-based agent orchestration for complex, stateful workflows; named in the ACE pivot explanation as a tool to adopt
- **Not currently deployed in ACE.** Included in planning because Conley has direct LangChain experience from ACE legacy builds — the conceptual foundation is there; LangGraph hasn't been needed yet at Phase I scale.
- Likely entry point: Phase II or Phase III workflows requiring persistent state across agent steps that n8n linear routing can't handle cleanly

### Job Discovery

**Apify — jupri/upwork actor**
- Scrapes Upwork job listings, replacing the deprecated RSS feed
- Extracts: job title, description, budget, required skills, Upwork job URL
- Replaces Vollna (referenced in Business Plan) as the job polling mechanism per the Phase 1 Reference Brief

### LLM Calls

**Google Gemini** (primary, per Reference Brief)
- Fast/cheap model for job scoring (1–10 fit score)
- Quality model for proposal drafting in Spartan Tone
- Data sanitization (normalizing company names, removing LLC/GmbH suffixes)

**Anthropic Claude Opus** (premium/secondary — router model strategy)
- Premium model for core creative output in OpenClaw workflows (see router model strategy above)
- Current version: Opus 4.7 (April 2026) — more agentic than prior versions; designed for extended, self-directed runs
- Key workflow pattern: give Claude a verification mechanism (bash/server for backend, Chromium extension for frontend, computer use for desktop) to 2–3x output quality on long-running tasks
- Appears in OPEX budget (~$35/month alongside Gemini API costs)
- See [[opus-4-7-workflow]] for workflow patterns specific to 4.7

> Note: The Business Plan references OpenAI GPT-4o-mini and Claude 3.5 Sonnet/Haiku as the LLM layer. The Reference Brief supersedes this with Gemini as primary. Anthropic API tokens remain in the OPEX budget (~$35/month), suggesting Claude may still be used selectively. I'm open to using any LLM API that fits my needs.

### Deduplication / State

**n8n DataTables** (table: `upwork_jobs`)
- Prevents duplicate processing of job IDs
- Cross-references extracted Job IDs before any API calls or scoring

### Data Enrichment

**Apollo.io** ($49/month, Basic tier)
- Primary lead database: 275M+ contacts
- Returns: email, title, LinkedIn, company size, phone
- Rate limits: 50–200 calls/minute depending on tier
- Batch size: 10–20 records; Wait node: 10–15 seconds between batches

**Cleanlist / Prospeo** ($29/month)
- Secondary verification layer: 98% email deliverability accuracy
- Cascades only when Apollo returns low-confidence or blank result
- Together with Apollo, replicates Clay's waterfall at ~$78/month vs. $185–$349/month

### Cache / Database

**Supabase** (PostgreSQL)
- 90-day enrichment cache: before any Apollo API call, check if domain was enriched in last 90 days
- Cache hit = free data pull; cache miss = Apollo call + write back to Supabase
- Builds a proprietary, zero-cost data lake over time
- Also used for long-term agent memory (pgvector) in Phase III

### HITL & Alerts

**Slack** (#new-upwork-gigs channel) **/ Telegram** (post-pivot alternative)
- Receives AI-drafted proposals for operator review before manual Upwork submission
- Receives error alerts from the dedicated n8n Error Trigger workflow
- Error alert format: workflow name + failed node + error message + execution URL
- Post-pivot: Telegram added as an alternative routing destination for asynchronous review and micro-adjustment of agent drafts before final approval

### Artifacts

**Google Docs** (via Drive API)
- Proposal artifacts and Mermaid.js flowcharts embedded in client-facing Google Doc
- Shareable URL appended to Upwork cover letter draft

### Hosting

**VPS** (~$12/month, Hostinger or Tencent Cloud)
- Hosts both n8n and Apify
- 24/7 uptime; predictable restarts

---

## Monthly OPEX Summary

| Item | Cost/Month |
|---|---|
| VPS (n8n + Apify) | ~$12 |
| Apollo.io Basic | $49 |
| Cleanlist / Prospeo | $29 |
| Upwork Connects | ~$50 |
| Gemini / Anthropic API tokens | ~$35 |
| Other (misc tools) | ~$15 |
| **Total** | **~$190** |

---

## Error Handling Architecture

n8n workflows must be hardened for silent failures (rate limits, timeouts, third-party API outages):

1. **Global Error Routing** — every production workflow routes to a dedicated Error Trigger workflow on failure
2. **Context Extraction** — Set node parses workflow name, failed node, error message, execution URL; pushes to Slack
3. **Retry / Exponential Backoff** — Retry on Fail enabled for critical nodes; backoff loop: 1s → 2s → 4s
4. **Graceful Degradation** — "Continue On Fail" enabled on non-critical nodes (e.g., LinkedIn URL lookup); workflow continues with partial data rather than crashing

---

## What ACE Does NOT Use (and Why)

- **Clay** — $185–$349/month; ACE replicates its waterfall in n8n for ~$78/month
- **Lusha** — 70–480 credits/month ceiling; ~$1,230 per 1,000 records; financially unviable for bulk automation
- **Vollna RSS** — mentioned in Business Plan; superseded by Apify actor per Reference Brief
