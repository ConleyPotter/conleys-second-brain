---
type: project
domain: personal
tags: [portfolio, github, open-source, career, code, pbe]
created: 2026-05-06
updated: 2026-05-06
sources: []
---

# Portfolio Projects

**Related:** [[personal-brand-engine]], [[github-strategy]], [[content-strategy]], [[career-transition-strategy]], [[tech-stack]]

---

## Purpose

Real, demonstrable, GitHub-published projects that serve as hard proof-of-work for the career transition. Each project must be:

1. **Technically credible** — a hiring manager or technical partner can review the code, README, and architecture
2. **Practically useful** — solves an actual problem, not a demo for its own sake
3. **Content-generative** — each build produces a Substack article, LinkedIn series, and X threads
4. **Honest** — not overclaimed; documented to the level it's actually been built

Build order is priority-ranked. Start with what's already built (packaging work), then move toward the most strategically differentiated builds.

---

## Project 1 — Upwork AI Job Scout

**Status:** Repurposing deployed ACE workflow — packaging and documentation work, not a net-new build  
**Effort:** Low (1–2 weekends)  
**GitHub:** New public repo

### What it does
An n8n workflow that automates the Upwork job search and proposal process:
1. Apify scrapes Upwork for job listings matching defined criteria
2. Gemini scores each gig against a fit model (1–10); filters below threshold
3. Claude drafts a Upwork proposal in a constrained Spartan Tone voice style
4. Claude generates an internal n8n workflow architecture doc showing how to fulfill the gig
5. Top gigs delivered to Slack with proposal draft + implementation plan for async review

### Why it lands
- Already built — packaging work only
- n8n + AI + Apify is a combination people actively search for on GitHub and YouTube
- The "AI designs its own fulfillment plan" mechanic is surprising and demonstrates real systems thinking
- Directly relevant to RevOps and MarTech ops roles ("this person automates complex workflows")

### Content output
- Substack Article #1: "I built an AI system that finds jobs, writes proposals, and designs its own fulfillment plans"
- LinkedIn series: 4 posts covering the problem, the architecture, what broke, and what's next
- X threads on each component (Apify scraping, Gemini scoring, Claude proposal drafting)

---

## Project 2 — n8n × HubSpot Marketing Automation Templates

**Status:** Active build — one workflow in progress at BA (HubSpot call → Claude summary → CRM note)  
**Effort:** Medium (ongoing; add templates incrementally)  
**GitHub:** Public repo of importable n8n workflow JSON files

### What it does
A curated, growing library of production-ready n8n workflow templates for common HubSpot marketing and sales automation tasks. Starting templates:
- HubSpot meeting recording → Claude AI summary → HubSpot note (from BA — real production workflow)
- New deal stage change → Slack notification → automated follow-up task
- Form submission → contact enrichment → CRM field update
- Lead score threshold → sequence enrollment trigger

### Why it lands
- HubSpot has 200K+ customers; n8n has a large and active community — the Venn diagram of people who want this is large
- The BA workflow is real production code, not a demo
- A living template library compounds over time — each new template is a GitHub commit, a post, and a potential star
- Directly demonstrates the exact skills that matter for MarTech Director and RevOps Director roles

### Content output
- Substack: "The HubSpot + AI integration gap nobody documents (here's a working template library)"
- Each new template = one LinkedIn post
- GitHub stars compound as the library grows

---

## Project 3 — AI Campaign Performance Analyzer

**Status:** Planned  
**Effort:** Medium (2–3 weekends)  
**GitHub:** Public repo + Streamlit or lightweight Next.js demo

### What it does
Upload a Google Ads or Meta Ads export CSV → Claude analyzes the performance data → produces plain-language strategy recommendations with specific, prioritized action items. No API keys required from the end user.

Example outputs:
- "Your Search campaigns have 12% CTR but 1.2% CVR — landing pages are the bottleneck, not targeting"
- "Brand keywords consume 40% of budget with 0.3x ROAS vs. non-brand — consider reallocation"
- "These 3 ad groups haven't served in 30 days — likely limited by budget or quality score"

### Why it lands
- Every digital marketer wants this and has the CSV export ready
- Demo-able live in 30 seconds — perfect for LinkedIn video and interview conversations
- Shows ability to build something non-technical users can actually use (full-stack instinct, not just backend)
- Directly relevant to demand gen, RevOps, and MarTech roles

### Content output
- Substack: "I built the AI campaign analyst I always wanted"
- LinkedIn demo video
- X threads on the architecture decisions

---

## Project 4 — MarTech Audit Tool

**Status:** Planned  
**Effort:** High (4–6 weekends; the flagship project)  
**GitHub:** Public repo + live demo

### What it does
Connects to a company's HubSpot or GA4 instance via read-only OAuth, runs an automated audit of marketing data quality and setup, and produces a specific, actionable report via Claude. Demo-able in under 5 minutes.

Example audit outputs:
- "Lead source attribution is missing for 34% of contacts — here's the fix"
- "12 active workflows have never triggered — possible misconfiguration"
- "Contact database has 23% email bounce rate — likely to affect deliverability"
- "Your GA4 conversion events aren't firing on mobile — here's the diagnosis"

### Why it lands
- Every company with HubSpot has these problems and pays consultants to diagnose them manually
- A free tool that does it in 5 minutes is genuinely useful and shareable
- The technical depth (OAuth + API + LLM + report generation) is the most impressive project in the portfolio
- This is the "wow" project for job interviews at MarTech companies, RevOps roles, and Big 4 AI practices

### Build note
Save this one for when there's enough momentum to give it proper polish — a half-finished MarTech audit tool with bad UX hurts more than helps. Build Projects 1–3 first.

### Content output
- Substack: Full technical architecture breakdown
- LinkedIn: Launch post + demo video
- Potential Product Hunt launch for distribution

---

## Project 5 — Open Source Contribution (External Repo)

**Status:** Ongoing / opportunistic  
**Effort:** Variable  
**GitHub:** Contribution to an established project

### What it is
A meaningful contribution to an established open source project in the n8n, LangChain, or MarTech tooling space — a feature, bug fix, well-documented template, or documentation improvement.

### Candidate repos
- n8n community nodes (a HubSpot or Apollo custom node would be directly useful)
- LangChain/LangGraph documentation or example workflows
- Dify, Flowise, or another open-source AI workflow tool
- A HubSpot API utility library on npm/PyPI

### Why it lands
- GitHub username appears in a repo people recognize
- Demonstrates ability to read and work within an existing codebase — different skill from greenfield
- Documentation improvements have high acceptance rates and real value

### Build order note
Don't block other projects waiting for the right opportunity. Contributions arise naturally from using these tools daily. Add to this project when a concrete opportunity appears.

---

## Build Order and Timeline

| Phase | Project | Estimated timeline |
|---|---|---|
| Now | Project 1 — Upwork AI Job Scout (package + publish) | Weeks 1–2 |
| Near-term | Project 2 — HubSpot template library (ongoing) | Weeks 3–ongoing |
| Mid-term | Project 3 — Campaign analyzer | Weeks 6–10 |
| Flagship | Project 4 — MarTech audit tool | Months 2–4 |
| Ongoing | Project 5 — OSS contributions | Continuous |

Build Project 1 first — it's already built and requires only packaging and documentation. It gives the PBE its first content anchor. Project 2 is a natural extension of existing BA work. Project 4 is the flagship — save it for when there's polish to spend on it.
