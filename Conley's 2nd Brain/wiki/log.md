# Wiki Log

Append-only chronological record of all wiki operations.  
Format: `## [YYYY-MM-DD] operation | description`  
Parse tip: `grep "^## \[" log.md | tail -10` gives the last 10 entries.

---

## [2026-04-14] init | Wiki created — initial ingest of 5 sources

**Operation:** Full wiki build from raw sources  
**Sources ingested:** 5  
**Pages created:** 12 (index + 11 topic pages)

### Sources processed

1. **ACE Business Plan_ Autonomous Freelance Agent.md** — 78-page strategic business plan covering the full ACE architecture: macroeconomic context, Phase I lead enrichment, Phase II content vectors, Phase III infrastructure deployment, financial projections, and advanced system engineering. Key data points extracted: platform market shares, unit economics, API vendor matrix, bandwidth allocation model, error handling architecture.

2. **ACE Phase 1 Reference Brief.md** — Condensed internal operating brief for Phase I. Supersedes several Business Plan details: Apify jupri/upwork actor replaces Vollna RSS; Google Gemini replaces GPT-4o-mini/Claude 3.5 Haiku as primary LLM; n8n DataTables replaces Airtable/Supabase for deduplication. Contains the definitive tech stack, critical operating rules, and Phase I unit economics.

3. **ACE_Phase1_Campaign_Plan.md** — 90-day marketing campaign brief ("First Contract," April 14 – July 13, 2026). Documents all 6 acquisition channels (Upwork, Portfolio Website, Threads, LinkedIn, Fiverr, Email), audience separation protocol, content calendar, success metrics, risk mitigations, and next steps.

4. **Brand Voice Guide 4.14.md** — Comprehensive personal brand voice documentation for Conley Potter. Defines 5 core voice attributes, language patterns to use and avoid, content type variations (technical, economics, body/capacity, life/relationships), and writing guidelines. Final version as of January 7, 2026.

5. **Upwork_Portfolio_Projects.md** — Ready-to-paste copy for 4 Upwork portfolio projects: spec project (Lancaster County manufacturing list), ABM campaign audience research (pull from work AI), CRM data enrichment (pull from work AI), AutoBoost target account research. Includes AI prompts for retrieving day job data.

### Pages created

| Page | Type |
|---|---|
| index.md | Index |
| ace-overview.md | Core strategy |
| tech-stack.md | Infrastructure |
| phase-1-lead-enrichment.md | Phase 1 operations |
| client-acquisition.md | Operations |
| phase-2-content-vectors.md | Phase 2 strategy |
| phase-3-infrastructure.md | Phase 3 strategy |
| financial-projections.md | Finance |
| platform-comparison.md | Market context |
| data-enrichment-apis.md | Tool analysis |
| campaign-plan.md | Marketing |
| brand-voice.md | Brand |
| upwork-portfolio.md | Credibility assets |

### Cross-references noted

- Reference Brief supersedes Business Plan on: job discovery (Apify > Vollna), LLM layer (Gemini > OpenAI), dedup (DataTables > Airtable)
- Both Anthropic API tokens and Gemini appear in OPEX budget — suggests Claude may be used selectively alongside Gemini
- Campaign plan start date (April 14, 2026) = today's date — wiki was built on campaign launch day

---

## [2026-04-14] query | Wiki built and ready for use

All 5 sources summarized and integrated. Wiki is ready for querying. Recommended next queries:
- "What do I need to do this week?" → see [[campaign-plan]] Week 1 tasks and [[upwork-portfolio]] spec project
- "How does the fulfillment pipeline work?" → see [[phase-1-lead-enrichment]]
- "What's my brand voice for Threads?" → see [[brand-voice]] and [[campaign-plan]] channel strategy

---

## [2026-04-14] ingest | Claude Accounts' Saved Memories.md

**Source type:** Multi-account memory consolidation — two Claude accounts (AutoBoost/work and personal/gmail)  
**Pages created:** 1 (`conley-potter.md`)  
**Pages updated:** 4 (`ace-overview.md`, `brand-voice.md`, `campaign-plan.md`, `index.md`)

