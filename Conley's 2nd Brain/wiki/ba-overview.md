---
type: operations
domain: ba
tags: [ba, autoboost, day-job, agency, rebrand]
created: 2026-04-16
updated: 2026-06-08
sources: [Claude Accounts' Saved Memories.md, Personal Portfolio Website Current State 4.14.26.md, conley-weekly-summary-apr-6-12-2026.md, Daily-Recap_2026-04-15.md, BA Team Roster.md, Daily-Recap_2026-04-16.md, Daily-Recap_2026-04-20.md, Daily-Recap_2026-04-21.md, ab-lead-classifier-confidence-pipeline-issue-2026-06-08.md]
---

# AutoBoost (formerly Business Actualization) — Day Job Overview

**Related:** [[conley-potter]], [[career-history]], [[ba-products]], [[ba-team]], [[ba-partners]], [[ba-clients-pipeline]], [[operating-doctrine-2026]], [[ab-lead-classifier]]

---

## What It Is

**AutoBoost** (formerly Business Actualization, rebranded recently) is a 13-person digital marketing agency founded in 2001 and headquartered in Palmyra, PA. It specializes exclusively in automotive repair shops — providing websites, paid ads, LSA management, review platforms, call tracking, and revenue attribution to independent and multi-location shop owners across the US. Founded by Adam Kushner.

AutoBoost is the company name, not a standalone SaaS product. The suite of client-facing software platforms (review management, call tracking, revenue attribution) are bundled into service delivery — white-labeled tools, not independently sold software. The positioning is marketing agency + platform bundle, not SaaS in the way competitors like Kukui are. Conley appears heavily in AutoBoost's video content (in-house studio) and has explored a future CEO trajectory with Adam.

**ARR:** ~$2.5M

---

## Conley's Role

**Formal title:** Project Manager (Digital Marketing)  
**Functional title:** Director of Client Success & Strategy (absorbing a departed director's duties; title alignment in progress)  
**Portfolio title:** Client Success & Growth Leader

In practice the role is a hybrid of sales, client success, and internal systems work. Conley runs and covers client calls, manages a HubSpot pipeline, drives partner relationships (AutoVitals, Turnkey), and coordinates internally across sales, delivery, and ops.

**Active BA workstreams (as of early 2026):**
- Building Cowork skill ecosystem for AutoBoost account management workflows
- DNS/hosting infrastructure projects (Route 53, CloudFront, GoDaddy)
- n8n automation exploration (HubSpot call → Claude summary → HubSpot note is identified highest near-term priority)
- Director title alignment in progress — the April 2026 FLSA compliance incident (29 C.F.R. § 785.37) is a documented example of the behavior supporting that case
- Confidence-gated lead classifier pipeline — Haiku-based classifier for Google Ads lead feedback with self-consistency scoring, human-in-the-loop review queue, and gold-set eval harness (see [[ab-lead-classifier]])

**On the flatarchy proposal:** Dropped as a formal initiative, though concepts from the investigation (pod structure, formalized leadership tiers) may resurface as AutoBoost formalizes its org structure over the coming months.

**Director role context:** Conley has been performing Director-level duties for 2+ months — absorbing client success and strategy responsibilities on top of the PM role. The formal title change would be recognition and authority, not a function change. Concrete delta from current PM title:
- Official ownership of client retention, satisfaction, and escalation decisions (currently performed without title authority)
- Seat at the leadership table alongside Adam and Micah in the three-person leadership structure
- Internal authority over service delivery standards, pod structure, and client onboarding — currently shaped informally
- Compensation alignment: market range $85K–$120K base (central PA corridor runs 15–20% below national median for marketing roles)

---

## Role in the 2026 Operating Doctrine

Per [[operating-doctrine-2026]], BA is designated as the **income foundation** — Conley's primary, compounding income engine. No exit planned in 2026 or likely 2027. Professional alignment and reputation at BA are protected at all times.

This means:
- All public work (ACE, Building Out Loud, portfolio) must remain clearly non-competitive with BA
- BA client relationships are never referenced publicly
- The LinkedIn identity is BA-only; ACE never surfaces there

The day job is not background noise. A single day (Apr 15) included 6 substantive HubSpot calls, 5+ outbound client emails, and sustained multi-thread Slack coordination. The operating doctrine's stability-as-platform framing is literal — BA generates the financial floor from which ACE is built.

---

## Services Overview

BA's service catalog covers the full digital marketing stack for automotive shops. See [[ba-products]] for tier detail.

**Core service categories:**
- Websites (Standard tier, custom builds)
- Google Ads (Jumpstart, Jumpstart+, Standard tiers)
- Local Service Ads / LSA (Standard and Advanced management tiers)
- Programmatic advertising
- Enhanced SEO and listing management
- Review platform and reputation management
- Call tracking
- Social content curation
- Video marketing
- Revenue attribution (Gauge integration)
- Email marketing
- Geographic exclusivity offered to clients

---

## Partner Ecosystem

Two primary referral and co-delivery channels. See [[ba-partners]] for full detail.

- **Turnkey Auto Marketing** — sends BA referrals; BA manages LSA for Turnkey's prospects
- **AutoVitals** — shared client base; joint calls, co-managed Google Ads and LSA accounts, billing coordination

**Industry conferences:** BA exhibits at automotive industry conferences. Adam and Jon attended TEKTONIC (Houston) the week of Apr 6–12. Conley traveled solo to **FLACA (Florida Automotive Community Association)** in Orlando, Apr 16–19, 2026, for exhibitor booth staffing and networking. Conley returned to the Palmyra office Monday Apr 20. Next: TOOLS 2026 (Conley attending; booth space TBD with Adam). These events are an active part of BA's business development motion.

---

## Internal Team

See [[ba-team]] for roles and working relationships.

**Key people:** Adam Kushner (Founder & CEO), Jon Fonner (Google Ads Lead), Micah Dilts (Acting COO), Conley Potter (Digital Marketing Project Manager / de facto Director of Client Success & Strategy), Adam Hicks (Paid Media Specialist), Abby Steele (Digital Marketing), Courtney Nguyen (Content Strategist), Van Nguyen (Content/Creative, part-time remote), Kyle Sarnowski (Video Production Associate), Ethan Wauls (Analytics), Josh Carson (Lead Software Engineer), Daniel Tobias (Junior SE), Jahson Gonzalez-Allie (Junior SE).

---

## Tooling

- **HubSpot** — CRM and pipeline tracking. Conley works in HubSpot daily: creating deals, logging calls, managing follow-up tasks, tracking deal stages (Decision Maker Bought-In → Contract Sent → Closed Won).
- **Hubstaff** — Time tracking. Conley logs ~7 hours/day.
- **Slack** — Primary internal comms. Key channels: `#internal-sales`, `#internal-google-ads`, `#internal-websites`, per-client channels (format: `#clients-[shop-name]`), AutoVitals workspace.
- **Gauge** — Analytics/attribution platform. Biweekly maintenance windows (Josh-organized). Revenue attribution dashboard used in client reporting.
- **CallRail** — Call tracking; GCLID capture for Google Ads conversion tracking.
- **Google Ads, Performance Max, LSA** — Core paid media stack for clients.
- **HubSpot AI (post-call summaries)** — Conley confirmed using HubSpot's AI features after calls to auto-generate notes. As of Apr 16, Micah confirmed the new HubSpot beta features (subtasks, improved task objects, enhanced workflows) can replace the existing "assign to client success" workflow entirely. Conley and Micah aligned on its value; Courtney skeptical of UI changes.

**Service delivery platforms (client-facing, managed by BA):**
- **Google Ads, Performance Max, LSA** — core paid media stack
- **Meta, Reddit, Bing, Programmatic** — extended ad channels
- **Duda** — website platform for all client sites
- **Agency Analytics** — client reporting dashboards
- **Birdeye** (white-labeled as BA's review platform) — reputation management
- **CallRail** (white-labeled as BA's call tracking product) — call tracking + GCLID capture for conversion attribution
- **GoDaddy → AWS Route 53 → CloudFront/ACM** — DNS/hosting/SSL pipeline for client websites

**Internal ops stack:**
- **HubSpot** — CRM + pipeline (Conley's daily environment); call tracking context
- **Slack** — primary internal comms
- **Google Workspace** — docs, drive, email
- **Hubstaff** — time tracking
- **n8n** — automation layer (BA use, distinct from ACE)
- **Anthropic API / Claude / Cowork** — AI-assisted workflows. BA org hit its monthly Claude Teams usage cap on Apr 21, 2026 — a signal of heavy team adoption.
- **Viktor** — new AI assistant deployed at AutoBoost (as of Apr 2026). Conley first used Apr 21 to pull Google Ads metrics from the MCC (hundreds of accounts) ahead of client calls. Integrated via Pipedream (Zoom app request pending Adam's approval). The team's assessment: "pretty dang smart for a clanker."
- **Notion** — Conley uses it; not standard across the team

**Platform changes to watch:**
- **DSA deprecation (Apr 21, 2026):** Google officially announced that Dynamic Search Ads (DSA) legacy capabilities are being deprecated, with all functionality migrating into AI Max for Search campaigns. Affects client campaigns currently using DSA setups.

---

## Revenue and Scale Signals

From the Apr 6–12 weekly summary:
- **~20 client meetings in one week** across three calendars (Conley's, Jon's, client success)
- **3 new HubSpot deals created** that week
- **3 deals closed-won** totaling **~$29,610** in which Conley had commission credit
- Conley carried Thursday and Friday client calls solo while Adam and Jon were at TEKTONIC Conference in Houston

This suggests BA operates at meaningful scale — enough deal volume that a single week of strong closing ($29K attributable) is notable but not exceptional. At $2.5M ARR, the agency is solidly mid-market for a vertical-specialized shop.
