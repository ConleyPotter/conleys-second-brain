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

## [2026-04-16] ingest | conley-weekly-summary-apr-6-12-2026.md + BA domain build-out

**Source type:** BA weekly work summary — Google Calendar, Gmail, HubSpot, Slack  
**Pages created:** 7 (`ba-overview.md`, `ba-products.md`, `ba-partners.md`, `ba-team.md`, `ba-clients-pipeline.md`, `adam-shop-incubator.md`, `weekly-recap-2026-04-06.md`)  
**Pages updated:** 3 (`index.md`, `CLAUDE.md`, `log.md`)

### What this source contains

A structured weekly summary of Conley's BA workday activity for the week of April 6–12, 2026. ~20 client meetings, 3 deals closed-won (~$29,610 attributed), 3 new HubSpot deals created (CarLink360 $19,884, Tilson's LSA deal, Legacy Auto Care $5,985), and two onboardings advanced signed → paid. Adam and Jon traveled to TEKTONIC Conference Thu–Fri; Conley covered solo. Notable events: auto shop incubator GC referral placed (Jim Walton), POS-based conversion tracking initiative in #internal-google-ads, filming session with Kyle.

### What changed

- **`ba-overview.md`** (new) — Foundation page for the BA day job domain. Covers what BA is, Conley's role, the two-pillar relationship to the 2026 Operating Doctrine, services overview, tooling, partner ecosystem, and revenue/scale signals. Extensive TODOs for BA revenue figures, AutoBoost product description, and flatarchy org proposal status.
- **`ba-products.md`** (new) — Full BA service catalog built by inference from deal records and sales conversations. Documents website tiers, Google Ads tiers (Jumpstart / Jumpstart+ / Standard / Advanced / Performance Max), LSA tiers (Standard / Advanced), programmatic, review platform, call tracking, social content curation, attribution (Gauge), video, email. Pricing partially filled from observed deal amounts. TODOs for official rate card and the Standard vs. Advanced LSA breakdown Conley sent Jared Baker.
- **`ba-partners.md`** (new) — Turnkey Auto Marketing (Jared Baker, Suzanne Berger) and AutoVitals (Carly Lama, Carlos Massaquoi, Shelby Maggard, Steve, Adam Hicks, Jordan) documented in full. Commercial structure of both partnerships flagged as a TODO.
- **`ba-team.md`** (new) — All internal team members documented with roles inferred from behavioral observation. Formal titles flagged for verification. AI prompts included for Slack-connected agents to pull roster and role data.
- **`ba-clients-pipeline.md`** (new) — Rolling reference for key accounts and pipeline. Seeded from two sources. Organized by: High-Priority Accounts, Active Clients, AutoVitals Co-Managed Accounts, Recently Closed/Onboarding, Pipeline Watch List, Accounts Needing Attention.
- **`adam-shop-incubator.md`** (new) — Documents Adam's 6-location auto repair shop chain initiative. GC referral (Jim Walton) placed Apr 7; walkthrough completed; bid pending. Notes strategic connection to BA marketing incubator thesis and possible future ACE Phase III relevance.
- **`weekly-recap-2026-04-06.md`** (new, archival) — Full structured wiki summary of the Apr 6–12 week. Executive summary, notable events, full meeting list by day, HubSpot deal activity, email/follow-up work, Slack threads driven, wins/themes.
- **`CLAUDE.md`** (updated) — Added `work-log` page type, `domain:` frontmatter field, rolling vs. archival distinction, recurring log source ingest pattern, expanded active domains (ACE / BA / Personal), updated index section list, updated Known Pages Needing Attention with four new items.
- **`index.md`** (updated) — New "Day Job (BA)" section added with 6 entries. "Operations & Tech" renamed to "ACE Operations & Tech". Day Job Logs section updated with weekly recap entry. Source count 13→14, page count 28→37.

### Notable observations

- The BA day job is now the highest-volume raw source type — daily and weekly recaps will arrive continuously. The `work-log` archival pattern established here is the repeatable framework for all future recaps.
- `ba-products.md` is the most speculative page in the wiki — built entirely by inference. It should be the first page to validate against official BA documentation.
- The AutoVitals partnership is structurally deeper than it initially appeared. Multiple named contacts, joint call cadence, and shared client base suggest it's not a simple referral relationship — it may be closer to a co-delivery arrangement.
- The POS-based conversion tracking initiative (Gauge/Pilot + GCLID capture) is a differentiation play worth watching — if it ships, it becomes a meaningful selling point for Advanced-tier clients.
- `ba-clients-pipeline.md` deliberately does not replicate HubSpot data. It holds relational context and strategic notes. This distinction should be maintained — resist the temptation to make it a deal tracker.

---

## [2026-04-16] query | Second brain article — first portfolio writing piece

**What was asked:** Write a substantive essay documenting the creation, development, and use of this second brain system for Conley's personal portfolio website. Cover the architecture (Claude Code + markdown + Obsidian), the team adaptation angle (Git/GitHub + schema changes), and credit Andrej Karpathy (CLAUDE.md inspiration) and Ray C Fu (Obsidian + Claude Code setup and initial prompts). Write to /wiki/, update index.md, update connected concept pages, log to log.md.

**Pages read:** All wiki pages (via Explore agent) + CLAUDE.md + index.md + log.md + portfolio-website.md + building-out-loud.md

**Pages created:** 1 (`second-brain-article.md`)
**Pages updated:** 3 (`index.md`, `portfolio-website.md`, `building-out-loud.md`)

### What this produces

- **`second-brain-article.md`** (new, type: `asset`, domain: `personal`) — Full portfolio essay, ~1,000 words, written in Conley's brand voice ("calm ambition"). Covers the three-layer architecture (raw sources / wiki / schema), the init story (April 14, 2026), what makes the system work (log as continuity, index as orientation, ingestion as compounding), the team adaptation pattern (shared CLAUDE.md + Git/GitHub), and an honest reflection on where it goes from here. Credits Karpathy and Ray C Fu in the closing line.

### What changed

- **`index.md`** — Page count 37 → 38. `[[second-brain-article]]` added to Meta section with one-line description.
- **`portfolio-website.md`** — Writing section updated to note that `[[second-brain-article]]` is a complete, portfolio-ready draft — the first substantive published piece available for the Writing section.
- **`building-out-loud.md`** — Added `[[second-brain-article]]` to Relationship to Other Concepts. The essay ends with the exact *Building Out Loud* stance ("I'm building this. You're welcome to watch.") — it's a natural written companion piece or episode source.

### Notable observations

- The article ends deliberately open — "I don't know yet" — which is consistent with [[brand-voice]] honesty and avoids the temptation to package uncertainty as a lesson. This is the right call for a first piece.
- The team adaptation section is intentionally brief. It names the pattern without overexplaining it. The audience for a portfolio piece doesn't need the implementation details; they need to understand that the model generalizes.
- "I'm building this. You're welcome to watch." appears both as the final sentence of the article and as the *Building Out Loud* positioning statement. That's not coincidence — this piece is the first concrete expression of that public stance in writing.
- The article credits Karpathy by name and Fu by name. Both attributions are appropriate and make the piece feel grounded rather than self-congratulatory.