### What this source contains

A consolidated dump of saved memories from two separate Claude accounts — AutoBoost (work context) and personal (conley.potter@gmail.com). The memories were recorded over time through active use of Claude in both roles.

**AutoBoost account memories cover:**
- Conley's role at Business Actualization — Project Manager (Digital Marketing), functioning as Director of Client Success & Strategy; 8 years experience; ~15-person agency serving automotive repair shops in Palmyra, PA
- Colleagues: Adam Kushner (founder), Jon Fonner (Google Ads), Courtney Nguyen (content), Ethan Wauls (analytics), Micah Dilts (acting COO), and broader team
- Active workstreams: Cowork skill ecosystem for AutoBoost AMs; DNS/hosting projects (Route 53, CloudFront); n8n automation exploration across BA stack; org structure flatarchy proposal
- Working style preferences: casual professional email tone, Google Sheets > xlsx, PPTX via pptxgenjs, Windows/PowerShell environment
- Compensation context: $85K–$120K estimated range for Director role; PA corridor runs 15–20% below national median

**Personal account memories cover:**
- Location: Marietta, PA; engaged to Sami; wedding planning period
- Education: BA in English Lit + Chinese (UW Madison); CS coursework at DePaul; App Academy CS bootcamp
- Restaurant industry background; hiking (Susquehanna Valley + AT); conservation and climate justice interests
- Long-range vision: The River Room (creative commons + digital workshop concept); River & Root podcast concept
- Pattern: tends toward overdelivering and anxiety-driven difficulty disengaging when rest is warranted

### New connections made

- [[conley-potter]] created as the operator profile page, consolidating both account memories
- [[ace-overview]] updated — the 15-hour constraint is now explicitly grounded in the day job context
- [[brand-voice]] updated — added "Operator Background That Informs the Voice" section linking educational/personal background to why the voice sounds the way it does
- [[campaign-plan]] updated — LinkedIn separation section now explains *why* it's hard (Conley is on AutoBoost video content; public professional identity at BA)
- [[index.md]] updated — source count 5→6, page count 12→13, new page and source row added

### Notable observations

- The two accounts reveal a clean identity split that maps exactly onto the [[campaign-plan]] Audience Separation Protocol: work Claude = AutoBoost; personal Claude = longer-arc personal projects
- The River Room concept (creative commons + digital skills co-op for small-town community) is thematically related to ACE but distinct — it's a long-range aspiration, not a current project
- "Director of Client Success & Strategy" formal title alignment is in progress at BA — context for why the LinkedIn separation matters especially now (a title change would make his BA identity even more visible)

---

## [2026-04-14] ingest | Personal Portfolio Website Current State 4.14.26.md

**Source type:** Full copy dump of Conley's personal portfolio website as of April 14, 2026  
**Pages created:** 4 (`portfolio-website.md`, `the-sentinel.md`, `thought-leader-engine.md`, `career-history.md`)  
**Pages updated:** 4 (`conley-potter.md`, `brand-voice.md`, `ace-overview.md`, `index.md`)

### What this source contains

The current copy from all seven sections of Conley's personal portfolio website: Homepage, About, Work, Projects, Writing, Contact. Written largely by Claude Code. Conley notes it is "not fully representative" and needs refinement.

**New information extracted:**

