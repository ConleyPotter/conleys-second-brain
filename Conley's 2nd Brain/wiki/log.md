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
## [2026-04-24] update | JARVIS content production system built and integrated

**Operation:** Hybrid integration — JARVIS content production layer added to the second brain vault
**Pages created:** 1 (`jarvis-system.md`)
**Pages updated:** 1 (`index.md` — page count + new entry)
**Structural changes:** 10 new directories, 4 skill files, 4 slash commands, root CLAUDE.md updated

### What this source contains

Not a source ingest — a system build. The JARVIS content production layer (inbox → captures → connections → briefs → published pipeline) was scaffolded directly inside `Conley's 2nd Brain/` alongside the existing wiki and raw-sources. The full folder structure, operating contract (`05-CLAUDE/CLAUDE.md`), four skill files, and four slash commands are now in place on branch `claude/hybrid-jarvis-integration`.

### What changed

- `05-CLAUDE/CLAUDE.md` — New file. Full JARVIS operating contract: identity context, audience definition, voice rules, hard rules (banned phrases, BA/ACE persona separation), deep personal context (BA team, ACE stack, Sentinel, River Room, 2026 doctrine).
- `05-CLAUDE/skills/process-inbox.md` — New file. Inbox processing skill: sharpen each note to one specific sentence, assign exactly 3 tags, route to correct 01-CAPTURES subfolder, report with patterns and one connection.
- `05-CLAUDE/skills/weekly-connections.md` — New file. Connection-finding skill: read all captures from last 7 days, find 3–5 Type A/B/C/D non-obvious connections, create connection notes in 02-CONNECTIONS.
- `05-CLAUDE/skills/generate-brief.md` — New file. Brief generation skill: five-field format (ONE THING, PROOF, READER TRANSFORMATION, THREE HOOKS, THREE CLOSERS); save to 03-BRIEFS tagged #ready-to-write.
- `05-CLAUDE/skills/write-content.md` — New file. Content writing skill: read brief + sources, apply voice rules, structure hook→proof→body→closer, self-check, save draft tagged #written.
- `.claude/commands/jarvis-process-inbox.md` — New slash command. Reads 05-CLAUDE/CLAUDE.md, executes process-inbox skill.
- `.claude/commands/jarvis-connections.md` — New slash command. Reads 05-CLAUDE/CLAUDE.md, executes weekly-connections skill.
- `.claude/commands/jarvis-brief.md` — New slash command. Reads 05-CLAUDE/CLAUDE.md, executes generate-brief skill.
- `.claude/commands/jarvis-write.md` — New slash command. Reads 05-CLAUDE/CLAUDE.md, executes write-content skill.
- `CLAUDE.md` (root) — Two changes: (1) directory diagram expanded to show both wiki and JARVIS layers; (2) new section 6 "Content production workflows (JARVIS)" added after the Lint workflow, cross-linking both systems.
- `jarvis-system.md` — New wiki page documenting the system: folder structure, slash commands, pipeline, connection types, and wiki integration rules.
- `index.md` — Page count updated from 49 → 50; `jarvis-system.md` added to Meta section; date updated to 2026-04-24.
- `00-INBOX/` through `05-CLAUDE/skills/` — 10 new directories scaffolded with `.gitkeep` files.

### Notable observations

- The single-vault architecture (JARVIS inside `Conley's 2nd Brain/` alongside wiki) means captures and briefs can natively link to wiki pages using `[[wiki-link]]` syntax. This is the core advantage over a two-repo approach — no sync, no broken links.
- The JARVIS system explicitly separates knowledge accumulation (wiki, slow, permanent) from content production (JARVIS, daily, perishable-input → permanent-output). The distinction matters operationally: one compounds, one produces.
- The voice rules in `05-CLAUDE/CLAUDE.md` and `[[brand-voice]]` cover the same ground. `05-CLAUDE/CLAUDE.md` is the truth source for content production; `[[brand-voice]]` is the wiki-page format. If they diverge, `05-CLAUDE/CLAUDE.md` wins.
- A manual step is required before zero-friction capture works: install **QuickAdd** from Obsidian Community Plugins (Settings → Community Plugins → Browse → "QuickAdd"). One keyboard shortcut drops a note into `00-INBOX/`. Cannot be automated from Claude Code.
- The JARVIS folder structure (`00-INBOX` through `05-CLAUDE`) is now visible in Obsidian's left sidebar alongside `wiki/` and `raw-sources/`. Obsidian cross-links between captures and wiki pages are ready to use.
- Stan's programmatic proposal has now appeared in recaps for three consecutive days (Apr 15, 17, and presumably will show up on 4/18). This is a pattern of deferrals, not priorities. May be worth a dedicated Monday task before the Telle Tire and Turnkey meetings dominate the week.

---

## [2026-04-24] ingest | JARVIS System Guide + Drone Opportunity Research

**Source type:** Two external resources (JARVIS setup guide + defense market research brief) + one set of working notes  
**Pages created:** 2 (`jarvis-system.md`, `drone-opportunity.md`)  
**Pages updated:** 2 (`index.md`, `log.md`)  
**Files produced outside wiki:** `JARVIS-CLAUDE.md` (saved at vault root — Conley-specific JARVIS CLAUDE.md, ready to drop into new JARVIS vault)

### What these sources contain

**How to Build a JARVIS Inside Obsidian With Claude Code (cyrilXBT, April 23, 2026) + New JARVIS Repo CLAUDE.md File.md** — A complete guide and template for building a JARVIS content production system: Obsidian vault with a specific folder architecture (00-INBOX / 01-CAPTURES / 02-CONNECTIONS / 03-BRIEFS / 04-PUBLISHED / 05-CLAUDE), four core skills (Process Inbox, Weekly Connections, Generate Brief, Write Content), a daily 20-minute ritual, and a performance feedback loop. The template CLAUDE.md is a skeleton requiring operator-specific fill-in. Distinct from the existing second brain wiki: the wiki accumulates knowledge; JARVIS produces content.

**compass_artifact... (Disposable Drone Research Document, April 2026)** — A comprehensive (~15,000 word) strategic brief on founding a disposable infantry UAS company in the current US defense market. Covers: doctrine shift post-Ukraine, US supply chain gaps (Group 1 FPV/OWA production 10–20× below Hegseth targets), adversary benchmarking (China/Russia/Iran cost comparisons), full market opportunity analysis, company build strategy, funding landscape ($500K pre-seed to $4B+ Series C benchmarks), and 5-year GTM roadmap. Key data: $450M–$1.25B/year TAM, $800–$1,800 ASP target for NDAA-compliant FPV-class drones, comparable companies (Neros, PDW, Skydio, Anduril).

**Questions & Notes on the Disposable Drone Research Document** — Conley's active working notes on the above. Most significant: a direct message to a collaborator named "Sam" — "I think that the plans you sent me only included an ISR variant. Will our first model offer OWA & decoy nose-cap variants?" This confirms active co-founder-level exploration, not passive research interest. Sam has apparently shared design plans. Also includes a glossary of new defense terms (sUAS, OWA, ISR, BOM, NDAA, TAM), and conceptual questions about electronic warfare, terminal guidance, and defense pricing models.

### What changed

- **`jarvis-system.md`** (new) — Synthesis page documenting what JARVIS is, how its architecture differs from the existing second brain, the four core skills, the daily ritual, the performance compounding loop, and the planned integration path between the two systems. Includes a comparison table distinguishing the wiki (knowledge accumulation) from JARVIS (content production).

- **`drone-opportunity.md`** (new) — Project page documenting the founding thesis, market context, Conley's active collaboration with "Sam," the proposed product architecture (ISR + OWA + decoy nosecap variants sharing a common airframe), NDAA-compliant reference BOM, funding landscape, and the critical 5-question diagnostic about the Sam collaboration. Includes an explicit flag: this project is outside the 2026 operating doctrine's "consolidate on ACE and BA" mandate and requires a formal go/no-go decision before further time investment.

