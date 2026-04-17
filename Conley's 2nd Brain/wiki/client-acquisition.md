---
type: operations
tags: [operations, upwork, proposals]
created: 2026-04-14
updated: 2026-04-16
sources: [ACE Business Plan_ Autonomous Freelance Agent.md, ACE Phase 1 Reference Brief.md]
---

# Client Acquisition Pipeline

**Related:** [[ace-overview]], [[tech-stack]], [[platform-comparison]], [[campaign-plan]]

---

## Overview

ACE's client acquisition must be fully automated because the operator has a maximum of 15 hours per week total — no room for manual job hunting. The pipeline discovers, scores, drafts, and delivers proposals without operator involvement until the final manual submit step.

**Target win rate:** 25–35% response rate (industry average without personalization: ~5%)  
**Target Cost Per Hire:** <$60 (vs. ~$192 at industry-average reply rates)  
**Per-proposal operator time:** ~2 minutes

---

## The Automated Acquisition Pipeline

| Step | Tool | Action |
|---|---|---|
| 1. Discovery | Apify jupri/upwork actor | Polls Upwork for lead enrichment jobs; extracts title, budget, description, URL |
| 2. Dedup | n8n DataTables (table: upwork_jobs) | Checks Job ID — halts if already seen |
| 3. Scoring | Gemini (fast/cheap model) | Scores job 1–10 for fit vs. operator capabilities. Below 8 → discard |
| 4. Proposal Draft | Gemini (quality model) | Writes proposal in Spartan Tone. Appends Google Doc artifact link |
| 5. HITL Alert | Slack #new-upwork-gigs | Posts full draft + budget + job URL. Operator reviews async |
| 6. Manual Submit | Operator | Copies proposal, opens Upwork URL, minor edits if needed, clicks Submit |

**Note on job discovery:** The Business Plan references Vollna RSS feeds for Upwork job polling. The Phase 1 Reference Brief supersedes this with Apify's jupri/upwork actor. Use Apify.

---

## Spartan Tone Protocol

All ACE proposals must comply with this protocol. Violations signal AI generation to experienced clients and destroy the covert positioning.

| Rule | Detail |
|---|---|
| Under 100 words | Every sentence must carry weight. No filler. |
| Zero pleasantries | Never: "thrilled to apply," "hope this finds you well," "excited about this opportunity" |
| Zero robotic transitions | Never: "furthermore," "delve," "leverage" (as a verb), "deliverables" (overused) |
| Address pain directly | Extract the specific problem from the job description. Open with the solution, not credentials. |
| Confident, not boastful | State capability matter-of-factly. No superlatives. |
| Never disclose automation | Do not mention n8n, AI, scrapers, Apify, Apollo, or pipelines to clients. Ever. |

**Message hierarchy for proposals:**
1. Why should I care? (client pain)
2. What is the solution? (the deliverable)
3. Why me? (fixed price, fast turnaround, clean output)
4. What should I do? (accept the proposal; I'll send intake form)

---

## Proposal Artifact

For high-priority jobs, a Mermaid.js flowchart is generated showing exactly how the client's problem will be solved (e.g., a visual diagram of the data extraction pipeline). This is embedded in a Google Doc via the Drive API and the shareable URL is appended to the Upwork cover letter. This creates a disruptive advantage over competing freelancers.

---

## Human-in-the-Loop (HITL) Gate

Upwork's Terms of Service explicitly prohibit fully automated proposal submission via unauthorized APIs or headless browsers. Violations result in permanent account bans.

ACE's HITL architecture:
- The fully drafted proposal, client details, budget, and artifact URL route to Slack
- The operator reviews async during their 15-hour weekly window
- The operator copies the text, opens the Upwork URL, makes microscopic adjustments, and manually clicks Submit
- This hybrid approach yields 30–40% win rate vs. the industry average for blind automation

**The operator never auto-submits.** This is non-negotiable.

---

## Connects Budget Management

Upwork's "Connects" system: 10–20 Connects per proposal, $0.15/Connect → $1.50–$3.00 per submission.

At a 5% reply rate (industry average for non-targeted proposals), Cost Per Hire escalates to ~$192. The Gemini scoring gate (below 8 → discard) filters jobs before any Connect spending occurs, protecting the budget and maintaining a sustainable sub-$60 CPH.

**Target:** Submit only to jobs scoring 8+ on the fit scale. 30% win rate assumed.

---

## Weekly Bandwidth Allocation

| Category | Hours/Week | Tasks |
|---|---|---|
| Acquisition Management (HITL) | 3 hrs | Review AI proposals in Slack, edit tone, manually submit on Upwork |
| Pipeline Maintenance & Triage | 2 hrs | Error logs, refresh OAuth tokens, DB maintenance, VPS storage |
| Client Communication | 4 hrs | Scope clarification, deliver artifacts, collect raw CSVs |
| System Engineering & Expansion | 6 hrs | Build new flows, optimize prompts, test APIs, expand to Phase II |
| **Total** | **15 hrs** | — |