- **Full career timeline** (first time the complete history was documented): Epic Systems (Jun–Sep 2018) → Freelance Director (Jan 2021–Feb 2024) → Tenfold Manager (Jul 2022–Oct 2023, overlapping) → Stoltzfus/Horizon Director of Marketing Technology (Feb 2024–Mar 2025) → AutoBoost current
- **Two previously undocumented projects:** The Sentinel (physical AI prototype, on-device, Linux/Docker/Tailscale) and Thought Leader Engine (social automation framework, n8n, Active)
- **"Calm ambition"** — new term Conley uses to compress his brand philosophy for public audiences
- **Public vs. internal ACE framing** — the portfolio describes ACE as "a multi-agent learning engine, not a prompt stack" — deliberately abstract; no mention of the arbitrage model
- **Three blog post topics** — The Human-Collaborative Machine (Apr 5), Beyond the Prompt (Apr 1), The New Leverage (Mar 25) — all tightly aligned with documented brand voice
- **Portfolio title discrepancy** — site uses "Lead Initiatives & Systems Architect" vs. the formal "Project Manager (Digital Marketing)" / in-progress "Director of Client Success & Strategy"
- **Contact details confirmed:** conley.potter@gmail.com, linkedin.com/in/conley-potter/, Lancaster PA

### New connections made

- [[portfolio-website]] created — full analysis of what the site says, what's accurate, and what needs updating
- [[the-sentinel]] created — physical AI prototype page with known details and open questions
- [[thought-leader-engine]] created — social automation engine page with relationship to ACE acquisition funnel
- [[career-history]] created — dedicated timeline page with cross-cutting patterns analysis
- [[conley-potter]] updated — added Active Projects section, Public-Facing Identity section, career-history link
- [[brand-voice]] updated — added "Calm Ambition" section and "Portfolio Voice Gap" section
- [[ace-overview]] updated — added "Public vs. Internal Framing" section at top
- [[index.md]] updated — source count 6→7, page count 13→17, new sections for Identity & Public Presence and Projects

### Notable observations

- Tenfold (2022–2023) overlaps with the freelance period — Conley was running both simultaneously. This is consistent with his pattern of building independence alongside employment.
- Stoltzfus Structures is in the same Lancaster County geography as ACE Phase I's target niche (Lancaster County industrial/manufacturing). He likely has deep familiarity with that business ecosystem.
- The Sentinel represents a completely different architectural pole from ACE: offline-first vs. cloud-native. Together they suggest a consistent interest in working at both ends of the infrastructure dependency spectrum.
- The portfolio needs meaningful human revision before it represents Conley accurately. Priority: the About page, which reads as AI-generic rather than voice-authentic.

---

## [2026-04-14] ingest | ACE Pivot + Original ACE + Sentinel Project Brief

**Sources ingested:** 3  
- `ACE Pivot Explanation.md`  
- `ACE What It Is, How It Works, and Why It Exists.md`  
- `Project Brief for The Sentinel.md`

**Pages created:** 1 (`ace-legacy.md`)  
**Pages rewritten:** 2 (`ace-overview.md`, `the-sentinel.md`)  
**Pages updated:** 2 (`portfolio-website.md`, `index.md`)

### What these sources contain

**ACE Pivot Explanation** — a concise explanation of what changed and why. The original ACE (autonomous creative studio) was sunsetted. The current ACE operates in two modes: (1) HITL co-pilot where the human is creative lead and agents handle research/drafting, routed through Slack/Telegram; and (2) automated output arbitrage for structured, objective tasks. New orchestration tools: OpenClaw and LangGraph added alongside n8n.

**ACE What It Is, How It Works, and Why It Exists** — the canonical document for the *original* ACE. Eight specialized agents (Research, Script Writer, Editor, Publisher, Analytics, Optimization, Meta, Watchdog) running a closed learning loop: observe → create → test → measure → learn → decide. Built on Supabase + n8n + Cloudflare Workers. Sunsetted Feb 2026.

**Project Brief for The Sentinel** — a fully developed project brief including executive summary, core philosophy, detailed hardware BOM (~$280 total), software architecture, and a 4-phase execution plan (four weekends). Key details: Pepper's Ghost optical illusion using beamsplitter glass + HyperPixel display; Raspberry Pi 5 brain; Live2D Cubism for facial animation; walnut + brass chassis. Status is aspirational — not yet built. ACE revenue is intended as seed capital for the build.

### What changed

