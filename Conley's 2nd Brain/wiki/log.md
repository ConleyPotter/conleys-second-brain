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

## [2026-04-14] ingest | 2026 Operating Doctrine

**Source type:** Personal operating doctrine — Conley's written principles, priorities, and commitments for the year
**Pages created:** 6 (`domain-personal.md`, `operating-doctrine-2026.md`, `building-out-loud.md`, `muse.md`, `companion.md`, `book-project-2025.md`)
**Pages updated:** 3 (`conley-potter.md`, `brand-voice.md`, `index.md`)

### What this source contains

A 9-section personal operating doctrine covering Conley's year theme (Consolidation and Signal), the two pillars of his leverage stack (BA and ACE), his creative output stance, public presence doctrine, body and capacity philosophy, relational commitments, inner work orientation, a weekly decision filter, and five end conditions for the year. First source that is explicitly personal rather than ACE-operational.

### What changed

- **`domain-personal.md`** (new) — First Personal domain anchor page. Defines what the domain covers and links out to all Personal-domain pages. Includes the 2026 year-at-a-glance.
- **`operating-doctrine-2026.md`** (new) — Full summary of the doctrine. All nine sections preserved. The decision filter (Section 8) is written as a standing operational tool.
- **`building-out-loud.md`** (new) — Stub for the solo podcast named in the doctrine as the primary public channel for 2026. Notes the distinction from River & Root (separate, broader project; sources forthcoming).
- **`muse.md`**, **`companion.md`**, **`book-project-2025.md`** (new stubs) — Three projects explicitly paused in the doctrine. No detail available yet; Conley intends to return to each.
- **`conley-potter.md`** (updated) — River & Root corrected from "Podcast Concept" to broader long-range project. New "2026 Posture" section added: year theme, paused projects, and decision filter summary.
- **`brand-voice.md`** (updated) — Building Out Loud added as primary channel entry in Channel-Specific Notes.
- **`index.md`** (updated) — Wiki renamed to "Conley Potter's 2nd Brain — Index" to reflect expanded scope. Source count: 10 → 11. Page count: 19 → 26. New Personal section added. Projects section expanded with four new entries.

### Notable observations

- This is the first source that establishes a formal hierarchy between BA and ACE: BA is the income floor; ACE is the owned asset built on top of it. The wiki previously treated BA as background context. The doctrine reframes it as load-bearing infrastructure.
- The decision filter (Section 8) is the most immediately useful operational artifact in this source — a weekly tool that can govern any new request or project consideration.
- Three unnamed 2025 projects (Muse, Companion, book) surface here for the first time. They are named but unexplained; stubs created to hold the space until sources arrive.
- "Building Out Loud" and "River & Root" are now explicitly distinguished. River & Root is broader than a podcast; sources needed before it can be properly documented.
- "Integration beats identity performance" (Section 7) is the most direct articulation of the anti-performance stance that runs through the brand voice — worth surfacing if brand voice is ever revised.

---

## [2026-04-16] ingest | the-river-room-business-plan-v2.md

**Source type:** Full V2 draft business plan for The River Room — community creative commons and digital workshop concept  
**Pages created:** 1 (`the-river-room.md`)  
**Pages updated:** 3 (`conley-potter.md`, `domain-personal.md`, `index.md`)

### What this source contains

A complete 2026 draft business plan for The River Room, a long-range physical community project Conley has been developing. The plan covers vision and values, market opportunity, space design, programming, operations, financial projections, funding strategy, community partnerships, and a phased launch strategy. This is V2 — the significant addition over V1 is a **dual-operation financial model** that introduces a parallel digital revenue strategy (evergreen products, paid community, cohort courses, consulting) as a separate but mission-aligned entity that funds and de-risks the physical space. The physical operation no longer needs to be profitable from day one; it needs to be viable while the digital operation generates surplus capital.

Key data points extracted:
- Three-layer model: The Commons (café/bookshop, open to all), The Studio (membership creative co-working), The Workshop (AI/digital skills co-op with corporate training as highest-margin stream)
- Startup cost estimate: $172K–$336K total
- Combined 4-year revenue: up to $462K–$742K by Year 4; net operating position reaches $202K–$372K by Year 4
- Year 3 threshold built into the plan: if digital operation isn't generating ≥$75K annually, a formal strategic review triggers
- Funding sources include digital revenue pre-accumulation of $40K–$80K — explicitly the ACE-equivalent digital operation
- Phased launch: Phase 0 is building-independent (pop-up workshops, newsletter) and can begin immediately
- AutoBoost named as a formal strategic partner for the digital clinic

### What changed

- **`the-river-room.md`** (new) — Full summary page. Covers all nine sections of the business plan with key tables preserved. Includes connections to [[conley-potter]], [[brand-voice]], [[the-sentinel]], [[financial-projections]], and [[operating-doctrine-2026]]. Five open questions filed at the bottom — most importantly: does the "companion Digital Revenue Strategy document" referenced in the financial section exist?
- **`conley-potter.md`** — Long-Range Vision Projects section: The River Room entry expanded from one vague sentence to a full paragraph describing the three-layer model, V2 financial structure, current status (pre-Phase 0), and link to the new page. `[[the-river-room]]` added to Related.
- **`domain-personal.md`** — `[[the-river-room]]` added to the Pages in this domain table and to Related. It belongs in Personal domain: it's a long-range community project, not an ACE operation.
- **`index.md`** — Source count 11→12, page count 26→27. `[[the-river-room]]` added to Projects section. New source row added to Source Files.

### Notable observations

- The V2 plan's dual-operation structure is a direct application of Conley's ACE mental model to a physical business. The digital revenue operation described for The River Room is structurally identical to what ACE is building: evergreen products, paid community, cohort courses, consulting. This is not incidental — it's the most concrete evidence that ACE's architecture is being designed with The River Room in mind.
- AutoBoost appears as a named strategic partner for the digital clinic (co-branding + client referral pipeline). This is the only place in the wiki where Conley's day job and a long-range personal project intersect operationally. Worth monitoring: this is either a future conversation with Adam Kushner or a plan Conley hasn't surfaced yet.
- "Human First" and "Honest and Useful" — the River Room's stated core values — are direct echoes of the documented brand voice. The plan reads as an expression of the same identity that informs ACE's public-facing stance.
- The plan distinguishes Building Out Loud (2026 active podcast) from the River Room programming (future speaker series, River Room Creative Summit) without naming the connection. River & Root also appears unresolved. All three share thematic DNA: place, community, audio/conversation, Susquehanna Valley.
- Phase 0 requires no building and costs almost nothing. It could start today under the 2026 operating doctrine's decision filter — IF Conley decides The River Room qualifies as a 2026 priority (it's currently classified as long-range, not active). The plan itself anticipates that the digital revenue operation starts before the physical space opens.

---

## [2026-04-16] ingest | Daily-Recap_2026-04-15.md

**Source type:** BA workday log — Gmail sent mail, HubSpot calls/notes, Slack (BA + AutoVitals workspaces), Claude chat history  
**Pages created:** 1 (`daily-recap-2026-04-15.md`)  
**Pages updated:** 3 (`conley-potter.md`, `index.md`, `log.md`)

### What this source contains

A structured end-of-day recap of Conley's BA workday on Wednesday, April 15, 2026. High-volume operational day:

- **5 client follow-up emails**: Heights Expert Automotive (Heather), Bernhard Auto Works (Dave), Chris Knopp/Paul Marsh website onboarding, Mike @ Mechanics of West Allis, Jaime (new inbound via AutoBoost form).
- **4 partner/referral threads**: Turnkey Auto Marketing (Jared Baker — Advanced LSA inquiry for a multi-shop "huge stinking deal"; Suzanne Berger — new client referral), AutoVitals (Carly Lama — billing transfer + Stan performance; Carlos Massaquoi — search terms vs. search themes clarification; Shelby Maggard — Lael's meeting rescheduling).
- **6 substantive HubSpot calls**: Kevin @ Exclusively Imports (33 min monthly review), Andy Makarevich (no-show), Brian @ Legacy Auto Care (31 min new prospect), Gina @ Metric Motors + Adam (49 min, Adam-led).
- **1 handbook policy change**: Conley identified a travel time compensation clause that conflicts with 29 C.F.R. § 785.37; recommended removal; Adam agreed same day.
- **1 healthcare discussion**: Micah exploring 100% minimum tier coverage ($310 vs. $155 current employee share).
- **13 open items carrying forward** across clients, partners, and internal policy.

### What changed

- **`daily-recap-2026-04-15.md`** (new) — Full summary page. Covers all 9 operational sections, open items table, and a "What This Reveals" synthesis section. New page type: `log` (first in the Day Job Logs category).
- **`conley-potter.md`** (updated) — Two additions:
  1. **Partner ecosystem section** (under Day Job): Turnkey Auto Marketing and AutoVitals named as primary referral/co-delivery channels with key contacts.
  2. **Legal/compliance proactivity paragraph** (under Working Style): The 29 C.F.R. § 785.37 incident documented as a concrete example of how Conley operates in his BA role.
  LSA also added explicitly to the BA services line (was implied but not named).
- **`index.md`** (updated) — Source count 12→13, page count 27→28. New "Day Job Logs" section added. New source row added.

### Notable observations

- The partner ecosystem (Turnkey + AutoVitals) is structurally important for BA's business — referrals, co-managed clients, and service scope questions all flow through these channels. This was previously undocumented in the wiki.
- The FLSA compliance catch is the clearest operational example of what "Director of Client Success & Strategy" behavior looks like at BA — unsolicited, legally literate, corrective, and immediately effective. Worth referencing if the formal title alignment ever needs justification.
- The distinction between *search terms* (Search campaigns) and *search themes* (Performance Max) that Conley explained to Carlos is a signal that BA's clients are running Performance Max campaigns — a nuance that affects reporting and optimization decisions.
- 13 open items after a single day suggests the BA role is consistently high-load. The 2026 operating doctrine designates BA as the "income foundation" — this log shows the operational density that entails.

---

## [2026-04-16] query | Wiki structure planning — how to expand beyond ACE

**What was asked:** How to evolve the wiki structure to be comprehensive across all life domains (not just ACE), whether to stay flat or split into segments, how many new wikis to create for concepts from the weekly/daily summaries, and what changes to make to CLAUDE.md.

**How it was answered:** Full codebase read — all raw sources and wiki pages reviewed. Synthesis filed as a standing page.

**Page created:** `wiki-structure-planning.md` (type: `synthesis`)  
**Pages updated:** `index.md` (Meta section added, page count 28→29)

### Summary of recommendations

- **Stay flat** (no subfolders) until ~80 pages; solve organization via domain frontmatter and `index.md` discipline
- **6 new BA domain pages**: `ba-overview.md`, `ba-products.md`, `ba-partners.md`, `ba-team.md`, `ba-clients-pipeline.md`, `adam-shop-incubator.md`
- **1 new weekly recap page**: `weekly-recap-2026-04-06.md` for the Apr 6–12 source
- **New page type**: `work-log` (archival, dated, never modified post-creation)
- **CLAUDE.md changes**: add `work-log` type, update active domains, add `domain:` frontmatter field, add rolling vs. archival distinction, add recurring-source ingest pattern, update index section list

---

## [2026-04-16] lint | Frontmatter standardization — 17 pages converted to YAML

**Pages fixed:** 18 (`ace-overview.md`, `conley-potter.md`, `financial-projections.md`, `platform-comparison.md`, `tech-stack.md`, `client-acquisition.md`, `phase-1-lead-enrichment.md`, `data-enrichment-apis.md`, `phase-2-content-vectors.md`, `phase-3-infrastructure.md`, `campaign-plan.md`, `brand-voice.md`, `upwork-portfolio.md`, `career-history.md`, `portfolio-website.md`, `ace-legacy.md`, `the-sentinel.md`, `daily-recap-2026-04-15.md`)  
**Suggestions made:** 0

### Issues found and fixed

**Frontmatter format inconsistency (17 pages):**  
The prior lint flagged that most pages used informal `**Tags:**` / `**Sources:**` inline headers instead of the YAML frontmatter defined in CLAUDE.md. All 17 affected pages have been converted to proper YAML format:

```yaml
---
type: [page type]
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
---
```

The inline `**Tags:**` and `**Sources:**` lines were removed from page bodies. The `**Related:**` lines were preserved in place — `related` is not a frontmatter field in the CLAUDE.md schema.

**Source name normalization:** Inline source references that used shorthand (e.g., "Business Plan", "Phase 1 Reference Brief") were expanded to match actual raw-source filenames (e.g., `ACE Business Plan_ Autonomous Freelance Agent.md`, `ACE Phase 1 Reference Brief.md`).

**Missing `updated:` field (1 page):**  
`daily-recap-2026-04-15.md` was missing the `updated:` field. Added `updated: 2026-04-16`.

### Remaining known issues (not addressed in this pass)

- The article ends deliberately open — "I don't know yet" — which is consistent with [[brand-voice]] honesty and avoids the temptation to package uncertainty as a lesson. This is the right call for a first piece.
- The team adaptation section is intentionally brief. It names the pattern without overexplaining it. The audience for a portfolio piece doesn't need the implementation details; they need to understand that the model generalizes.
- "I'm building this. You're welcome to watch." appears both as the final sentence of the article and as the *Building Out Loud* positioning statement. That's not coincidence — this piece is the first concrete expression of that public stance in writing.
- The article credits Karpathy by name and Fu by name. Both attributions are appropriate and make the piece feel grounded rather than self-congratulatory.

---

## [2026-04-17] ingest | BA Team Roster.md

**Source type:** Official BA active team roster — 13 members with formal titles, Slack display names, locations, and role/responsibility summaries  
**Pages created:** 0  
**Pages updated:** 4 (`ba-team.md`, `ba-overview.md`, `conley-potter.md`, `ba-clients-pipeline.md`)

### What this source contains

The first official BA team roster in the wiki. Confirms or corrects all prior inferred roles from behavioral observation. Documents 13 active team members: Adam Kushner (Founder & CEO), Micah Dilts (Acting COO), Conley Potter (Digital Marketing Project Manager), Jon Fonner (Google Ads Lead), Courtney Nguyen (Content Strategist), Van Nguyen (Content/Creative, part-time remote, New Orleans), Ethan Wauls (Analytics), Kyle Sarnowski (Video Production Associate), Josh Carson (Lead Software Engineer), Daniel Tobias (Junior SE), Jahson Gonzalez-Allie (Junior SE), Adam Hicks (Paid Media Specialist), Abby Steele (Digital Marketing). Slack names, locations, and internal naming conventions (e.g., "Hicks" for Adam Hicks) confirmed. The engineering team structure (Josh → Daniel + Jahson) documented for the first time. BA uses Scrum/Kanban methodology with Micah as Product Owner and Conley as Sprint Planning stakeholder.

### What changed

- **`ba-team.md`** — Major rewrite. Three significant corrections from prior inferred-role version:
  1. **Courtney Nguyen** was incorrectly described as "Scheduling / Intake" — corrected to "Content Strategist" and longest-tenured BA employee. Her content leadership role was not previously captured.
  2. **Kyle Sarnowski** was listed as "Role TBD" — now confirmed as "Video Production Associate." BA is actively selling video production as a client service; ~6 months into the role with no client projects sold yet.
  3. **Josh Carson** — last name now confirmed; role confirmed as Lead Software Engineer owning AutoBoost platform and internal tooling. Gauge is BA's internally-built revenue attribution platform, not an external vendor.
  Four new team members added: Van Nguyen, Daniel Tobias, Jahson Gonzalez-Allie (engineering under Josh), Adam Hicks (Paid Media Specialist; was previously undocumented in ba-team.md but appeared in client pipeline). Abby's last name (Steele) confirmed. "Gauge (Josh) — External/Vendor Relationships" section removed since Josh is a BA employee and Gauge is an internal tool. All TODO notes for title verification removed — now answered by the official roster.

- **`ba-overview.md`** — Key People section expanded from 8 to 13, with confirmed formal titles for all members. Source list and updated date updated.

- **`conley-potter.md`** — Key colleagues list rewritten with all 12 other team members, confirmed titles, and brief role notes. Updated date updated.

- **`ba-clients-pipeline.md`** — STAR Automotive entry corrected: "AV contact: Adam Hicks" label removed. Adam Hicks is a BA employee (Paid Media Specialist), not an AutoVitals contact. The context was Conley asking Hicks about Meta ads for STAR, not an AV-side relationship.

### Notable observations

- Confirming Courtney's role as Content Strategist (not scheduling/intake) is the most significant correction this source delivers. The prior wiki was built only from behavioral observation in daily/weekly recaps, where Courtney's content leadership rarely appeared directly. This is a reminder that role inference from recaps captures what someone *does in Conley's view*, not what they formally own.
- The three-person engineering team (Josh, Daniel, Jahson) is fully focused on AutoBoost platform development and internal tooling. No client-facing engineering is documented. The Gauge attribution platform is their internal product.
- BA has two "Adams": Adam Kushner (CEO) and Adam Hicks (Paid Media). The internal convention — "Hicks" for Adam Hicks — should be preserved in any AI prompts or Slack searches referencing him.
- Van Nguyen (part-time remote, New Orleans) is the only team member outside the in-office Palmyra cluster who wasn't already known. Adds a second remote content resource alongside Courtney.
- Kyle's video production role is explicitly noted as not yet generating client revenue (~6 months in). This suggests BA is internally incubating a new service line — video production for automotive shops — using Kyle as the foundation. Worth tracking whether this converts to client-facing work in future recaps.

---

## [2026-04-17] update | second-brain-article.md revised + writing-style.md created

**Pages updated:** 2 (`second-brain-article.md`, `index.md`)
**Pages created:** 1 (`writing-style.md`)

### What changed and why

Conley reviewed the article and flagged several LLM-tell patterns requiring correction, plus attribution errors. Changes made:

1. **`second-brain-article.md`** — Six categories of revision:
   - Attribution fixed: "Ray C Fu" corrected to "Rui Fu" (@raycfu) with link to raycfu.com throughout; naming claim removed ("something I've been calling the second brain method"); Tiago Forte credited as the originator of the second brain concept with link to buildingasecondbrain.com
   - All em dashes removed and replaced with commas, colons, semicolons, or periods
   - "It's not memory — it's a schema" rewritten: "A schema rather than memory, a way of making the model's behavior consistent across sessions"
   - "It's not just bookkeeping. It's the continuity..." rewritten as single prose sentence
   - Bold + em dash inline headers in "What it is" section restructured to flowing prose ("The first is... The second is... The third is...")
   - Bold + period inline headers in "What makes it work" section converted to plain prose paragraphs
   - Domain list expanded from three to four (ACE, BA, Personal, meta) to break uniform rule-of-three pattern
   - External links added: Obsidian (obsidian.md), Claude Code (claude.ai/code), Rui Fu (raycfu.com), Tiago Forte (buildingasecondbrain.com)
   - `updated` frontmatter date: 2026-04-16 → 2026-04-17

2. **`writing-style.md`** (new, type: `asset`, domain: `personal`) — Comprehensive reference documenting Conley's writing mechanics and conventions. Covers: LLM-tells to eliminate (em dashes, "it's not X it's Y" patterns, uniform three-item lists, bold + em dash headers), formatting conventions (bold header rules, sentence fragments), punctuation standards, linking and attribution rules, and positive style targets. References [[brand-voice]] for voice/tone without duplicating it. Designed as a living document.

3. **`index.md`** — Page count 38 → 39. `[[writing-style]]` added to Meta section.

### Notable observations

- The em dash removal is the most structurally significant edit. Replacing them forced sentence-level rewrites that produced more varied and direct prose throughout the article. The constraint is productive.
- The Tiago Forte attribution adds appropriate humility and a credible external link. Forte's site (buildingasecondbrain.com) is a high-authority link that supports SEO.
- The `writing-style.md` page is deliberately distinct from `brand-voice.md`: brand voice is about who Conley is when he writes; writing style is about the craft mechanics that express that identity without LLM contamination.

---

## [2026-04-17] ingest | Daily Recap — April 16, 2026

**Source type:** BA daily work log — split office/travel day; FLACA conference departure, morning client meetings, afternoon covered by Jon and Adam while Conley traveled  
**Pages created:** 1 (`daily-recap-2026-04-16.md`)  
**Pages updated:** 3 (`ba-clients-pipeline.md`, `ba-partners.md`, `ba-overview.md`)

### What this source contains

A full workday covering three morning client meetings (Kidders Repair, Twenty First Century Auto, 59 Auto Repair), extensive Jon-coordination DMs across six accounts, the Tilson's Auto Repair disengagement, Mechanics of West Allis finally booking, Metric Motors tier proposals in #internal-sales, and Conley's solo departure to the FLACA conference in Orlando. Day ended with exhibitor setup at the venue through 9:15 PM. 15 open items carrying forward.

### What changed

- `ba-clients-pipeline.md` — Multiple status updates: Tilson's Auto changed to "Closed — Prospect Dropped"; Kidders Repair updated from "pending call" to "call attended, follow-up needed"; Metric Motors updated with three proposed service tiers and sales deck assigned to team; Mechanics of West Allis updated from "Prospect / rescheduling" to "Booked." Three new entries added: A&R Complete Auto (Taina departed, Angie now sole contact), Save More Automotive / Brenner Newman (April promos in motion), Kennedy's (declined call tracking overlay, not offboarding). Sources and updated date refreshed.
- `ba-partners.md` — AutoVitals contact "Jordan" updated to full name "Jordan Bania" with expanded role note (confirmed on monthly Google Ads review calls). Stephen Baker added as new AV contact (present on Kidders Repair intro call Apr 16). Sources and updated date refreshed.
- `ba-overview.md` — Two additions: (1) HubSpot AI post-call summaries note under Tooling — Micah confirmed the new capabilities can replace the "assign to client success" workflow; (2) Industry conferences section added under Partner Ecosystem — documents BA's active conference presence (TEKTONIC week of Apr 6–12, FLACA Apr 16–20). Sources and updated date refreshed.

### Notable observations

- Tilson's Auto dropping after sitting in "Decision Maker Bought-In" is a useful data point on the reliability of that HubSpot stage. The AV-paper close mechanism (LSA deals closing on AutoVitals billing cycles) appears to create friction or delay that can kill deals if momentum cools. Worth watching for this pattern in other AV-referred prospects.
- Conley and Jon's mutual, low-drama decision to drop Tilson's suggests operational maturity about pipeline hygiene — they're not chasing dead weight. The "bad vibes" framing is worth noting as an informal filter Conley applies, and it appears to correlate with deals that were always going to be difficult closes.
- The Brenner Newman "even he's feeling it now" observation about slow business is the first market-softness signal in the recap series. If similar language appears across multiple clients in April/May, it could signal a seasonal dip affecting BA's upsell and renewal rate. Flag if it recurs.
- BA is now running two back-to-back industry conferences (TEKTONIC + FLACA) in the same two-week stretch. The team split — Adam/Jon for TEKTONIC, Conley solo for FLACA — suggests BA has enough coverage bandwidth to field multiple events simultaneously. This is worth cross-referencing if FLACA-sourced contacts appear in later pipeline recaps.
- Jordan Bania's full name confirmed. Prior wiki entries used "Jordan" only. The Two Adams convention (CEO vs. Paid Media Specialist) documented in the BA Team Roster ingest now has a parallel case: two named "Jordan" contacts at different levels could cause confusion in future recaps without full names.

---

## [2026-04-17] ingest | Opus 4.7 Thread by Boris Cherny

**Source type:** External social post (Threads, @boris_cherny) — post #6 in a numbered thread about Claude Opus 4.7 workflow optimization  
**Pages created:** 2 (`opus-4-7-workflow.md`, `domain-general.md`)  
**Pages updated:** 2 (`tech-stack.md`, `index.md`)

### What this source contains

A short but high-signal Threads post from Boris Cherny (April 16, 2026) on getting the most out of Claude Opus 4.7. The core argument: give Claude a way to verify its own work, and you 2–3x what you get from it — this was always true, but it matters more as the model gets more agentic. Verification method varies by context: bash/server for backend, the Claude Chromium extension for frontend, computer use for desktop apps. Recommended workflow for long-running tasks: (1) test end to end, (2) run `/simplify`, (3) put up a PR. The broader framing: Opus 4.7 is a meaningful leap once you restructure your workflow to match its longer autonomous runs — not just a drop-in upgrade to old habits.

### What changed

- `opus-4-7-workflow.md` (new) — Synthesis page documenting Cherny's workflow patterns, the verification matrix by context type, the three-step workflow, and the relevance to ACE's HITL co-pilot mode and the 15-hour operator constraint.
- `domain-general.md` (new) — First General Knowledge domain anchor page, created per CLAUDE.md convention ("when a new domain becomes active, create a domain page"). Defines what the domain covers and links to all pages in it. This is the first external article ingested into the wiki.
- `tech-stack.md` — Added Claude Opus as a named entry under LLM Calls. Previously, Claude appeared only in the OPEX budget line and the OpenClaw router model strategy blurb, but had no dedicated stack entry. Added Opus 4.7 as the current version with a note on the verification-first workflow pattern. `updated` date bumped to 2026-04-17.
- `index.md` — Source count 17→18, page count 40→42. New General Knowledge section added with both new pages. New source row added.

### Notable observations

- This is the first "General knowledge" source in the wiki — the expansion path has officially started. The domain is thin (one post) but the anchor is in place. Future articles, podcast notes, and research clippings now have a home.
- The verification-first workflow pattern from Cherny is directly applicable to how Conley uses Claude Code in this wiki's own maintenance (the `/simplify` skill is already in use). The advice is self-referential.
- Opus 4.7 running longer and more autonomously changes the economics of the HITL gate in ACE. If the model can self-verify and run extended workstreams, the operator's role compresses further toward final approval rather than active monitoring. This is additive to ACE's core thesis about operator bandwidth.
- The Chromium extension for frontend verification is a new tool not yet mentioned anywhere else in the wiki. Worth noting if ACE's Phase II (SEO content workflows) eventually involves frontend verification steps.

---

## [2026-04-17] ingest | LLM Wiki Pattern + OpenAI Codex App + gstack

**Source type:** Three external articles — pattern document, product announcement, open-source README  
**Pages created:** 3 (`llm-wiki-pattern.md`, `openai-codex-app.md`, `gstack.md`)  
**Pages updated:** 5 (`domain-general.md`, `second-brain-article.md`, `opus-4-7-workflow.md`, `index.md`, `log.md`)

### What these sources contain

**CLAUDE.md from Kaparthy.md** — An abstract pattern document (associated with Andrej Karpathy) titled "LLM Wiki." Describes the conceptual architecture underlying this second brain: three layers (raw sources / wiki / schema), three operations (ingest / query / lint), and two navigation files (index.md / log.md). The document is intentionally implementation-agnostic — its job is to communicate the pattern, not prescribe a stack. This is the intellectual source that `second-brain-article.md` references when it credits Karpathy's approach.

**Codex for (almost) everything.md** — OpenAI's April 15, 2026 blog post announcing a major update to the Codex desktop app. Five new capability categories: background computer use (parallel agents, own cursor, non-interfering), in-app browser with direct page commenting, gpt-image-1.5 image generation, 90+ new plugins (JIRA, GitLab, CircleCI, MS Suite, Neon), and expanded SDK lifecycle features (PR review, multi-terminal, SSH to remote devboxes). Plus: memory across sessions, automations that can wake up to continue long-term tasks across days/weeks, and proactive task suggestions based on projects + memory + plugins.

**garrytangstack README** — Garry Tan's (YC CEO) open-source Claude Code sprint framework. 23+ specialist slash commands (CEO, designer, eng manager, QA, security, release) organized as a repeatable sprint: Think → Plan → Build → Review → Test → Ship → Reflect. Stats: 600K+ LOC in 60 days, 10–20K LOC/day part-time. Key skills: `/office-hours` (6 forcing questions), `/autoplan` (full review pipeline in one command), `/qa` (real Chromium browser with auto-generated regression tests), `/cso` (OWASP + STRIDE), `/ship`. Parallel sprints via Conductor (10–15 Claude Code sessions). Integrates with OpenClaw via ACP dispatch. MIT licensed, free.

### What changed

- `llm-wiki-pattern.md` (new) — Synthesis page documenting the three-layer architecture, three operations, two navigation files, division of labor, applicable domains, optional infrastructure (qmd, Obsidian, Marp, git), and the connection to Vannevar Bush's Memex. Connects explicitly back to how this wiki implements the pattern.
- `openai-codex-app.md` (new) — Tool analysis page covering all five capability categories, competitive context vs. Claude Code / gstack, and the ACE relevance note (Codex's automation roadmap is converging on the same endpoint as ACE's HITL architecture).
- `gstack.md` (new) — Tool analysis page: sprint process, full skill tables (planning / build+review / ship / design pipeline / power tools), parallel sprint model, OpenClaw dispatch patterns, and relationship to Karpathy's AI coding rules.
- `domain-general.md` — Three new rows added to the pages table. `updated` date unchanged (already 2026-04-17).
- `second-brain-article.md` — `[[llm-wiki-pattern]]` added to the Related line. The article already credits Karpathy at the bottom; this creates the formal wiki cross-link.
- `opus-4-7-workflow.md` — New "Related Tooling" section added at the end, cross-referencing `[[gstack]]` and `[[openai-codex-app]]` as the workflow enforcement layer and competitive context respectively. `[[gstack]]` added to Related. Source list updated.
- `index.md` — Source count 18→21, page count 42→45. Three rows added to General Knowledge section. Three rows added to Source Files.

### Notable observations

- The Karpathy LLM wiki pattern is the conceptual source of this entire second brain, but until now it had no wiki page. Filing it closes a notable gap: the system's intellectual foundation is now documented inside the system it founded. The self-referential loop is complete.
- gstack's OpenClaw integration is the most operationally relevant connection for ACE. If Conley ever runs multi-session development sprints for ACE Phase II/III infrastructure, gstack's dispatch model (OpenClaw → Claude Code → /autoplan → implement → /ship) could significantly compress operator time. Worth revisiting when Phase II work begins.
- OpenAI Codex's scheduled autonomous work (wake up and continue long-term tasks across days/weeks) is the feature to watch. If it matures, it represents a direct challenge to the HITL co-pilot architecture that ACE is building — a model where the agent doesn't need a human to restart it. Claude Code and OpenClaw don't yet have this natively.
- All three articles cluster around the same moment in AI tooling: April 2026, when agentic developer tools are rapidly acquiring memory, verification, and extended autonomy. The wiki's General Knowledge domain is becoming a useful lens for tracking this shift as it unfolds.
- gstack's /retro stats (140K+ lines, 362 commits, ~115K net LOC in one week for one person) are the most concrete published evidence of the "single builder as team" thesis that ACE's arbitrage model is built on. Worth referencing in client acquisition or positioning conversations.

---

## [2026-04-18] ingest | Resume Variants + MarkItDown Tool

**Source type:** Three targeted resume variants (July 2025) + one GitHub README for a PDF-to-Markdown conversion tool  
**Pages created:** 2 (`resume-variants.md`, `markitdown.md`)  
**Pages updated:** 3 (`career-history.md`, `llm-wiki-pattern.md`, `index.md`)

### What these sources contain

**Conley-Potter-Resume-July-2025.md / -AI.md / -ADS.md** — Three variants of the same base resume, each with a distinct Summary and Core Competencies section targeting a different audience. The General variant targets mission-driven/values-aligned organizations ("7+ years, sustainability, health equity"). The AI variant targets B2B SaaS and marketing automation roles ("7+ years, AI-powered automation, GTM, revenue enablement"). The ADS variant targets eCommerce and performance marketing roles ("4+ years" of paid media specifically — narrower framing than the other two). All three share the same five jobs, same education (App Academy + UW-Madison), and same base skills list.

**microsoftmarkitdown README** — GitHub README for microsoft/markitdown, the open-source Python utility Conley uses to convert PDFs and Office documents to Markdown before dropping them into `raw-sources/`. Supports PDF, Word, PowerPoint, Excel, images, audio, YouTube, EPubs. Has an MCP server (markitdown-mcp) for Claude Desktop integration, a markitdown-ocr plugin for LLM-vision OCR of embedded images, and an Azure Document Intelligence path for enterprise-grade conversion.

### What changed

- `resume-variants.md` (new) — Documents all three resume variants with target audiences, positioning strategy, skills deltas between versions, the "4+ vs 7+" experience framing explained, and gaps in the current variant set. Cross-links to `career-history`, `portfolio-website`, `conley-potter`.
- `markitdown.md` (new) — Tool analysis page covering what it is, how Conley uses it in the raw-sources ingest pipeline, all supported formats, CLI and Python API usage, MCP server and OCR plugin, breaking changes from 0.1.0, and how it compares to textract and manual alternatives.
- `career-history.md` — Added two previously missing entries: App Academy coding bootcamp (Feb–Sep 2019, San Francisco) and Freelance Web Developer and SEO Consultant (Aug 2019 – Jan 2021, Madison, WI). This is a distinct role from the later Lancaster-based Freelance Digital Marketing Director position. The Madison web dev period — missed in prior ingests — is now part of the documented timeline. Source list updated.
- `llm-wiki-pattern.md` — Added markitdown to the Optional Infrastructure section as the ingest bridge. Cross-link to `[[markitdown]]` added.
- `index.md` — Source count 21→25, page count 45→47, `resume-variants` added to Identity & Public Presence, `markitdown` added to General Knowledge, four new source rows added. `career-history` summary updated to reflect the now-complete timeline.

### Notable observations

- The resumes reveal a gap in `career-history` that persisted across all prior ingests: the Madison freelance web dev period (Aug 2019 – Jan 2021) is a distinct phase between App Academy and the Lancaster marketing career. Prior sources (portfolio, saved memories) didn't make this explicit. The career timeline is now complete.
- The ADS resume's "4+ years" claim is intentional and legitimate: it scopes to paid media management specifically, not total marketing tenure. But it's a potential candidate for confusion in a job search context — worth being explicit about if asked directly.
- Three resume variants exist; none targets director/VP-level strategic leadership or nonprofit community leadership explicitly. The July 2025 dating also means the current AutoBoost role is absent from all three. A refresh incorporating BA and ACE (in appropriate framing) would increase positioning accuracy.
- markitdown is now the documented entry point for getting non-text documents (PDFs, Word files, etc.) into the raw-sources ingest pipeline. Its MCP server option could eventually allow Claude Desktop to convert and ingest documents in a single step, bypassing the CLI entirely.
- The three resume variants, markitdown, and the prior gstack/Codex/Karpathy entries collectively signal that Conley is actively instrumenting his personal infrastructure — not just ACE as a product, but his own career operating system.

---

## [2026-04-18] update | Portfolio update plan expanded — Work timeline + Capabilities

**Pages updated:** 3 (`portfolio-update-plan.md`, `portfolio-website.md`, `index.md`)

### What changed

- `portfolio-update-plan.md` — Added Query 7 (Work page career timeline update) to add the missing Madison freelance web developer role (Aug 2019 – Jan 2021) and App Academy (Feb–Sep 2019) to the site's Work section. Expanded Query 6 (Capabilities) with the full skills inventory from the three resume variants: Ruby on Rails, React/Next.js/Tailwind CSS, specific Salesforce suite tools (Marketing Cloud, SF Data Cloud, Marketing Intelligence Cloud), paid media platforms (Meta Ads, TikTok Ads, Google Shopping specifically), ManyChat, and Zapier. Updated the status table to reflect the new Query 7 and renumbered the Upwork URL deferral to Query 8. Corrected the "What NOT to Change" note that incorrectly stated the Work page timeline was accurate as-is. Added QA checklist items for the new Work timeline and expanded Capabilities entries.
- `portfolio-website.md` — Added ⚠️ flag to the Work page timeline noting the two missing entries. Added two new bullets to the "What Needs Updating" section for the timeline gap and the stale Capabilities section.

### Notable observations

- The portfolio's Work page gap is significant: skipping from Epic (Sep 2018) directly to Freelance Digital Marketing Director (Jan 2021) creates a 2.5-year black hole that now has content. The App Academy → Madison web dev arc is one of the more distinctive things about Conley's career — the self-directed technical pivot is part of what makes the Lit degree + systems architecture story credible.
- The Capabilities gap is also meaningful: React/Next.js/Tailwind and Ruby/Rails are the foundations of the web dev period and remain current skills. Listing them correctly signals depth that "Python, JavaScript, SQL" alone doesn't convey.
- These gaps were invisible until the resumes were ingested — which is exactly the kind of cross-source contradiction the wiki is designed to surface.

---

## [2026-04-18] ingest | portfolio-website-about-page-4-18.md

**Source type:** Finalized About page copy — full text of the About page in its pre-launch state, plus career history sidebar content and Interests tags  
**Pages created:** 0  
**Pages updated:** 4 (`portfolio-update-plan.md`, `portfolio-website.md`, `conley-potter.md`, `index.md`)

### What this source contains

The About page copy in its finalized state as of April 18, 2026. Conley describes this as potentially the final version before site launch. The source documents:

- **Lead paragraph and honest follow-through:** "I work at the intersection of marketing operations and systems architecture. Day job: leading client success and growth at AutoBoost..." — direct, non-abstract, with day job / ACE / Sentinel described cleanly.
- **"The Scenic Route" section:** Full education arc — DePaul CS → UW-Madison English Lit + Chinese → nonprofit sector management (12 staff, multi-grant budget, housing and financial counseling) → retraining at App Academy. The journey that earns the Lit → systems architecture conclusion.
- **"Philosophy of Work" / calm ambition:** Intact and in Conley's voice.
- **"Outside of Work":** AT corridor near Harrisburg, restaurant background, fibromyalgia, fiancée Sami, June wedding, 2026 as build + wedding year simultaneously.
- **Closing paragraph:** Observational/invitation energy — Consulting section for hiring inquiries; documentation for builders watching.
- **Career history sidebar:** Current role card reads "Client Success & Growth Leader | AutoBoost | Business Actualization | Digital Transformation, AI Integration." Previous section shows only 2 entries (Stoltzfus, Lancaster Freelance) with 4 entries missing: Tenfold, Madison Freelance, App Academy, Epic Systems.

This source also confirms that Query 3 of [[portfolio-update-plan]] has been executed and the About page copy is finalized.

### What changed

- **`portfolio-update-plan.md`** — Query 3 marked ✅ Complete with a summary of what was changed. Original Query 3 spec archived in-document for reference. New Query 8 added for the career history sidebar (adding 4 missing roles: Tenfold, Madison Freelance, App Academy, Epic; correcting Stoltzfus dates). Former Query 8 (Upwork URL) renumbered to Query 9. Status table updated. QA checklist expanded with sidebar verification items and role card title check.
- **`portfolio-website.md`** — Current Role section updated from "Lead Initiatives & Systems Architect" to "Client Success & Growth Leader" with a note on the April 2026 title change. "Personal voice / About page" item in "What Needs Updating" marked resolved. Source list updated.
- **`conley-potter.md`** — Portfolio role card title updated from "Lead Initiatives & Systems Architect" to "Client Success & Growth Leader."
- **`index.md`** — Source count 25→26. `portfolio-update-plan` summary updated to reflect 9 total queries and current completion status. New source row added.

### Notable observations

- The about page finalization is the clearest signal yet that the portfolio is approaching launch readiness. Queries 1–4 are now complete. The remaining pending work (Queries 5–8) is self-contained and can be executed independently.
- The title change from "Lead Initiatives & Systems Architect" (aspirational/descriptive) to "Client Success & Growth Leader" (functional/accurate) reflects a shift in how Conley wants to present the BA role publicly. The new title is more aligned with the actual work — client outcomes, growth, success metrics — rather than the systems architecture framing that belongs more to the ACE persona.
- The sidebar gap (4 missing career entries) is the same gap identified in the Work page timeline (Query 7), but manifesting in a different component. Tenfold in particular is absent from both the sidebar and the Work page — yet it's the role the About page copy references most explicitly in the "load-bearing context" passage. The copy and the sidebar are currently contradicting each other on this point.
- The AT corridor is described as "near Harrisburg, PA" in the about page — the wiki had this as "near Lancaster" and "Susquehanna Valley." Harrisburg and Lancaster are both correct (the AT corridor runs northeast of both); "near Harrisburg" is more precise for the specific section Conley hikes. Minor, but accurate.

---

## [2026-04-18] query | Second brain as MCP server — gstack integration synthesis

**Pages created:** 1 (`second-brain-mcp-server.md`)
**Pages updated:** 1 (`index.md`)

### What was asked

Conley asked: if this second brain project were turned into an MCP server, how could it integrate into a workflow using gstack — with all the personalized knowledge and wiki schema informing that workflow?

### How it was answered

Filed as a synthesis page rather than a chat answer because the question is comparative, architectural, and likely to be revisited. The page covers:

- Why the problem exists (gstack and the second brain currently operate in separate contexts; every Claude Code session starts cold)
- What MCP tools the server would expose: seven tools covering read, search, list, write, log append, index, and schema retrieval
- Which gstack skills benefit most and how: `/office-hours` (constraints surfaced before planning), `/autoplan` and `/plan-ceo-review` (strategic context grounds scope), `/design-consultation` and `/design-review` (brand voice loaded automatically), `/retro` (output flows directly to log.md), `/learn` (session learnings write back to wiki instead of local JSONL), `/cso` (tech stack context before threat modeling)
- The compounding effect: wiki grows from discrete ingest sessions to continuous growth via sprint artifacts
- Parallel sprint context: all 10–15 Conductor sessions share the same wiki; concurrent write coordination is the main unsolved problem
- A three-phase implementation path: Phase 1 (read-only, weekend project), Phase 2 (write-back + log integration), Phase 3 (semantic search + `wiki_query` tool)
- Four open questions: schema enforcement on writes, concurrent write coordination, `/learn` migration strategy, n8n integration loop

### Notable observations

- Phase 1 (read-only MCP server) has a high effort-to-value ratio: even without write-back, every gstack session gaining automatic access to [[operating-doctrine-2026]], [[brand-voice]], and [[ace-overview]] materially improves planning quality.
- The `/retro` write-back is the highest-leverage integration in Phase 2. It closes the loop between sprint execution and wiki memory without requiring any new behavior from Conley — the retro was already running; now its output lands somewhere permanent.
- The n8n connection (noted in CLAUDE.md as an automation opportunity for raw-sources ingest) converges with the MCP server build. If n8n watches the wiki directory for writes from the MCP server, the full data flow — source arrives → wiki updated → gstack session aware → sprint output logged — becomes automated end to end.
- The page explicitly flags that nothing described exists yet. Priority question: does this get built before or after ACE Phase I generates its first client contract?

---

## [2026-04-18] update | ba-overview.md — direct corrections from Conley

**Pages updated:** 1 (`ba-overview.md`)

### What changed

Conley answered six open questions from the wiki TODO audit. All TODOs in `ba-overview.md` are now resolved.

- **Company rebrand:** Business Actualization has rebranded to AutoBoost. Page title and "What It Is" section updated to reflect this. AutoBoost is the company name, not a SaaS product — the SaaS framing was incorrect.
- **AutoBoost product clarification:** The client-facing software platforms (review, call tracking, revenue attribution) are white-labeled tools bundled into service delivery, not independently sold software. Not analogous to Kukui.
- **Founding year and headcount:** Founded 2001; current headcount 13 (was listed as ~15 — corrected).
- **ARR:** ~$2.5M confirmed. Revenue section updated; TODO removed.
- **Flatarchy proposal:** Dropped. Not being actively pursued. Concepts may resurface as org structure formalizes, but no active initiative.
- **Director role scope:** Conley has been performing Director-level work for 2+ months. Formal title change would be recognition + authority, not a function change. Concrete delta documented: client retention/escalation ownership, seat at three-person leadership table, authority over service delivery standards and onboarding, compensation alignment ($85K–$120K base range confirmed).
- **Internal tech stack:** Full service delivery and internal ops stack documented — Duda (websites), Agency Analytics (reporting), Birdeye white-label (review), CallRail white-label (call tracking), GoDaddy → Route 53 → CloudFront/ACM (DNS/hosting), plus Google Ads/Meta/Reddit/Bing/Programmatic/LSA. Internal ops: HubSpot, Slack, Google Workspace, Hubstaff, n8n, Anthropic API/Claude/Cowork, Notion (Conley only).

### Notable observations

- The AutoBoost rebrand is architecturally significant — any wiki page that refers to "Business Actualization" as the current company name needs updating. `ba-overview.md` is updated; other pages (e.g., `conley-potter.md`, `career-history.md`) may still use the old name.
- The "AutoBoost as SaaS" framing was a persistent misunderstanding in earlier wiki entries. The distinction matters for how Conley positions BA relative to competitors like Kukui when talking to clients or investors.
- At $2.5M ARR with 13 staff, AutoBoost is solidly mid-market for a vertical-specialized agency. Commission structure and Director compensation make more sense in this context.

---

## [2026-04-18] update | ba-products.md — full rate card and service detail confirmed

**Pages updated:** 1 (`ba-products.md`)

### What changed

Conley provided the full official rate card and resolved all outstanding TODOs on this page. The page has been rewritten from an inferred/approximate state to confirmed documentation.

- **Full pricing table added:** 20 line items with monthly and onboarding fees. All services are à la carte. The only bundled discount is the Advanced Website 20%-off structure.
- **Standard Website scope confirmed:** Pre-optimized layouts, brand customization, on-page SEO + listing directory management, performance dashboard, managed SEO transition, fast content edits. CMS platform not explicitly stated in client materials (likely Duda).
- **Jumpstart vs. Jumpstart+ clarified:** Key differentiator is single vs. multiple targeting categories, both Performance Max-style entry-level. Jumpstart targets shops under $300/month ad spend; Jumpstart+ under $500/month. Jumpstart+ formerly called "Local Plus+."
- **LSA Standard vs. Advanced confirmed:** Standard = verified listing + lead management + basic optimization. Advanced adds active lead rating, call recording review, and call notes to train Google's LSA algorithm.
- **Programmatic DSP identified:** Simpli.fi. Not disclosed externally. Three tiers: Display / Display+Audio / Display+Audio+Video.
- **Gauge clarified:** Internal name only. White-labeled foundation with heavy BA-proprietary layers. Client-facing term: "Revenue Attribution Platform."
- **Email marketing confirmed dormant:** On the rate card at $249/month; not actively sold in ~9 months.
- **All TODO blocks removed.** Page is now authoritative documentation, not inferred reconstruction.

### Notable observations

- The Advanced Website 20% discount is a meaningful strategic lever — it creates a natural anchor to upsell the full service stack. A client on Advanced Website ($1,499/mo) getting 20% off Google Ads Advanced ($999/mo) saves $200/month, essentially subsidizing the website upgrade.
- The Simpli.fi non-disclosure is consistent with BA's broader white-label approach (Birdeye, CallRail). BA presents a unified platform to clients rather than a patchwork of third-party vendors.
- Email marketing being dormant for 9 months suggests the service exists defensively (to match competitor menus) rather than as an active revenue driver.
- Deal amounts in HubSpot (e.g., Turbo Tim's at $31,348) don't map cleanly to monthly rate × 12, suggesting multi-year pre-payments or multi-location contracts are common at the top of the client base.

---

## [2026-04-18] ingest | Daily Recap — April 17, 2026

**Source type:** BA workday log — full FLACA conference day in Orlando; zero outbound emails; one recurring client call; all active work handled by Palmyra team
**Pages created:** 1 (`daily-recap-2026-04-17.md`)
**Pages updated:** 3 (`ba-clients-pipeline.md`, `ba-partners.md`, `index.md`)

### What this source contains

A full-day conference log for Friday, April 17 — Day 2 of FLACA (Florida Automotive Community Association) at Wyndham Lake Buena Vista / Disney Springs. Conley attended conference sessions and the expo (5–7 PM solo). The only Conley-owned call was Best One Fleet Google Ads review (~15 min from the hotel). Zero emails sent. The Palmyra team (Jon, Ethan, Courtney) handled all client-facing work.

Notable inbound activity despite Conley's absence:
- **Telle Tire** — Marco Gonzalez (suspected PE firm Partner) booked a Mon 4/21 meeting via HubSpot. Conley flagged to Jon the PE angle; high deal-size potential.
- **Turnkey multi-shop lead** — Suzanne Berger confirmed the Wed 4/22 3:30 PM ET meeting — the "huge stinking deal" from Jared Baker's Apr 15 referral is now a live appointment.
- **Virginia Auto Service** — Matt + accounting contact accepted meeting; Adam took inbound call (~12 min).
- **John McCormick** — Urgent SMS text blast request; Jon/Ethan planned weekend draft for Monday launch (480-person Shopware list).
- **Brenner Newman** — Courtney escalated an SEO strategy gap to Conley; she "doesn't know ranking strategy" and is usually the implementer.
- **9 open items** carrying forward into the coming week.

### What changed

- `daily-recap-2026-04-17.md` — New archival page. Full recap covering conference context, Best One Fleet solo call, 3 pipeline advances (Telle Tire, Turnkey, Virginia Auto Service), 3 urgent client threads handled by the team (McCormick, Newman SEO, TAS/Sonny Letak), and a "What This Reveals" synthesis section with 5 observations.
- `ba-clients-pipeline.md` — 9 updates total:
  - **Added:** Telle Tire (High-Priority, PE contact suspected, Mon 4/21 meeting)
  - **Added:** Virginia Auto Service / Import Car Specialists (Active Clients, inbound, two decision-makers engaged)
  - **Added:** John McCormick (Active Clients, urgent SMS blast request, 480-person list)
  - **Added:** Stan's Auto Service (Active Clients, programmatic proposal outstanding, Sheldon)
  - **Added:** TAS / Sonny Letak (Active Clients, Tesla + A/C content + LSA issue)
  - **Updated:** Turnkey multi-shop lead — renamed to reflect Suzanne Berger; meeting now confirmed Wed 4/22
  - **Updated:** Sav-Mor / Brenner Newman — added Courtney's SEO gap escalation
  - **Updated:** Best One Fleet — added outstanding recording task note
  - **Updated:** A&R Complete Auto — Angie availability and pending reschedule noted
- `ba-partners.md` — Suzanne Berger entry expanded: confirmed meeting acceptance for the multi-shop Advanced LSA prospect; turnaround from referral to confirmed call documented as 7 days.

### Notable observations

- Telle Tire's PE angle is the highest-value signal from this day. If Marco Gonzalez is from the PE firm that owns the chain, the deal scope is likely multi-location and high-ticket. Worth doing pre-call research on Telle Tire's ownership structure before 4/21.
- The Turnkey-to-confirmed-meeting turnaround (Apr 15 referral email → Apr 22 call confirmed) is 7 days. The prior Turnkey lead in the pipeline (still unnamed prospect, Advanced LSA) represents exactly the high-intent referral pattern the [[ba-partners]] page describes. If this closes, it validates the Turnkey channel as a consistently high-velocity source.
- Courtney's SEO gap is potentially more significant than a single client issue. If SEO ranking strategy lives only with Conley and isn't distributed to the content team, that's a bottleneck — especially as client load grows. The Director title alignment case includes service delivery standards ownership; this kind of gap is exactly what that authority would let Conley address structurally.
- The team's independent handling of McCormick (SMS urgency), Letak (Tesla content + LSA ticket), and Newman (SEO escalation) while Conley was at conference is operational evidence of a functioning delegation structure. No client issues escalated to Conley from the hotel; all were either handled or queued appropriately.

---

## [2026-04-21] ingest | The disposable drone opportunity — Drone Enterprises founding research

**Source type:** Comprehensive founder's playbook — infantry-scale UAS market analysis, April 2026. Authored as a briefing document synthesizing current doctrine, adversary capabilities, supply-chain gaps, company-build strategy, funding pathways, and GTM sequencing. Accompanied by Conley's Q&A/glossary notes on the document.  
**Pages created:** 6 (`domain-drone-enterprises.md`, `drone-enterprises.md`, `drone-market-analysis.md`, `drone-build-strategy.md`, `drone-funding-gtm.md`, `sam-schutt.md`)  
**Pages updated:** 3 (`conley-potter.md`, `index.md`, `CLAUDE.md`)

### What this source contains

A 7-section playbook covering the US military drone industrial gap, adversary capabilities (China/Russia/Iran), supply chain dependencies on Chinese components, the market opportunity for a $500–$2,000 NDAA-compliant Group 1 UAS at 100K+/year volumes, company-build architecture, funding strategy (SBIR/STTR, OTA, defense VC), and a 0–5 year GTM roadmap modeled on Anduril's trajectory. Key data points: Army Secretary Driscoll's 1M-drone-over-3-years target; $1B DDP RFI for 300K units; Skydio X10D at $17,300/unit (March 2026 Army order); Neros Archer ramping toward 10K/month; no US-made $500–$1,500 NDAA-compliant OWA/FPV drone exists at scale. The companion Q&A notes reveal Conley is new to defense-tech vocabulary — wiki pages were written to define key terms (Shahed-class, EW, NDAA compliance, OWA, attritable) in context.

This source establishes a **new domain**: Drone Enterprises. Conley is co-founding with Sam Schutt (closest friend, best man at June 12, 2026 wedding) as Chief Strategy Officer.

### What changed

- `domain-drone-enterprises.md` (new) — Domain anchor page. Founding context, active pages list, status.
- `drone-enterprises.md` (new) — Company overview. Thesis, founding team, product vision, competitive landscape, revenue model, status and immediate next steps.
- `drone-market-analysis.md` (new) — Full market analysis. Doctrine shift, five-war case studies, Replicator/DDP context, China/Russia/Iran adversary capabilities, NDAA supply chain gaps with reference compliant-supplier table, TAM math ($450M–$1.25B/year), price benchmark table. Includes plain-language explainers for EW (electronic warfare), Shahed-class drones, and the NDAA compliance gap — added because Conley's Q&A notes flagged these as unfamiliar terms.
- `drone-build-strategy.md` (new) — Hardware and manufacturing strategy. Architecture decision (Neros-style vertically integrated + Auterion software layer), design non-negotiables (modularity, EW resilience, MOSA, open APIs), full NDAA-compliant BOM with sourcing options, manufacturing hub-and-spoke model, volume unit economics, IP/defensibility analysis, team composition by funding stage.
- `drone-funding-gtm.md` (new) — Funding and GTM. Defense VC landscape with check-size benchmarks, SBIR ladder (Phase I → Phase III sole-source), OTA mechanics, DIU/Blue UAS on-ramp, target customers by procurement speed, programs of record, allied sales channels, strategic acquirers, full 0–5 year GTM roadmap with raise targets and unit volume milestones.
- `sam-schutt.md` (new) — Stub profile for Sam Schutt. Personal relationship (best man, closest friend), co-founder role, open questions about his professional background.
- `conley-potter.md` — Added Drone Enterprises entry under Active Projects. Updated Related links. Updated frontmatter date.
- `index.md` — Added Drone Enterprises section (6 pages). Source count 27 → 29. Page count 49 → 55. Two new source file rows.
- `CLAUDE.md` — Added Drone Enterprises to Active Domains list.

### Notable observations

- This is a genuinely new domain — no defense-tech or hardware-startup context existed in the wiki before this ingest. The pages are built from a single comprehensive source; they will need updating as Conley and Sam develop the company and new sources arrive.
- Conley's Q&A notes reveal he is entering this space as a domain outsider. His strengths (strategy, systems architecture, commercial GTM, public narrative) map well to the CSO role, but the wiki should flag when pages assume defense-domain fluency he doesn't yet have. Plain-language definitions in market-analysis pages are intentional.
- **Sam Schutt's professional background is completely undocumented.** The `sam-schutt.md` stub is essentially empty. The founding team archetype analysis in `drone-enterprises.md` flags that Drone Enterprises needs three archetypes represented — it's unclear from available sources whether Sam fills the technical or operator archetype, or if a third recruit is needed.
- The structural gap that Drone Enterprises is targeting (no US-made $500–$1,500 NDAA-compliant OWA at 100K+/month) is real and validated by multiple independent data sources in the research document. Neros is the closest competitor but they are still ramping and their pricing appears to be above target. The window is open now.
- This is the first "hardware startup co-founding" domain in the wiki, which puts it in an interesting relationship with ACE. ACE is 15 hr/week maximum; Drone Enterprises is a full company-build. The [[operating-doctrine-2026]] decision filter ("say yes only if it strengthens BA or ACE, increases calm/leverage/clarity, or compounds attention") should be revisited — Drone Enterprises doesn't fit that filter as written. Worth flagging to Conley.
- `Wiki Base.base` in raw-sources is a byte-for-byte duplicate of the compass_artifact markdown file. Not logged as a separate source.
- Stan's programmatic proposal has now appeared in recaps for three consecutive days (Apr 15, 17, and presumably will show up on 4/18). This is a pattern of deferrals, not priorities. May be worth a dedicated Monday task before the Telle Tire and Turnkey meetings dominate the week.