- **`JARVIS-CLAUDE.md`** (new, vault root) — The JARVIS CLAUDE.md written specifically for Conley. Not a template — fully filled in with: complete identity section (what he does, who he's building it for, three content pillars); deep ACE context (phase I lead enrichment, tech stack, 3-phase roadmap, The Proactive Ghost, covert client rules); BA context (team roster, partner ecosystem, identity separation rules); The Sentinel and River Room; personal context (Marietta PA, UW-Madison English Lit + Chinese, App Academy, restaurant background, fibromyalgia, June 12 wedding, AT hiking, Mandarin fluency); 2026 operating doctrine; exact voice rules with word-choice specifics and failure modes; full hard rules (forbidden phrases, persona separation rules); and five detailed primary job definitions. Ready to drop into `05-CLAUDE/CLAUDE.md` in the new JARVIS vault.

- **`index.md`** — Source count 27→31, page count 49→51. Two new rows added to General Knowledge section. Four new source rows added.

### Notable observations

- The drone opportunity is the most unexpected revelation in this source batch. Conley is not passively reading a research document — he has a collaborator named "Sam" who has already sent design plans. This is a co-founder-stage conversation happening outside the documented wiki. Given the 2026 doctrine's explicit "consolidate" mandate, this is a significant tension worth surfacing directly.
- JARVIS and the existing second brain are architecturally complementary, not redundant. The existing wiki is the context source; JARVIS is the output engine. The second-brain-mcp-server synthesis already identified the integration path: the wiki as MCP server feeding JARVIS connection sessions. If both systems are running simultaneously, they complete a full loop: real-world input → wiki knowledge → JARVIS connections → published signal → feedback data → wiki updated.
- The JARVIS CLAUDE.md written today is the richest single-file context document about Conley that exists in this system. It synthesizes everything ingested since April 14 into one operator file. This document will be read at the start of every JARVIS session — it is the highest-leverage writing produced in this wiki so far.
- Sam's design plans (ISR variant, with Conley asking about OWA + decoy nosecap) suggest the collaboration is past ideation and into early product design. The fact that Conley is asking a clarifying question rather than responding to an open-ended brainstorm suggests Sam is the technical/hardware lead and Conley is playing the commercial/strategic role — exactly the founding team composition the research document says a drone startup needs.

---

## [2026-04-26] update | Portfolio fully updated — all known issues resolved

**Pages updated:** 2 (`portfolio-website.md`, `CLAUDE.md`)
**Inbox notes affected:** 1 deleted by Conley (`obs-portfolio-describes-dead-system`)

### What happened

Conley completed a full portfolio update over the weekend of April 25–26, 2026. All previously tracked issues are resolved. The wiki was updated to reflect this.

### What changed

- **`portfolio-website.md`** — Major restructure:
  - Overview rewritten to reflect site is now current and accurate
  - "ACE Description Problem" section archived with ✅ resolved status (no longer an active issue)
  - Projects Page description updated: all three projects (ACE, The Sentinel, TLE) reflect post-update copy
  - "What Needs Updating" section replaced with "Open Items (Post-Update)" — only two remaining items: blog post stubs (unconfirmed) and wiki sync (ingest a new site snapshot)
  - Strategic Notes updated: site is now "launch-ready from a content accuracy standpoint"
  - Frontmatter `updated` date: 2026-04-18 → 2026-04-26
- **`CLAUDE.md` (root)** — Known pages needing attention:
  - Removed: `[[portfolio-website]]` ACE description / About page fix (resolved)
  - Removed: `[[the-sentinel]]` portfolio status discrepancy (resolved — site now accurate)
  - Added: low-priority note that wiki's "What the Site Currently Says" section is pre-update state pending a new snapshot ingest

### Notable observations

- The portfolio update closes the longest-standing accuracy gap in the wiki — ACE's public description had been describing a sunsetted system since February 2026. The site is now aligned with the operating reality.
- The one remaining structural gap: the wiki's "What the Site Currently Says" section documents the April 14 state. A new raw-source screenshot/capture would let that section accurately reflect the current copy. Low urgency but worth doing before the next portfolio-linked wiki query.

---

## [2026-05-06] update | Major vault overhaul — ACE/TLE pivoted to Personal Brand Engine

**Pages created:** 4 (`personal-brand-engine.md`, `content-strategy.md`, `portfolio-projects.md`, `github-strategy.md`)  
**Pages rewritten:** 5 (`ace-overview.md`, `thought-leader-engine.md`, `campaign-plan.md`, `building-out-loud.md`, `operating-doctrine-2026.md`)  
**Pages archived:** 7 (`phase-1-lead-enrichment.md`, `phase-2-content-vectors.md`, `phase-3-infrastructure.md`, `financial-projections.md`, `client-acquisition.md`, `upwork-portfolio.md`, `platform-comparison.md`)  
**Pages updated:** 3 (`index.md` — page count 52→56, section restructure; `CLAUDE.md` — description and active domains; `log.md`)

### What this source contains

A major strategic pivot triggered by Conley's honest assessment: the ACE freelance arbitrage business plans were never executed due to time constraints (BA workload + wedding preparation), and likely won't be in the foreseeable future. The more strategic use of the same AI infrastructure is to build public presence and career capital — the Personal Brand Engine. ACE (Autonomous Content Engine) and the Thought Leader Engine (TLE) have been merged into the PBE, with the commercial framing of both archived.

Conley's stated goals for the PBE: build awesome portfolio projects, contribute to open source, publish heavily on GitHub/X/Substack/portfolio blog, become a known presence in the AI/MarTech space, and use the systems to amplify output beyond what's possible manually. The career transition is the primary objective; the PBE is the primary mechanism.

### What changed

- **`personal-brand-engine.md` (created)** — The primary reference page for the merged system. Covers the three pillars (Content, Code, Community), full input/output architecture, the Upwork pipeline as Portfolio Project #1, the ACE+TLE merger story, 12-month success metrics, and relationship to the career transition.
- **`content-strategy.md` (created)** — Channel-by-channel publishing guide replacing [[campaign-plan]]. Covers LinkedIn, X, Substack, portfolio blog, audio/speaking, and GitHub. Includes the LinkedIn audience separation update (strict ACE/LinkedIn separation is retired — MarTech/AI content belongs on LinkedIn now). Weekly rhythm target (~5–7 hrs/week).
- **`portfolio-projects.md` (created)** — Five open source projects with specs, build order, and content output for each: Upwork AI Job Scout (packaging existing workflow), n8n×HubSpot template library, AI campaign performance analyzer, MarTech audit tool (flagship), and external OSS contributions.
- **`github-strategy.md` (created)** — GitHub profile setup, activity cadence, repo standards, OSS contribution strategy, and the GitHub→content pipeline (each shipped project triggers specific content across all channels).
- **`ace-overview.md` (rewritten)** — Restructured around the three-pivot history. Removed all commercial framing (Phase I–III, The Proactive Ghost). Now describes what survived the pivot (Upwork pipeline, tech infrastructure, brand voice work) and what was archived. Current stack accurately documented.
- **`thought-leader-engine.md` (rewritten)** — Lead section replaced with personal TLE architecture (Conley's own content automation, not client ghostwriting). Original Proactive Ghost commercial product documentation preserved in an "Archived" section for reference.
- **`campaign-plan.md` (archived)** — Added archive notice; points to [[content-strategy]] as replacement.
- **`building-out-loud.md` (rewritten)** — Updated from "solo podcast, audio-first, source of truth" to "audio/speaking channel, format TBD, on par with written content." Added format evaluation table (guest appearances, LinkedIn Audio, solo, interview, short-form video). Recommended starting approach: guest appearances first.
- **`operating-doctrine-2026.md` (updated)** — Updated "Singular Owned Asset" section from ACE to PBE. Updated "Public Output" from audio-first/everything-is-derivative to multi-channel with TLE enabling consistent output within bandwidth constraints.
- **7 pages archived** — All with archive notice + pointer to PBE.
- **`index.md` (restructured)** — Renamed "ACE Operations & Tech" to "Personal Brand Engine & Tech." Added 4 new pages. Updated summaries for rewritten pages. Marked archived pages with ⚠. Updated header.
- **`CLAUDE.md` (updated)** — Updated "What this is" description. Updated active domains (ACE → PBE as primary domain). Cleared resolved tech-stack item. Added portfolio-update-plan as needing review.

### Notable observations

- The honest through-line of this pivot: the elaborate plans (Phase I–III, Proactive Ghost, "First Contract" campaign) were architecturally sound but required execution time that never materialized. The PBE is a more realistic use of the actual available bandwidth (5–10 hrs/week, inconsistent, often low). This is worth flagging explicitly in future sessions — don't build plans that require consistent blocks of side-hustle time.
- The Upwork job discovery pipeline is one of the more impressive things in the portfolio already, and it's been invisible. Open-sourcing and writing about it is low effort and high signal.
- The LinkedIn audience separation protocol (strict ACE/LinkedIn firewall) being retired is a meaningful change. LinkedIn now needs to be treated as a primary career channel, not a separate identity silo.
- The audio/speaking format question is genuinely open and worth revisiting when there's bandwidth to experiment. Guest podcast appearances are the right low-risk starting point.
- Seven pages now have `status: archived` in frontmatter. A future lint pass should verify that no active pages are still linking to archived pages without context.

---

## [2026-05-06] update | Career strategy refined; ACE build status corrected; LinkedIn title updated

**Pages updated:** 5 (`career-transition-strategy.md`, `resume-cs-ai-leadership-2026.md`, `tech-stack.md`, `ace-overview.md`, `conley-potter.md`)

### What changed

- **`career-transition-strategy.md`** — Added new "Role Fit: Marketing Technology & AI Over Client Success" section. Revised primary role targets from CS-forward to MarTech/AI-forward (RevOps Director, MarTech Director at enterprise, AI GTM Lead, MarOps at AI-native company, Solutions Consultant). Added detailed comp analysis and reasoning for each. Added honest Anthropic/OpenAI $200–300K path analysis (2–3 year arc, not direct jump). Updated Months 1–3 step 1 LinkedIn positioning to "MarTech and AI implementation leader." Updated step 3 resume note to reflect MarTech framing. Added fifth open question on aligning role choice to eventual venture.
- **`resume-cs-ai-leadership-2026.md`** — Fixed three inaccuracies: (1) target roles header updated to MarTech/AI framing; (2) summary rewritten to lead with MarTech + AI implementation rather than CS leadership; (3) AI Systems section corrected — removed false Apollo + Cleanlist claim, replaced with accurate description of the deployed Upwork job discovery pipeline (Apify → score → proposal draft → n8n architecture doc → Slack delivery).
- **`tech-stack.md`** — Added deployment status warning to Overview. Added new "Deployed Workflows" section documenting the Upwork job discovery pipeline end-to-end. Added "not yet deployed" callout to Data Enrichment section (Apollo, Cleanlist, Supabase). Updated OPEX table to distinguish planned vs. active costs; noted actual current spend is ~$97/month.
- **`ace-overview.md`** — Added build status callout to Phase I section: enrichment pipeline not yet built; only deployed workflow is the Upwork job discovery pipeline.
- **`conley-potter.md`** — Updated role/title section to reflect three concurrent external titles now in use: LinkedIn (Director of Digital Marketing, updated May 2026), resume/job search (Director of Client Success & Strategy), and portfolio website (Client Success & Growth Leader). Noted that Adam and Micah confirmed public title flexibility.

### Notable observations

- The Apollo/Cleanlist overclaim was present in the resume and implicitly in tech-stack.md since initial wiki creation — the business plan described it as the Phase I stack, but it was never flagged as unbuilt. This kind of gap (plan vs. reality) is worth auditing across ACE pages; other planned tools may be documented as if deployed.
- The role pivot from CS to MarTech/AI is more than positioning — it changes which companies to prioritize and which proof points to lead with. The Upwork pipeline is the right anchor story for the resume, not a generic "data enrichment waterfall."
- LinkedIn title "Director of Digital Marketing" is a reasonable public-facing framing that's accurate to what he actually does at BA, marketable for the job search, and doesn't overclaim on the CS side.

---

## [2026-05-03] query | Career transition strategy — new role, positioning, and job search plan

**What was asked:** How Conley could use ACE and the Thought Leader Engine to position himself for a high-compensation corporate role in the next 6–12 months; what role would be the best fit; how to maximize earnings at a world-class company; what companies to target in Philadelphia or remote.

**How it was answered:** Full synthesis across [[conley-potter]], [[career-history]], [[resume-variants]], [[operating-doctrine-2026]], [[thought-leader-engine]], [[ace-overview]], and a live web search on B2B SaaS market disruption in 2025–2026. Three direct questions answered inline: security clearance eligibility, SaaS market conditions, and realistic assessment of Palantir candidacy.

**Pages created:** 2 (`career-transition-strategy.md`, `resume-cs-ai-leadership-2026.md`)  
**Pages updated:** 1 (`index.md` — page count 50→52, two new entries in Identity & Public Presence, merge conflicts resolved)

### What this source contains

A comprehensive career pivot strategy triggered by Conley's stated goal of leaving BA for a higher-compensation corporate role within 6–12 months, rising once or twice, then exiting to start his own venture. The strategy incorporates live market research confirming that traditional B2B SaaS is undergoing a structural correction (the "SaaSpocalypse" — $2T in market cap erased, 40% of IT budgets shifting to agentic platforms), which materially changes the target company list.

Key findings: Conley's primary differentiator is genuine AI system-building experience (not just AI tool use), combined with client success and CRM leadership. Security clearance is complicated by his Chinese language/culture academic background (Foreign Influence category). Palantir "Head of AI" was aspirational framing — realistic Palantir target is Deployment Strategist (commercial, no clearance required).

### What changed

- **`career-transition-strategy.md` (created)** — Full strategy page covering: goal and constraints, why traditional SaaS is de-prioritized, role recommendation (AI strategy/CS leadership at AI-native or defense-adjacent companies), target company tables (Philadelphia hybrid + remote), 6–12 month execution plan, what the corporate stint should build toward the venture, doctrine tension note, and open questions.
- **`resume-cs-ai-leadership-2026.md` (created)** — New resume variant targeting AI strategy and CS leadership roles. Key additions over July 2025 variants: Business Actualization / AutoBoost role as "Director of Client Success & Strategy" (March 2025–present), AI Systems & Independent Projects section surfacing multi-agent work, updated skills with n8n/LangGraph/OpenClaw/Claude API/Gemini, updated summary threading AI implementation with CS leadership.
- **`index.md` (updated)** — Page count 50→52, two new rows in Identity & Public Presence section, merge conflicts resolved (two conflicts present from prior branch divergence).

### Notable observations

- The SaaS market concern Conley raised is well-founded and confirmed by current data. The traditional "Director of CS at a SaaS company" role is itself a disruption target — AI agents are replacing the CS workflows that justified per-seat pricing. This is a significant strategic signal for the job search.
- The defense-adjacent path (Palantir commercial, Booz Allen commercial) is strategically compelling because it directly feeds Drone Enterprises — learning DoD procurement, SBIR/OTA, and building the network that makes Drone Enterprises fundable. The security clearance concern is real but doesn't block commercial roles.
- The Thought Leader Engine is an underutilized asset for the job search. Pointing it at LinkedIn (AI in enterprise, CS operations, real implementation stories) for 6 months pre-application creates genuine inbound that most job seekers can't manufacture.
- The "Director of Client Success & Strategy" title is now confirmed usable externally (per Adam and Micah). This changes the resume and LinkedIn positioning meaningfully — he no longer needs to navigate the PM vs. Director ambiguity.
- Open strategic question: whether Drone Enterprises is near-term enough to optimize the job search around defense specifically. That decision should be made explicitly, not by default.
- Inbox note `obs-portfolio-describes-dead-system.md` was deleted by Conley — appropriate, since the observation is no longer true.

---

## [2026-04-27] ingest | Daily Recap — April 20, 2026

**Source type:** BA workday log — first day back from FLACA; Production Meeting, HR interview, four client calls, Menard webmaster breakthrough, South Lake Euro billing transition, FLACA accountability conversation
**Pages created:** 1 (`daily-recap-2026-04-20.md`)
**Pages updated:** 4 (`ba-clients-pipeline.md`, `ba-overview.md`, `ba-team.md`, `ba-partners.md`)

### What this source contains

A high-volume return-to-office day after four days at FLACA in Orlando. Conley attended the full Production Meeting (all 13 staff), co-interviewed HR candidate Hilary Masland, ran four client calls (Rodgers Family Auto monthly review; Import Car/Virginia Auto combined review; OBS Solutions monthly; Lee Myles Autocare multi-location), and reached the Menard webmaster for the first time after weeks of failed contact. Significant internal thread: Micah and Adam raised Hubstaff time data showing Conley missed FLACA conference sessions; Conley took accountability and committed to full attendance at future shows. South Lake European billing transfer to BA initiated in #internal-sales ($799 Google Ads Advanced Legacy, start 4/27).

### What changed

- `ba-clients-pipeline.md` — Multiple status updates: Telle Tire updated (meeting held Apr 21, details added); Bernhard Auto Works updated to "Proposal Declined"; Virginia Auto Service updated (website go-live scheduled Apr 21); Rodgers Family Auto Care updated (active monthly review); Salta updated (formal review held Apr 21); John McCormick updated (BirdEye SMS block documented); A&R Complete Auto updated (meeting held Apr 21); Harford County Transmissions updated (second follow-up sent); Menard Automotive updated in Accounts Needing Attention (breakthrough — path now clear). New entries added: South Lake European, OBS Solutions, Lee Myles Autocare SE PA, Bailey Holston (Auto Repair Mom), Sage Creek Repair, Rantz Automotive, Plover & 6th Street, JulieAnna Howes, Automedics 406, Dennis Auto Repair.
- `ba-overview.md` — FLACA concluded (Conley back Apr 20); Viktor AI assistant added to internal ops stack; Claude Teams usage cap note added; DSA deprecation added to Platform Changes section; TOOLS 2026 conference added.
- `ba-team.md` — Viktor AI assistant noted; hiring section added (Hilary Masland HR interview + marketing generalist candidate review with Micah).
- `ba-partners.md` — Sydney Dorsey added as AutoVitals contact; Jordan Bania follow-up on Rantz noted; Carly Lama Sage Creek campaign note added. Source list and updated dates refreshed across all pages.

### Notable observations

- The Menard breakthrough is the highest-signal operational moment in this recap. A weeks-long tracking installation blocker was resolved in a 2-minute phone call. The human unlock was always available; no one had reached the right person.
- South Lake European's billing transition from AutoVitals to BA is a recurring structural theme: clients can sit on AV billing even when BA is delivering the service. When BA takes direct billing, it increases revenue visibility and control — this transition is worth watching as a model for other AV-billing clients.
- Lee Myles ($24,776 GA spend) is the largest single-advertiser account documented in the recap series so far. Multi-location automotive accounts with active attribution work are BA's highest-complexity tier.
- The Bailey Holston car count gap (strong ads, weak car count) is a structurally important pattern: when call volume is high but booking is low, the constraint is shop-side (staffing, booking window), not marketing. BA can't fix that with ad optimization. Worth flagging in future recaps if this pattern repeats across accounts.
- The FLACA accountability conversation resolves cleanly based on available data but suggests conference management protocols could be clearer (full schedule distributed on arrival, session attendance explicitly expected vs. expo focus). The conversation was honest and constructive on both sides.

---

## [2026-04-27] ingest | Daily Recap — April 21, 2026

**Source type:** BA workday log — packed 8-event meeting day; Telle Tire PE call, Import Car go-live, Viktor first use, Sage Creek record performance, DSA deprecation announced, Claude Teams usage cap
**Pages created:** 1 (`daily-recap-2026-04-21.md`)
**Pages updated:** 0 (rolling pages already updated during April 20 ingest above)

### What this source contains

The highest-volume single day in the recap series so far: 8 scheduled events, five client calls Conley led or co-led, three AV reviews, one internal go-live, and one cancelled meeting. Key signals: Telle Tire discovery call with suspected PE firm contact (Marco Gonzalez, high potential deal); Import Car Specialists website went live; first active use of Viktor AI assistant for live Google Ads metrics in pre-call prep; Sage Creek Repair trending toward record April and appearing in ChatGPT + Gemini search results. Google officially announced DSA deprecation (→ AI Max migration). BA's Claude Teams org hit its monthly usage cap. Hiring progress: resume reviewed for marketing generalist candidate.

### What changed

- `daily-recap-2026-04-21.md` (new) — Full archival page covering all 8 scheduled events, 5 emails, HubSpot calls, Slack activity, 14 open items, and a 6-observation "What This Reveals" section.

### Notable observations

- Viktor's first-day results are operationally significant. Pulling accurate MCC-level metrics for a multi-location client before a live review call is exactly the use case that compresses Conley's pre-call prep time. If Viktor scales across BA's account base, it changes the economics of account management — more accounts per rep with the same quality of preparation.
- Sage Creek Repair appearing in ChatGPT and Gemini search results with 16 documented AI-platform users is the first case of AI search visibility appearing as a client-level metric at BA. This is a selling point that will likely become standard in BA's reporting — AutoBoost clients are visible in AI search. Worth surfacing to the team and in prospect conversations.
- The DSA → AI Max deprecation is a platform-level change affecting every BA client with DSA campaigns. This is a proactive opportunity for BA to consult clients before Google forces migration. Conley surfaced it to Jon immediately — if the team moves fast, this could be a trust-building moment across multiple accounts simultaneously.
- Claude Teams hitting its usage cap on April 21 is a signal worth flagging: a 13-person automotive marketing agency burning through its Claude Teams monthly limit means AI is genuinely embedded, not experimental. This is relevant to Conley's ACE pitch — BA itself is a case study for AI adoption at the SMB agency level.
- The FLACA accountability conversation (April 20) and Conley's return to a smooth, high-output office day (April 21) suggest the conversation closed the loop without ongoing friction. Leadership culture at AutoBoost appears to value accountability over performance-management escalation.
- Index.md merge conflict (between `claude/process-articles-update-wiki-VePUF` and `main` branches) was resolved as part of this ingest session. Combined source count post-merge: 31 unique sources. Two new sources added here: 33 total.

---

## [2026-05-05] ingest | Blog Article Brief — AI-Native Operational Vault

**Source type:** Agent prompt / writing brief — self-contained instructions for producing a 1,200–1,800 word blog article about building an operational second brain for AI agents in an agency context
**Pages created:** 0 (source is a production brief, not wiki content — no new wiki pages warranted)
**Pages updated:** 0
**Draft produced:** `03-BRIEFS/2026-05-05-ai-operational-vault-draft.md`

### What this source contains

A detailed blog article brief authored for a content-writing agent. Covers the full architecture of an "operational vault" — a structured Markdown-based knowledge system designed to give AI agents persistent context before they act. Includes article structure guidance (8-part narrative arc), tone/voice direction (confident, concrete, no hype), SEO target phrases (AI knowledge base for agencies, operational second brain, LLM context management, agentic AI workflows), and the complete vault architecture as background material. Working title: "Your AI Assistant Keeps Forgetting Everything — Here's How We Fixed It."

### What changed

- Draft article produced and saved to `03-BRIEFS/2026-05-05-ai-operational-vault-draft.md`. Proposed alternative title: "Your AI Keeps Starting From Zero. Here's the Architecture That Fixed It." Article runs ~1,400 words in Conley's voice, structured around the eight-part narrative arc specified in the brief.
- `index.md` updated — source count 33 → 34, new source row added to Source Files table.

### Notable observations

- This brief describes what sounds like the BA operational vault — a knowledge system Conley built for the agency's AI agent workflows. The article is positioned for a "digital marketing agency's blog," which maps to either BA's own thought leadership content or Conley's portfolio.
- The architecture described (CLAUDE.md as agent operating manual, INDEX.md as catalog, LOG.md as audit trail, client subfolders with persistent profiles) is structurally analogous to this second brain — the same pattern applied at the team/agency level rather than the personal level. The two articles (this new draft and `second-brain-article.md` in the wiki) are complementary: one covers personal use, the other covers agency/operational use.
- The brief's SEO targets (AI knowledge base for agencies, LLM context management, agentic AI workflows) are a stronger fit for BA's blog or LinkedIn thought leadership than for Conley's personal Threads presence. If this article goes live on a BA or AutoBoost blog, it could drive qualified inbound for the agency — a content marketing asset rather than personal brand content.
- The brief explicitly prohibits revealing specific client names, internal API configurations, or proprietary prompt engineering details — which makes the article publishable on a public blog without confidentiality concerns.

---

## [2026-05-05] update | Obsidian vault improvement — base file, dashboard, frontmatter audit

**Pages created:** 2 (`Wiki Database.base`, `Dashboard.md`)
**Pages updated:** 21 (domain frontmatter added/corrected across wiki pages; one type fix)

### What changed

- **`domain` frontmatter added** to 19 wiki pages that were missing it — `ace-overview.md`, `ace-legacy.md`, `financial-projections.md`, `domain-personal.md`, `data-enrichment-apis.md`, `phase-2-content-vectors.md`, `portfolio-website.md`, `platform-comparison.md`, `operating-doctrine-2026.md`, `muse.md`, `phase-3-infrastructure.md`, `phase-1-lead-enrichment.md`, `the-sentinel.md`, `tech-stack.md`, `upwork-portfolio.md`, `portfolio-update-plan.md`, `the-river-room.md`, `thought-leader-engine.md`, `campaign-plan.md`
- **`client-acquisition.md` domain corrected** from `ba` to `ace` — this page covers Upwork/ACE bidding pipeline, not BA operations
- **`daily-recap-2026-04-15.md` type corrected** from `log` to `work-log` — now consistent with all other recap pages
- **`Wiki Database.base` created** at `wiki/Wiki Database.base` — Obsidian Bases file with 7 views: All Knowledge Pages (table, grouped by domain), Stale Pages (table, pages not updated in 14+ days), Work Logs (table), and domain-specific card views for ACE, Day Job (BA), Drone Enterprises, and Personal. Includes formulas for staleness calculation and type icon display.
- **`Dashboard.md` created** at `Conley's 2nd Brain/Dashboard.md` — vault home page with quick navigation table and embedded base views for each domain. Intended as the default opening note in Obsidian.

### Notable observations

- After domain field audit, the wiki now has fully queryable frontmatter: every page with a `type` field also has a `domain` field, enabling filtering in Bases without fallback logic.
- The Obsidian base renders correctly with 52 knowledge pages grouped by domain. The "Stale Pages" view surfaces pages not updated in 14+ days — useful for tracking which wiki sections are drifting out of sync with reality.
- `the-sentinel.md` was assigned `domain: personal` (not `ace`) — The Sentinel is a personal vision project funded by ACE revenue, but it is not an ACE product or service. The distinction matters for Base filtering.
- The Dashboard `![[Wiki Database.base#View Name]]` embed pattern allows per-domain card views to coexist on a single home page, giving the full knowledge graph at a glance.

---

## [2026-05-12] ingest | Conley Potter Resume 2026 — CV.md created

**Source type:** Current resume (docx) — May 2026 version, supersedes all July 2025 variants
**Pages created:** 1 (`cv.md`)
**Pages updated:** 0

### What this source contains

Conley's most up-to-date resume as of May 2026. Key structural changes from the July 2025 variants: adds the Director of Client Success & Strategy role at Business Actualization / AutoBoost (March 2025–present) with full bullet detail; adds a dedicated AI Systems & Independent Projects section covering the Upwork automation pipeline; updates the summary to foreground AI implementation depth alongside MarTech leadership; expands the skills section to include n8n, LangGraph, Claude API, Gemini API, multi-agent architecture, and HITL pipeline design. Core Competencies are now in a two-column table in the docx — both columns captured in the CV. Skills are split across two tables in the docx; fully reconstructed in the CV.

### What changed

- **`cv.md` created** — canonical CV in clean markdown format, following the example CV format (no code block wrapper, H2/H3 header hierarchy, bullet lists, plain skills section). Includes full contact header, professional summary, all six work experience entries with complete bullet points, AI Systems & Independent Projects, education with honors, and categorized skills. Wiki frontmatter preserved for Obsidian compatibility.
- **`index.md` updated** — source count 37 → 38, page count 61 → 62, `cv.md` added to Identity & Public Presence section, new source row added.

### Notable observations

- The July 2025 resume variants (`resume-variants.md`) are now superseded by this source. `resume-cs-ai-leadership-2026.md` is similarly superseded — `cv.md` is the new canonical document. Neither old page should be deleted (they have historical value and context), but future resume-related queries should draw from `cv.md` first.
- The BA role bullet points in this docx are more expansive than in `resume-cs-ai-leadership-2026.md` — includes Viktor/Boostbot details, the AutoBoost-Vault build, and the GBP/programmatic channels mention that the earlier wiki version omitted. `cv.md` reflects these additions.
- The "Manager of Financial Empowerment Center" at Tenfold overlaps in time with the "Freelance Digital Marketing Director" period (July 2022–October 2023 inside January 2021–February 2024). The resume presents them as sequential under different headers, which is standard practice for concurrent roles — not an error.

---

## [2026-05-16] ingest | How to Build a Team of AI Agents That Actually Work Together

**Source type:** X thread by @eng_khairallah1 — comprehensive guide/course on multi-agent AI orchestration patterns, based on Anthropic's Claude Managed Agents announcement (May 6, 2026)
**Pages created:** 1 (`multi-agent-orchestration.md`)
**Pages updated:** 0

### What this source contains

A ~2,500-word X thread presenting a full course on building multi-agent AI systems. Covers three proven orchestration patterns (Pipeline, Fan-Out, Specialist Team), a seven-step build process, two new Anthropic features (Dreaming for agent memory and Outcomes for rubric-based self-evaluation), and production examples from Netflix, Harvey, Shopify, and Mercado Libre. Also notes Apple's announcement of Claude integration into iOS 27.

### What changed

- `multi-agent-orchestration.md` (new) — synthesis page covering the three orchestration patterns, seven-step build process, production example (Weekly Market Intelligence Report), common mistakes, and cross-references to existing wiki pages (JARVIS, gstack, TLE, Opus 4.7 workflow).
- `index.md` updated — source count 38 → 39, page count 62 → 63, new page added to General Knowledge section, new source row added to Source Files.

### Notable observations

- The three patterns (Pipeline, Fan-Out, Specialist Team) map directly to systems Conley is already building. JARVIS is essentially Pattern 1 (pipeline). The Second Brain Ingest Agent built today in Hyperagent is a simpler version of Pattern 2 (fan-out) — a commander (the agent) distributing work across tools.
- Dreaming as a concept — scheduled background review of past sessions to extract patterns and curate memory — is structurally identical to what this wiki does manually. If Anthropic's Managed Agents can automate this, it could complement or partially replace the manual ingest workflow.
- Harvey's claimed 6x completion rate improvement from Dreaming alone is a striking data point. If accurate, it suggests persistent memory is the highest-leverage improvement for any agent system — more impactful than model upgrades or prompt engineering.
- This is the first source captured and ingested entirely through the new Hyperagent Second Brain Ingest Agent — fetched from an X.com URL via browser automation, converted to markdown, and committed to the repo without touching Claude Code locally.
- The Apple/iOS 27 Claude integration mention is a significant industry signal worth tracking — Claude becoming a system-level service on Apple devices changes distribution dynamics for anyone building Claude-based tools.

---

## [2026-05-17] split | portfolio-update-plan.md — archive completed queries

**Trigger:** Issue #38 — page at 34KB mixes completed historical queries with still-actionable pending work
**Pages created:** 1 (`portfolio-update-history.md`)
**Pages updated:** 1 (`portfolio-update-plan.md`)

### What changed

- **`portfolio-update-history.md` created** (type: work-log, domain: personal) — archives completed coding-agent queries 1–4 from the Portfolio Website Update Plan. Includes the executed changes summary for each query and the full original spec for Query 3 (about page brand voice injection).
- **`portfolio-update-plan.md` slimmed** — replaced inline Query 1–4 content with a summary table and pointer to `portfolio-update-history.md`. Pending queries 5–9, the QA checklist, and all shared context sections retained. Reduced from 33,947 bytes to ~27,100 bytes.
- **`index.md` updated** — page count 65 → 66, `portfolio-update-plan` description updated, `portfolio-update-history` entry added to Identity & Public Presence section.

### Notable observations

- The remaining plan page is still ~27KB because Queries 5–9 are individually large (Query 5 contains a full article body, Queries 7–8 contain detailed career timeline specs). A further split is not warranted — the remaining content is all actionable pending work with a coherent purpose.
- Queries 5–8 remain applicable post-PBE pivot: they address the portfolio website's career history, capabilities, and writing section, none of which are ACE-specific.
- Query 9 (Upwork profile URL) may be stale given the freelance strategy deprioritization, but it's deferred and trivial — left as-is.
## [2026-05-17] ingest | Perplexity Agent Skills Guide

**Source type:** Engineering blog post — internal guide to designing agent skills at Perplexity
**Pages created:** 1 (`perplexity-agent-skills.md`)
**Pages updated:** 0

### What this source contains

Perplexity's Agents team published their internal playbook for building, reviewing, and maintaining Agent Skills — the modular knowledge packages powering Perplexity Computer. The guide systematically inverts conventional software engineering intuitions: skills are directories not files, descriptions are routing triggers not documentation, gotchas are the highest-value content, and anything the model already knows should be deleted. It covers the three-tier progressive disclosure cost model, a four-step build process (description → body → hierarchy → iterate), and a rigorous eval framework (precision, recall, forbidden loads, file reads, end-to-end quality).

### What changed

- Created `perplexity-agent-skills.md` in General Knowledge with full structured summary
- Added page to index.md General Knowledge section
- Added raw source to index.md Source Files table

### Notable observations

- The "description as routing trigger" principle directly applies to Hyperagent skill design and the vault's own agent architecture
- Progressive disclosure (100 tokens index → full SKILL.md → conditional references) mirrors how this vault's agents selectively load context
- The emphasis on evals before skills is a pattern worth adopting for the second brain agent pipeline
- Connects to [[gstack]], [[llm-wiki-pattern]], and [[second-brain-mcp-server]]

## [2026-05-17] ingest | Mitchell Hashimoto on AI Psychosis

**Source type:** X thread — opinion piece on AI-assisted development risks
**Pages created:** 1 (`ai-psychosis-hashimoto.md`)
**Pages updated:** 0

### What this source contains

Mitchell Hashimoto (@mitchellh, co-founder of HashiCorp) posted a widely-shared thread warning about "AI psychosis" in software development. He draws a direct parallel to the MTBF vs. MTTR reckoning during the cloud infrastructure transition: organizations are adopting an uncritical "agents will fix the bugs" mentality, and surface-level metrics (test coverage up, bug reports down) mask systemic architectural decay. The thread resonated broadly (12K+ likes, 1M+ views).

### What changed

- Created `ai-psychosis-hashimoto.md` in General Knowledge with structured summary
- Added page to index.md General Knowledge section
- Added raw source to index.md Source Files table

### Notable observations

- Useful counterbalance to the vault's generally pro-AI-leverage stance — acknowledges the real risk of over-delegation
- Connects to [[operating-doctrine-2026]]'s emphasis on using AI without losing comprehension
- The MTBF/MTTR framing is a concise way to explain this risk in content and conversations
- At 1M+ views this is a culturally significant signal in the engineering community worth tracking

---

## [2026-05-18] ingest | Orphan raw-source wiki coverage — Wedding Prayer, Sam Schutt notes, gig-portfolio

**Source type:** Three orphan raw-sources identified by Vault Steward (issue #42)
**Pages created:** 1 (`wedding-prayer.md`)
**Pages updated:** 2 (`sam-schutt.md`, `portfolio-website.md`)

### What these sources contain

Three raw-source files lacked wiki coverage: (1) Wedding Prayer.md — Conley's ceremony prayer by Olivia and his dinner speech/prayer for the June 12, 2026 wedding; (2) Notes on Meeting with Sam Schutt - DENT.md — technical drone notes on Faraday cage EMF protection, nickel coating, PETG shell materials; (3) gig-portfolio snapshot of the portfolio Projects page showing the updated ACE/Sentinel/TLE descriptions.

### What changed

- Created `wedding-prayer.md` (Personal domain) with structured summary of both prayers
- Enriched `sam-schutt.md` with a new "Technical contributions" section containing EMF protection and materials science details from the DENT meeting notes; added source citation
- Added `gig-portfolio...md` as a source citation in `portfolio-website.md` (content was already absorbed)
- Updated `index.md` page count and added wedding-prayer entry to the Personal section

### Notable observations

- The Wedding Prayer raw-source was intentionally captured to the second brain, confirming personal/life content is in scope
- Sam Schutt's meeting notes contain specific materials science knowledge (Faraday cage, nickel coating, PETG) that enriches the drone engineering picture beyond what's in drone-enterprises.md
- The gig-portfolio snapshot was captured after the April 2026 portfolio update — it shows the corrected ACE description, not the old one. No new wiki content was needed

## [2026-05-20] ingest | AutoBoost Vault — Skills Development Reflection

**Source type:** Personal voice-note reflection on internal AI tooling development
**Pages created:** 1 (`autoboost-vault-skills.md`)
**Pages updated:** 0

### What this source contains

Conley's reflection on a productive day spent transitioning personal slash commands into reusable skills and routines for the AutoBoost Vault project. He is preparing the system for team-wide rollout at BA, which requires making the tooling accessible to non-technical team members. He also notes the Hyperagent skills model — skills as folders of scripts — as a significant capability upgrade.

### What changed

- Created `autoboost-vault-skills.md` (type: operations, domain: ba) documenting the slash-commands-to-skills migration, team rollout plans, and Hyperagent skills architecture insights
- Added page to Day Job (BA) section of `index.md`; page count 66 → 67
- Added source to Source Files table; source count 40 → 41

### Notable observations

- This is the first signal that BA's internal AI tooling is expanding beyond Conley's personal use to a team-wide rollout — significant for `ba-overview.md`
- The skills-as-folders model Conley describes aligns with the architecture he's building in Hyperagent for his personal second brain agents
- The "make it friendly for the whole team" challenge echoes the UX simplification theme in `tech-stack.md` and could generate future wiki pages on internal tooling adoption

## [2026-05-20] ingest | Mom's Housing Offer — Lebanon PA Multi-Gen Property

**Source type:** Personal voice-note capturing a family housing proposal
**Pages created:** 1 (`housing-offer-lebanon.md`)
**Pages updated:** 0

### What this source contains

Conley's mom and Jim have invited Conley and Sami to move into a six-bedroom multi-generation property at 1403 Douglas Fir Drive, Lebanon, PA (Cornwall School District). The lower floor offers ~2,000 sq ft of independent living space with its own entrance, driveway, and patio. Rent would be ~$1,100 including all utilities. Closing is June 30, 2026 — 18 days after the wedding. Mom's motivation: help Sami stop working to start a family, provide childcare, and help them save for a first home.

### What changed

- Created `housing-offer-lebanon.md` (type: identity, domain: personal) documenting the property details, timeline, financial terms, and family context
- Added page to Personal section of `index.md`; page count 67 → 68
- Added source to Source Files table; source count 41 → 42

### Notable observations

- The June 30 closing compresses two major life transitions (wedding + move) into a single month — worth flagging in `conley-potter.md` when the time comes
- The ~$1,100/month all-inclusive rent represents a dramatic cost reduction that directly supports the 2026 operating doctrine's financial goals
- Mom's offer to help with childcare signals a near-term family planning timeline — `conley-potter.md` should be updated post-wedding with these life developments
- The property includes a workshop/art studio building that could be relevant to The River Room or future creative projects
---

## [2026-05-31] lint | Weekly deep audit — Vault Keeper consolidated run

**Audit scope:** Full catalog integrity, orphans, contradictions, stale pages, split candidates, domain emergence
**Direct fixes:** 2 (index.md header drift, index.md missing LGS sections)
**PRs opened:** 1 (CI VALID_DOMAINS update)
**Issues filed:** 1 (stale PR review queue)
**Issues closed:** 2 (#34, #36 — resolved by PR #53)

### Vault state at audit time

- 68 wiki pages on disk, 42 raw-source files
- index.md header: page count corrected 67→68, last updated corrected to 2026-05-31
- Source count: 40 in index (2 orphan sources covered by open PR #60)
- 7 open issues (2 now closed), 3 open PRs awaiting Conley's review
- CLAUDE.md: Vault Keeper consolidation merged (PR #63, 2026-05-30) — three-agent architecture replaced by single agent with four modes; long-game-studios domain added to doctrine

### What changed

- **index.md header fixed** — page count 67→68 (was undercounting by 1 since PR #53 merge), last updated date 2026-05-17→2026-05-31
- **index.md sections added** — empty "Long Game Studios" and "Long Game Studios Dev Logs" sections inserted between Drone Enterprises and Meta, matching the section organization specified in CLAUDE.md after the Vault Keeper consolidation
- **CI validation PR filed** — `long-game-studios` must be added to `VALID_DOMAINS` in `.github/scripts/check_vault.py` so future wiki pages with that domain pass the validate check
- **Issues #34 and #36 closed** — orphan raw-sources (Perplexity agent skills, Hashimoto AI psychosis) were resolved by PR #53 (merged 2026-05-22) but issues remained open because the commit used "Addresses" instead of "Closes"
- **Stale PR review queue flagged** — PRs #54, #56, #60 have been awaiting Conley's review for 11–14 days; filed issue to surface the backlog

### Notable observations

- The Vault Keeper consolidation (PR #63) merged the CLAUDE.md doctrine update on 2026-05-30, formally replacing the three-agent architecture with a single agent operating in four modes. This is the first weekly audit run under the new consolidated identity.
- No new raw-source captures since 2026-05-19 (12 days). The capture pipeline has been idle — likely reflecting Conley's focus on the LGS product build and Vault Keeper consolidation rather than knowledge ingest.
- Three open PRs (#54, #56, #60) from the Remediator are aging. All are labeled `remediator-review` and require Conley's merge. PR #60 in particular has merge conflicts with current main (its base predates PR #53's merge). These will need rebasing before they can merge cleanly.
- The wedding on June 12 is 12 days away. `conley-potter.md` currently says "engaged to Sami" — the "Known pages needing attention" section in CLAUDE.md tracks this update for post-wedding. No action needed yet.
- Issue #41 (log ordering violations) is marked `remediator-claimed`. The forward-looking fix is working — all entries since May 12 are in strict chronological order. The historical disorder remains as-is per the append-only rule.
- The `long-game-studios` domain is now in CLAUDE.md doctrine but NOT in the CI validation script. Until the CI PR merges, any wiki page with `domain: long-game-studios` will fail the validate check. This is a soft blocker for the first Dev-Log Capture mode run.


---

## [2026-06-01] lint | Daily light sweep

**Audit scope:** Trivial drift — index header counts, last-updated date
**Direct fixes:** 1 (index.md page count 68→71, last updated 2026-05-31→2026-06-01)
**PRs opened:** 0
**Issues filed:** 0

### Vault state at sweep time

- 71 wiki pages on disk, 42 raw-source files
- 0 open PRs, 0 open issues — all prior remediator work merged
- CLAUDE.md Vault Keeper consolidation live; `long-game-studios` domain in both doctrine and CI validation
- Capture pipeline idle since 2026-05-19 (13 days)
- Wedding in 11 days (June 12)

### What changed

- **index.md header fixed** — page count 68→71. Three pages landed via PR merges on 2026-05-31 afternoon (after the weekly audit's header correction at 10:11 UTC): `portfolio-update-history.md` (PR #54), `autoboost-vault-skills.md` and `housing-offer-lebanon.md` (PR #60). All three pages were already listed in the section tables by those same PRs — only the header counter was stale.
- **index.md last updated** — 2026-05-31→2026-06-01.

### Notable observations

- Cleanest vault state to date: zero open PRs, zero open issues. The entire backlog of remediator work (PRs #54, #56, #60, #64) was merged by Conley on May 31.
- The `long-game-studios` CI validation fix (PR #64) is now live — Dev-Log Capture mode is unblocked for its first run.
- No new raw-source captures in 13 days. Expected given the wedding and LGS product build focus.


---

## [2026-06-03] lint | Daily light sweep

**Audit scope:** Trivial drift — index header counts, last-updated date, frontmatter, source attribution, orphan detection
**Direct fixes:** 0
**PRs opened:** 0
**Issues filed:** 0

### Vault state at sweep time

- 71 wiki pages on disk, 42 raw-source files
- 0 open PRs, 0 open issues — cleanest state maintained for a third consecutive day
- CLAUDE.md Vault Keeper consolidation live; `long-game-studios` domain in both doctrine and CI validation
- Capture pipeline idle since 2026-05-19 (15 days)
- Wedding in 9 days (June 12)

### What was checked

- **index.md header:** page count 71 matches actual wiki directory (71 .md files minus index.md and log.md). Source count 42 matches Source Files table rows and raw-sources/ directory listing. Last updated 2026-06-01 is correct (no index modifications since then).
- **Frontmatter spot-check:** 3 pages sampled (`autoboost-vault-skills.md`, `housing-offer-lebanon.md`, `portfolio-update-history.md`) — all have valid type, domain, tags, created/updated dates, and source attribution.
- **Raw-sources orphan check:** all 42 files in raw-sources/ have corresponding wiki pages and Source Files table entries. No orphans.
- **log.md compliance:** append-only, newest at bottom, no ordering violations.
- **Open PRs/issues:** none. No coordination labels to reconcile.

### Notable observations

- Third consecutive clean sweep. The full remediator backlog clearance on May 31 left the vault in stable equilibrium.
- Capture pipeline has been idle for 15 days (since May 19). Expected — Conley's focus has been on the LGS product build and wedding preparation.
- Wedding is June 12, 9 days away. `conley-potter.md` currently says "engaged to Sami" — tracked in CLAUDE.md "Known pages needing attention" for a post-wedding update.
- The Long Game Studios sections in index.md are still empty. Dev-Log Capture mode is unblocked (CI validation includes `long-game-studios`) but has not yet run its first capture.

---

## [2026-06-04] lint | Daily light sweep

**Audit scope:** Trivial drift — index header counts, last-updated date, frontmatter, source attribution, orphan detection
**Direct fixes:** 0
**PRs opened:** 0
**Issues filed:** 1

### Vault state at sweep time

- 71 wiki pages on disk, 42 raw-source files
- 0 open PRs, 0 open issues — cleanest state maintained for a fourth consecutive day
- CLAUDE.md Vault Keeper consolidation live; `long-game-studios` domain in both doctrine and CI validation
- Capture pipeline idle since 2026-05-19 (16 days)
- Wedding in 8 days (June 12)

### What was checked

- **index.md header:** page count 71 matches actual wiki directory (71 .md files minus index.md and log.md). Source count 42 matches Source Files table rows and raw-sources/ directory listing (42 files). Last updated 2026-06-01 is correct (no index modifications since then).
- **Index-to-disk cross-check:** all 71 wiki pages on disk are referenced in index.md section tables; all index.md [[page-name]] references resolve to files on disk. No orphans, no phantom references.
- **Frontmatter spot-check:** 2 pages sampled (`domain-general.md`, `wedding-prayer.md`) — both have valid type, domain, tags, created/updated dates, and source attribution.
- **Raw-sources orphan check:** all 42 files in raw-sources/ have corresponding wiki pages and Source Files table entries. No orphans.
- **log.md compliance:** append-only, newest at bottom, no ordering violations.
- **Open PRs/issues:** none prior to this sweep. No coordination labels to reconcile.

### What was found

- **domain-general.md stale anchor table** — the domain anchor page lists only 4 pages in its "Pages in this domain" table, but the General Knowledge section of index.md now has 12 entries (11 excluding domain-general itself). At least 7 pages added since the anchor was created on 2026-04-17 are missing from its internal table. Filed as vault-steward issue — requires reading each page's frontmatter to determine which pages truly have `domain: general` vs. being categorized elsewhere.

### Notable observations

- Fourth consecutive clean sweep (no header/count drift). The vault has been in stable equilibrium since the full backlog clearance on May 31.
- Capture pipeline has been idle for 16 days (since May 19). Expected — Conley's focus is on wedding preparation and LGS product build.
- Wedding is June 12, 8 days away. `conley-potter.md` currently says "engaged to Sami" — tracked in CLAUDE.md "Known pages needing attention" for a post-wedding update.
- Long Game Studios sections in index.md remain empty. Dev-Log Capture mode is unblocked but has not yet run its first capture.
- The `domain-general.md` stale-anchor finding is the first new issue surfaced since the June 1 sweep cleared all outstanding work. It confirms that domain anchor pages need periodic refresh as the wiki grows — other anchors (`domain-drone-enterprises.md`, `domain-personal.md`) may warrant similar review during the next weekly deep audit.

---

## [2026-06-04] update | Refresh domain-general.md anchor table

**Source type:** Vault Keeper Remediate pass — Issue #66 (domain-general.md anchor table stale)

### What changed

- **domain-general.md** — Added 7 missing pages to the "Pages in this domain" table, bringing the total from 4 to 11. All 7 pages confirmed as `domain: general` via frontmatter inspection: `markitdown`, `second-brain-mcp-server`, `jarvis-system`, `drone-opportunity`, `multi-agent-orchestration`, `perplexity-agent-skills`, `ai-psychosis-hashimoto`. Updated `updated` frontmatter date from 2026-04-17 to 2026-06-04.

### Notable observations

- All 7 candidate pages listed in Issue #66 confirmed as `domain: general` — no false positives from the index.md section-based heuristic.
- `drone-opportunity.md` has `domain: general` despite being thematically related to the Drone Enterprises project (which has its own domain and anchor page). This may warrant reclassification to `domain: drone-enterprises` in a future audit, but the current frontmatter is authoritative.
- This is the first domain anchor page to need a refresh. Other anchors (`domain-drone-enterprises.md`, `domain-personal.md`) should be checked during the next weekly deep audit to prevent similar drift.

---

## [2026-06-05] lint | Daily light sweep

**Audit scope:** Trivial drift — index header counts, last-updated date, frontmatter, source attribution, orphan detection, open PR/issue reconciliation
**Direct fixes:** 0
**PRs merged:** 1 (PR #67 — domain-general.md anchor refresh, CI-green for 19h but auto-merge had not triggered)
**PRs opened:** 0
**Issues filed:** 0

### Vault state at sweep time

- 71 wiki pages on disk, 42 raw-source files
- 1 open PR (#67, remediation confidence 0.93, CI passed, unlabeled — expected auto-merge)
- 1 open issue (#66, labeled remediator-claimed — addressed by PR #67)
- CLAUDE.md Vault Keeper consolidation live; `long-game-studios` domain in both doctrine and CI validation
- Capture pipeline idle since 2026-05-19 (17 days)
- Wedding in 7 days (June 12)

### What was checked

- **index.md header:** page count 71 matches actual wiki directory (71 .md files minus index.md and log.md). Source count 42 matches Source Files table rows and raw-sources/ directory listing (42 files). Last updated 2026-06-01 is correct (no index modifications since then).
- **Index-to-disk cross-check:** all 71 wiki pages on disk are referenced in index.md section tables; all index.md [[page-name]] references resolve to files on disk. No orphans, no phantom references.
- **Frontmatter spot-check:** 2 pages sampled (`multi-agent-orchestration.md`, `career-transition-strategy.md`) — both have valid type, domain, tags, created/updated dates, and source attribution.
- **Raw-sources orphan check:** all 42 files in raw-sources/ have corresponding wiki pages and Source Files table entries. No orphans.
- **log.md compliance:** append-only, newest at bottom, no ordering violations.
- **Open PR reconciliation:** PR #67 (remediator fix for domain-general.md anchor) had CI validate passing since 2026-06-04T16:05:51Z but had not auto-merged. Merged manually during this sweep — PR was unlabeled at confidence 0.93, within auto-merge policy.
- **Open issue reconciliation:** Issue #66 closed automatically by PR #67 merge.

### Notable observations

- Fifth consecutive clean sweep with no header/count drift. The vault remains in stable equilibrium since the full backlog clearance on May 31.
- PR #67's failure to auto-merge despite passing CI suggests auto-merge may not be reliably enabled on agent-created PRs. Worth investigating in the next remediation run to ensure the `enable auto-merge` flag is set on high-confidence PRs at creation time.
- Capture pipeline has been idle for 17 days (since May 19). Expected — Conley's focus is on wedding preparation and LGS product build.
- Wedding is June 12, 7 days away. `conley-potter.md` currently says "engaged to Sami" — tracked in CLAUDE.md "Known pages needing attention" for a post-wedding update.
- Long Game Studios sections in index.md remain empty. Dev-Log Capture mode is unblocked but has not yet run its first capture.
- Post-merge vault state: 0 open PRs, 0 open issues. Cleanest state maintained.


---

## [2026-06-06] lint | Daily light sweep

**Audit scope:** Trivial drift — index header counts, last-updated date, frontmatter, source attribution, orphan detection, open PR/issue reconciliation
**Direct fixes:** 0
**PRs opened:** 0
**Issues filed:** 0

### Vault state at sweep time

- 71 wiki pages on disk, 42 raw-source files
- 2 open PRs (#68 first dev-log capture, #69 No Priors podcast ingest) — both opened 2026-06-05 after last sweep
- 0 open issues
- CLAUDE.md Vault Keeper consolidation live; `long-game-studios` domain in both doctrine and CI validation
- Capture pipeline reactivated: first ingest (PR #69) since 2026-05-19 (18 days idle)
- Wedding in 6 days (June 12)

### What was checked

- **index.md header:** page count 71 matches actual wiki directory (71 .md files minus index.md and log.md). Source count 42 matches Source Files table rows and raw-sources/ directory listing (42 files). Last updated 2026-06-01 is correct (no index modifications since then on main).
- **Index-to-disk cross-check:** all 71 wiki pages on disk are referenced in index.md section tables; all index.md [[page-name]] references resolve to files on disk. No orphans, no phantom references.
- **Frontmatter spot-check:** 3 pages sampled (`writing-style.md`, `book-project-2025.md`, `conley-potter.md`) — all have valid type, domain, tags, created/updated dates, and source attribution.
- **Raw-sources orphan check:** all 42 files in raw-sources/ have corresponding wiki pages and Source Files table entries. No orphans.
- **log.md compliance:** append-only, newest at bottom, no ordering violations.
- **Open PR reconciliation:** 2 PRs opened after yesterday's sweep — PR #68 (first LGS dev-log capture, 4 pages + 3 PBE captures) and PR #69 (No Priors Nadella podcast ingest, 1 page). Both are well-formed Vault Keeper branches (devlog/, ingest/ prefixes). Both modify index.md and log.md from the same base commit (24ebc6a); the second to merge will need a rebase to resolve index/log conflicts.
- **Open issue reconciliation:** none. No coordination labels to reconcile.

### Notable observations

- Sixth consecutive clean sweep with no header/count drift. The vault remains in stable equilibrium.
- The capture pipeline is active again after 18 days idle. PR #69 is the first new ingest since May 19 — a Spotify podcast episode (No Priors with Satya Nadella). PR #68 is the inaugural Dev-Log Capture mode run, synthesizing all DailyChew and The Grind development history.
- Both open PRs modify the same navigation files (index.md, log.md) from the same base. Whichever merges first will cause a merge conflict on the other. This is expected behavior for concurrent agent branches and is not a vault integrity issue — the second PR will need a rebase before its CI can pass.
- Wedding is June 12, 6 days away. `conley-potter.md` currently says "engaged to Sami" — tracked in CLAUDE.md "Known pages needing attention" for a post-wedding update.
- Long Game Studios sections in index.md remain empty on main. PR #68 populates them with 4 new pages (domain anchor, two product overviews, one archival dev-log). Once it merges, the LGS domain will be fully bootstrapped in the vault.


---

## [2026-06-07] lint | Weekly deep audit

**Audit scope:** Full vault review — catalog integrity, completeness, orphans, contradictions, stale pages, split candidates, domain emergence
**Direct fixes:** 0
**PRs opened:** 2 (vault-steward labeled, never auto-merge)
**Issues filed:** 6 (vault-steward labeled)

### Vault state at audit time

- 71 wiki pages on disk, 42 raw-source files (unchanged from last sweep)
- 4 open PRs: #68 (first dev-log capture), #69 (No Priors podcast ingest), #70 (HDBSCAN ingest), #71 (Graphiti ingest) — all expected in-flight Vault Keeper work
- 0 open issues at audit start
- CLAUDE.md Vault Keeper consolidation live; `long-game-studios` domain in both doctrine and CI validation
- Wedding in 5 days (June 12, 2026)

### What was checked

- **Index-to-disk cross-check:** all 71 wiki pages on disk referenced in index.md; all index.md references resolve. No orphans, no phantom references.
- **Raw-sources orphan check:** all 42 files accounted for. No orphans.
- **Frontmatter validation:** 20-page deep sample + 6-page domain verification = 26 pages checked (36% of vault). All have valid required fields (type, domain, tags, created, updated). One date mismatch found (ace-overview.md).
- **Domain anchor audit:** 3 existing anchors reviewed (domain-general.md, domain-personal.md, domain-drone-enterprises.md). Two missing anchors identified (ba, ace).
- **Staleness assessment:** 14 of 20 sampled pages not updated in 6+ weeks. Expected — Conley's focus on wedding prep and LGS product build. 9 ACE pages properly archived with banners.
- **Content contradiction:** conley-potter.md still has LinkedIn/ACE separation protocol that contradicts content-strategy.md (retirement of that protocol).
- **Split candidates:** None identified. No pages are oversized or covering multiple unrelated topics.
- **Domain emergence:** No new domains emerging. long-game-studios domain is in-flight (PR #68 creates the anchor).
- **Open PR evaluation:** All 4 PRs are well-formed Vault Keeper branches. PRs #68 + #69 share a base (24ebc6a); PRs #70 + #71 share a base (232d9f8). All conflict on index.md/log.md — must merge sequentially.

### Issues filed

| # | Title | Nature |
|---|---|---|
| #72 | drone-opportunity.md domain reclassification (general → drone-enterprises) | Domain judgment call |
| #73 | portfolio-update-plan.md PBE pivot review | Content review |
| #74 | Post-wedding content updates (conley-potter.md + portfolio pages) | Scheduled June 12+ |
| #75 | ba-clients-pipeline.md rolling page stale | Needs source from Conley |
| #76 | the-sentinel.md + the-river-room.md ACE funding references stale | Content update |
| #77 | ace-overview.md frontmatter date mismatch + ace domain anchor question | Frontmatter + domain judgment |

### PRs opened

| # | Title | Nature |
|---|---|---|
| #78 | Create domain-ba.md anchor page | New wiki (confidence 0.85) |
| #79 | Refresh domain-personal.md — add 12 missing pages | Gap-fill (confidence 0.85) |

### Notable observations

- Seventh consecutive week with no index/log count drift. The vault's structural integrity is solid.
- The personal domain anchor was the most incomplete artifact found: 6 of 18 pages listed. This was the original anchor (April 14), predating the vault's expansion into identity, career, and portfolio pages.
- The ACE→PBE pivot (May 2026) left a broad ripple of stale references: operating-doctrine-2026, conley-potter, portfolio-update-plan, the-sentinel, the-river-room, and domain-personal.md itself. These are tracked across issues #73, #74, #76, and PR #79. A single pass to reconcile all ACE references would be efficient but requires Conley's direction on scope.
- Wedding is June 12, 5 days away. The post-wedding content update (issue #74) is pre-filed for the Remediate pipeline to pick up on or after June 12.
- housing-offer-lebanon.md has a June 30 closing date — 23 days away. May warrant a status update post-closing.
- 4 open capture/devlog PRs all conflict on index.md/log.md. Merging them will require sequential rebases. This is expected behavior for concurrent agent branches and is not a vault integrity issue.


---

## [2026-06-07] lint | Daily light sweep

**Audit scope:** Trivial drift — index header counts, last-updated date, frontmatter, source attribution, orphan detection, open PR/issue reconciliation
**Direct fixes:** 0
**PRs opened:** 0
**Issues filed:** 0

### Vault state at sweep time

- 71 wiki pages on disk, 42 raw-source files (unchanged from weekly deep audit ~1h ago)
- 6 open PRs: #68 (first dev-log capture), #69 (No Priors ingest), #70 (HDBSCAN ingest), #71 (Graphiti ingest), #78 (domain-ba anchor), #79 (domain-personal refresh) — all expected in-flight Vault Keeper work
- 6 open issues: #72–#77, all filed by today's weekly deep audit, all labeled vault-steward, none yet claimed by Remediate (12pm ET run pending)
- Wedding in 5 days (June 12, 2026)

### What was checked

- **Index header verification:** page count 71, source count 42, last-updated 2026-06-01 — all correct. No pages added or removed on main since June 1 index update.
- **Disk-to-index cross-check:** 71 wiki .md files on disk (excl index.md, log.md), 42 raw-source files on disk — both match index.md header counts exactly.
- **log.md compliance:** append-only, newest at bottom, no ordering violations. Weekly audit entry from earlier today correctly formatted.
- **Open PR reconciliation:** 6 PRs open, all from recognized Vault Keeper branches (devlog/, ingest/, steward/ prefixes). 4 capture/devlog PRs (#68–#71) need sequential rebasing — all modify index.md/log.md from behind-main base commits. 2 steward PRs (#78, #79) labeled vault-steward, Conley merges.
- **Open issue reconciliation:** 6 issues (#72–#77) all filed today by weekly audit, all labeled vault-steward, none with Remediate labels. Correctly awaiting the 12pm ET Remediate pass.

### Notable observations

- Ninth consecutive clean sweep with no header/count drift. Vault structural integrity remains solid.
- The weekly deep audit ran ~1 hour before this sweep. No new commits or merges in that window — vault state unchanged. This sweep is a confirmation pass.
- 6-PR merge queue is the longest in vault history. PRs #68–#69 are based on commit 24ebc6a (3 commits behind main); PRs #70–#71, #78–#79 are based on 232d9f8 (1 commit behind). All conflict on index.md/log.md. Sequential rebase needed — not a trivial fix.
- All 6 issues from the weekly audit are fresh and awaiting the 12pm Remediate pass. No coordination label conflicts.
- Wedding in 5 days. Post-wedding content updates tracked in issue #74 (deferred to June 12+).


---

## [2026-06-08] lint | Daily light sweep

**Audit scope:** Trivial drift — index header counts, last-updated date, frontmatter, source attribution, orphan detection, open PR/issue reconciliation
**Direct fixes:** 3 (merge stale PR, add missing labels)
**PRs opened:** 0
**Issues filed:** 0

### Vault state at sweep time

- 71 wiki pages on disk, 42 raw-source files (unchanged)
- 10 open PRs at start: #68 (first dev-log capture), #69 (No Priors ingest), #70 (HDBSCAN ingest), #71 (Graphiti ingest), #78 (domain-ba anchor), #79 (domain-personal refresh), #80 (ace-overview date fix), #81 (ACE→LGS funding refs), #82 (drone domain reclass), #83 (portfolio-plan archive)
- 6 open issues: #72–#77, all from yesterday's weekly audit
- Wedding in 4 days (June 12, 2026)

### What was checked

- **Index header verification:** page count 71, source count 42, last-updated 2026-06-01 — all correct. No pages added or removed on main since June 1 index update.
- **Disk-to-index cross-check:** 71 wiki .md files on disk (excl index.md, log.md), 1 non-.md file (Wiki Database.base), 42 raw-source files on disk — all match index.md headers.
- **log.md compliance:** append-only, newest at bottom, no ordering violations. Yesterday's weekly audit and daily sweep entries correctly formatted.
- **Open PR reconciliation:** 10 PRs open at start. PR #80 (confidence 0.95, frontmatter date fix, no label) was stale — 15h without auto-merge. Merged manually; auto-merge likely failed because it was not explicitly enabled on the individual PR. PRs #78 and #79 (weekly audit PRs) were missing `vault-steward` labels — added. After fixes: 9 PRs remain open.
- **Open issue reconciliation:** 6 issues (#72–#77). Labels: #72 remediator-claimed (PR #82 draft), #73 remediator-claimed (PR #83 draft), #74 vault-steward only (June 12+ deferred), #75 remediator-skipped (needs Conley input), #76 remediator-claimed (PR #81), #77 remediator-claimed (PR #80, now merged — frontmatter part resolved, domain anchor question still open).

### Direct fixes applied

1. **Merged stale PR #80** — ace-overview.md frontmatter `updated` date correction (confidence 0.95, auto-merge eligible but stuck). Squash merged. Issue #77 remains open for the domain anchor question.
2. **Added `vault-steward` label to PR #78** — weekly audit PR (domain-ba anchor) was missing its coordination label.
3. **Added `vault-steward` label to PR #79** — weekly audit PR (domain-personal refresh) was missing its coordination label.

### Notable observations

- Tenth consecutive clean sweep with no header/count drift. Vault structural integrity remains solid.
- 9-PR merge queue is the longest in vault history (down from 10 after merging #80). 4 capture/devlog PRs (#68–#71) and 4 remediation PRs (#81–#83 + now-merged #80) all conflict on index.md/log.md. Sequential merge-and-rebase is needed — not a trivial fix, but expected behavior for concurrent agent branches.
- The auto-merge gap on PR #80 suggests the Remediate mode may not be explicitly enabling auto-merge on individual PRs. Future high-confidence PRs should verify auto-merge is toggled on.
- Wedding is June 12, 4 days away. Post-wedding content updates tracked in issue #74 (deferred). housing-offer-lebanon.md has a June 30 closing date — 22 days away.
- Issue #77 partially resolved (frontmatter date via PR #80) but the domain anchor question (options a/b/c) remains open for Conley.


---

## [2026-06-08] ingest | Claude Code Agent Teams Documentation

**Source type:** Official Anthropic documentation (code.claude.com)
**Pages created:** 1 (`claude-code-agent-teams.md`)
**Pages updated:** 2 (`multi-agent-orchestration.md`, `domain-general.md`)

### What this source contains

The official Anthropic documentation for Claude Code Agent Teams — an experimental feature (v2.1.32+, June 2026) that coordinates multiple Claude Code sessions as a team. One session acts as team lead, spawning teammates that operate as fully independent Claude Code instances with their own context windows. Key differentiator from subagents: teammates communicate directly with each other through a shared mailbox and task list, rather than only reporting back to a parent.

### What changed

- **Created `claude-code-agent-teams.md`** — tool-analysis page covering the full feature: architecture (lead/teammates/task list/mailbox), comparison with subagents, display modes (in-process vs. split panes via tmux/iTerm2), task coordination with dependencies, quality gate hooks (TeammateIdle/TaskCreated/TaskCompleted), plan approval mode, best practices (3–5 teammates, 5–6 tasks each), and known limitations (no session resumption, no nested teams, one team at a time).
- **Updated `multi-agent-orchestration.md`** — added cross-reference noting that agent teams are the first-party implementation of the Fan-Out and Specialist Team patterns.
- **Updated `domain-general.md`** — added new page to the anchor table (11th page in domain).

### Notable observations

- This is the first official Anthropic tool documentation captured in the vault. Previous Claude-related pages (`opus-4-7-workflow`, `gstack`, `multi-agent-orchestration`) were community-sourced threads and guides. Having primary documentation raises the signal-to-noise quality of the AI tooling knowledge in the vault.
- Agent teams are a direct implementation of Patterns 2 and 3 from `[[multi-agent-orchestration]]` — the competing-hypotheses debugging example is particularly noteworthy as an adversarial variant of Fan-Out.
- The shared task list with dependencies mirrors project management conventions used in Conley's own GitHub Projects boards (Now/Next/Later with dependencies). The architectural parallel is worth noting.
- **Practical relevance to Conley's stack:** Claude Code is the primary development tool for both DailyChew and The Grind. Agent teams could accelerate cross-layer work (frontend + backend + tests) once the feature stabilizes past experimental. The token cost constraint is real — each teammate is a full Claude instance, which matters for Conley's budget-constrained quota.
- The CLAUDE.md propagation behavior (teammates read CLAUDE.md from the working directory) means any team working on vault-related or product-related code would automatically inherit the operating contracts.