- **[[ace-legacy]]** created — preserves the original ACE architecture in full; clarifies why the portfolio copy ("multi-agent learning engine") is historically accurate but outdated
- **[[ace-overview]]** rewritten — now opens with the pivot story; distinguishes current ACE's two operating modes (HITL co-pilot + arbitrage); adds "ACE as Seed Capital for The Sentinel" section; updates tech stack with OpenClaw + LangGraph
- **[[the-sentinel]]** rewritten — full project brief integrated; hardware table with all components; Pepper's Ghost optics explained; 4-phase build plan; corrected status to "aspirational / not yet built" (portfolio said "In Development" which was aspirational, not accurate)
- **[[portfolio-website]]** updated — added "The ACE Description Problem" section at top; corrected the "What Needs Updating" section to name the ACE copy as the highest-priority fix
- **[[index.md]]** updated — source count 7→9, page count 17→18, ace-legacy added to Projects table, three new source rows added

### Notable observations

- The portfolio's ACE description is now a known problem, not a mystery. It describes the sunsetted version. The current ACE needs a new public-facing description built from scratch.
- The Sentinel has a fully formed build plan and a ~$280 BOM. The only thing between the plan and the prototype is time + the seed capital ACE is generating. It is closer to real than the "dreaming about" framing might suggest.
- The ACE pivot introduced OpenClaw and LangGraph — neither of which appears in [[tech-stack]] yet. That page needs to be updated.
- The output intent for The Sentinel Alpha is a visual essay / building-in-public content piece — this connects directly to the Thought Leader Engine and Threads channel strategy.

---

## [2026-04-14] query | Portfolio website update plan for Phase 1 ACE launch

**What was asked:** Create a detailed plan to update the personal portfolio website for ACE Phase 1, structured as discrete queries for a coding agent.

**Pages read:** [[portfolio-website]], [[ace-overview]], [[brand-voice]], [[phase-1-lead-enrichment]], [[campaign-plan]], [[upwork-portfolio]]

**Pages created:** 1 (`portfolio-update-plan.md`)

**How it was answered:** Synthesized the known gaps in the portfolio (stale ACE description, generic About page voice, Phase 3-positioned Consulting section, minor title/meta discrepancies) against Phase 1's requirements (credibility anchor for B2B buyers, live by Week 2). Produced four discrete coding-agent queries covering: (1) ACE and Projects section rewrite, (2) Phase 1 service block added to Consulting section, (3) About page brand voice injection, (4) minor housekeeping fixes.

**Filed as:** [[portfolio-update-plan]] — type `asset`, saved to wiki/portfolio-update-plan.md

### Notable decisions in the plan

- The Consulting section is preserved, not replaced — the Phase 3 advisory framing is accurate to the long-range identity. A "Current Work: B2B Lead Enrichment" block is inserted above it.
- The ACE description is rewritten to acknowledge the pivot and describe the current system, without disclosing the automation or arbitrage model. Public framing: "supervised pipeline infrastructure for structured professional outputs."
- The Sentinel status is corrected from "In Development" to "In Design" — consistent with [[the-sentinel]] page.
- Each query includes a "what not to say" constraint to prevent the coding agent from inadvertently disclosing the automation stack or arbitrage thesis.
- A QA checklist is included at the end of the plan document for Conley to verify before calling the site live.

---

## [2026-04-14] lint | Full wiki health check — 21 pages audited

**Pages fixed:** 1 (`brand-voice.md` — duplicate `---` divider removed)  
**Pages flagged for follow-up:** 6  
**Open questions raised:** 5

### Issues found

**Orphan pages (2):**
- `portfolio-update-plan.md` — only linked from `log.md`; not referenced from `portfolio-website.md` which it directly serves. Low priority.
- `data-enrichment-apis.md` — not linked from `ace-overview.md` or `tech-stack.md` despite those pages discussing the API waterfall extensively.

**Contradictions / tensions (6):**
- `thought-leader-engine.md` lists a source (`Thought Leader Engine - Project ACE x OpenClaw.md`) not recorded in `index.md`. Source count may be 10, not 9. **Check `raw-sources/`.**
- `index.md` page count jump from 18→19 not documented in the log. `portfolio-update-plan.md` creation may explain this, but the log entry didn't record a count bump.
- `tech-stack.md` LangGraph section explicitly admits use cases are undocumented — this gap persists since the ACE pivot ingest.
- The Proactive Ghost is framed as a "fourth commercial track" in `ace-overview.md` but is listed under Projects in the index — structural tension worth resolving as the product matures.
- `the-sentinel.md` status ("Alpha Prototype Phase — aspirational / in planning") doesn't match the phrasing `portfolio-update-plan.md` specifies for the live site ("In Design"). These should be aligned.
- `conley-potter.md` says "Engaged to Sami"; `portfolio-update-plan.md` Q3 copy says "my wife Sami." Verify current status before About page goes live.

**Stale information (4):**
- `tech-stack.md` — LangGraph use cases still undocumented.
- `conley-potter.md` — "engaged to Sami" may be outdated.
- `portfolio-website.md` — may not reflect actual current site state if the coding-agent queries from `portfolio-update-plan.md` were executed in early April.
- `CLAUDE.md` Known Pages list — `[[tech-stack]]` and `[[the-sentinel]]` were partially addressed; list may need pruning.

**Formatting (1 fixed, 3 flagged):**
- `brand-voice.md` — duplicate `---` divider between "Calm Ambition" and "Five Core Voice Attributes" sections. **Fixed.**
- Most pages use informal `**Tags:**` headers instead of the YAML frontmatter defined in `CLAUDE.md`. Only `thought-leader-engine.md` and `portfolio-update-plan.md` use proper frontmatter. Consider a migration pass or update `CLAUDE.md` to officially accept the informal format.
- `index.md` — `conley-potter.md` listed in both Core Strategy and Identity & Public Presence. Intentional but could confuse scans.

### Suggestions — questions worth investigating

1. Has the `portfolio-update-plan.md` been executed? If so, `portfolio-website.md` needs a state update.
2. What are LangGraph's specific use cases in the current ACE stack? One paragraph would close the `tech-stack.md` gap.
3. Is Conley married or still engaged? Affects `conley-potter.md` and About page copy.
4. Does `raw-sources/` contain `Thought Leader Engine - Project ACE x OpenClaw.md`? If yes, log and index need updating.
5. Are the three blog posts on the portfolio published and live, or placeholders?

---

## [2026-04-14] update | Lint follow-up — 5 corrections from Conley's responses

**Pages updated:** 4 (`tech-stack.md`, `conley-potter.md`, `index.md`, `portfolio-website.md`)

### What changed and why

1. **`portfolio-website.md`** — Added a note to "What Needs Updating" confirming the [[portfolio-update-plan]] queries have **not yet been executed** (Cowork session ran out of tokens mid-query). The site still reflects its April 14 pre-update state. Also added "Blog posts are stubs" as a documented gap.

2. **`tech-stack.md`** — Corrected the LangGraph entry. LangGraph is **not currently deployed** in ACE — it was named as a tool to consider post-pivot, and was included in planning because Conley has direct LangChain experience from ACE legacy builds. It has not been needed at Phase I scale and remains on the roadmap for Phase II/III stateful agent workflows.

3. **`conley-potter.md`** — Added wedding date: **June 12, 2026** (59 days from April 14). Conley is still engaged, not yet married. Also sharpened the framing: 2026 is simultaneously a build year and a marriage year — the tension is literal, not metaphorical.

4. **`index.md`** — Added the missing 10th source: `Thought Leader Engine - Project ACE x OpenClaw.md`. Confirmed to exist in `raw-sources/`. The prior ingest session (which produced `thought-leader-engine.md`) ran out of Claude Cowork tokens before the log/index update step completed. Source count corrected: 9 → 10.

5. **`portfolio-website.md`** (continued) — Clarified that the three blog posts in the Writing section are **placeholder stubs** — titles and topics are defined, but no post content has been written. Added a note that a `writing/` wiki section is a natural future addition when the Personal domain opens.
