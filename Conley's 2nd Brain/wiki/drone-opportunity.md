---
type: project
domain: general
tags: [defense-tech, drone, startup, research, hardware]
created: 2026-04-24
updated: 2026-04-24
sources:
  - compass_artifact_wf-cf062d2d-8ed4-460c-a460-02e0262b03b7_text_markdown.md
  - Questions & Notes on the Disposable Drone Research Document.md
---

# Drone Opportunity — Disposable Infantry UAS

**Related:** [[conley-potter]], [[operating-doctrine-2026]], [[the-river-room]], [[the-sentinel]]

---

> **Note:** This page documents Conley's active research into a potential defense hardware venture. Status as of April 2026: early-stage exploration with an identified collaborator ("Sam"). No capital committed. This is parallel to ACE and BA; it falls outside the 2026 operating doctrine's "consolidate on ACE and BA" mandate, so it is flagged as a significant decision point.

---

## The Founding Thesis

The US Department of Defense has publicly committed to placing a drone in every US Army squad by end of FY2026. The industrial base to fulfill that commitment does not exist. The gap is real, enormous, and currently being underserved.

**The specific white space:** A software-forward, modular, disposable infantry drone with a US-compliant (NDAA) component stack, optimized for $500–$2,000 all-in unit economics at 100K+ units/year, is the most pressing missing product in the current defense landscape.

Key numbers (from the April 2026 research document):
- Army plans to procure 1 million drones over 2–3 years, rising to "half a million to millions" annually — from ~50,000 today (10–20× production expansion requirement)
- US produces ~10,000–20,000 defense-grade Group 1 systems/month across all vendors
- Every squad armed with OWA drone by end FY26 requires ~50,000+/month steady-state
- TAM: $450M/year at $1,500 ASP × 300K units (Army alone); $1.25B/year at $2,500 ASP × 500K units across services and allies

---

## The Collaborator Signal

Conley's notes on the research document include a direct message to a collaborator named "Sam":

> "For Sam: I think that the plans you sent me only included an ISR variant. Will our first model offer OWA & decoy nose-cap variants?"

This is the most significant signal in the source. "Sam" has apparently shared preliminary design plans. The question about "our first model" confirms active co-founder-level collaboration, not passive interest. Sam appears to have a hardware/engineering background (sending design plans for an ISR drone variant).

> **Open question:** Who is Sam? What is their background? Is this a formal engagement or exploratory conversation? The answer to these questions determines how seriously this project should be tracked.

---

## Market Context

**Why now (April 2026):**
- Secretary Hegseth's "Unleashing US Military Drone Dominance" memo (July 2025) and the Drone Dominance Program ($1B, 300K drones, targets 30K delivered by July 2026) signal the largest structural shift in US small-unit procurement since the rifled musket
- Blue UAS list transitioned to DCMA (December 2025) — new certification pathway open
- a16z $1.176B American Dynamism fund deploying into defense hardware
- Three years of Ukraine combat data provide requirements written "in blood" — no speculation needed about what the product needs to do

**The cost gap:**
- Ukrainian FPV (disposable one-way attack): $400–$500 BOM at 100K+/month production
- US Switchblade 300 (the current squad-level OWA): $60,000–$80,000/unit
- Target for a new entrant: $800–$1,800 ASP with NDAA-compliant components

**Comparable companies:**
- Neros Technologies (El Segundo) — closest analog; FPV-class, on Blue UAS list, 1,500–2,000 units/month mid-2025. $10.9M seed (Sequoia), $35M Series A.
- Performance Drone Works (PDW) — Huntsville; 350 C100/month + 5,000 FPV/month target; $110M Series B (March 2026)
- Skydio — ISR-focused (X10D, $17,300/unit); not an FPV/OWA competitor
- Anduril — premium systems integrator; not in the disposable segment

---

## Proposed Product Architecture

Per the research document, a new entrant in the disposable segment should:

1. **Pick 2–3 use cases sharing a common airframe** — e.g., ISR quadcopter + OWA FPV + decoy nosecap variant. SKU consolidation drives volume.
2. **Build NDAA-compliant from day one** — NDAA §848 + American Security Drone Act (fully enforced Dec 22, 2025) bar federal procurement of drones with covered Chinese components. NDAA-compliant BOM adds ~$300–$400 over Chinese components but is non-negotiable for DoD sales.
3. **Adopt Auterion Skynode or ARK Electronics flight controller** — Open PX4-based stack; most credible "Android for drones" foundation.
4. **Price to scale** — $1,500 at 1K units/year → $1,100 at 10K → $800 at 100K. Design for manufacturability from day one.

**Reference NDAA-compliant BOM (estimated $600–$900 at volume):**
- Motors: Vertiq, KDE Direct, or Dynamic Aerospace Systems (not T-Motor)
- Batteries: Amprius silicon-anode (US) or Panasonic/LG Energy Solution (not CATL/BYD)
- Flight controller: Auterion Skynode S/X, ARK Electronics, CubePilot Orange+
- Compute: Nvidia Jetson Orin (US-made at TSMC)
- Radios: Doodle Labs RM-2025 Mesh Rider, Silvus StreamCaster
- Cameras: Sony (Japan), Teledyne FLIR for thermal

---

## Go-to-Market Sequence (if building)

1. **Year 0–1 (pre-seed → seed):** Build team (technical + defense-domain + operator). Prototype. Win SBIR Phase I via SOFWERX (~$250K, 6 months). Demo at SOFIC (Tampa) or AUSA. Raise $3M–$7M seed from American Dynamism / Shield Capital / Lux.
2. **Year 1–2:** SBIR Phase II ($2M). OTA prototype via DIU CSO ($5M–$15M). Blue UAS certification (6–18 months). First Ukraine trial. Ship 5,000–20,000 units. Series A $25M–$50M at $100M–$250M post.
3. **Year 2–3:** OTA production follow-on. Blue UAS Select List. Formal multi-service pilots. FMS to NATO partners. Ship 50,000–150,000 units. Series B $75M–$150M.

---

## Funding Landscape

Defense VC checks available now (April 2026):
- Pre-seed: $500K–$2M on $8M–$15M post
- Seed: $3M–$10M on $20M–$50M post (Neros seed: $10.9M at ~$40M post implied)
- Series A: $20M–$50M on $80M–$250M post (Neros $35M)
- Key funds: a16z American Dynamism ($1.176B deployed), Founders Fund, Lux Capital, 8VC, Shield Capital, Sequoia (backed Neros), In-Q-Tel

SBIR non-dilutive fuel: Phase I up to $314K (6 months), Phase II up to $2M (24 months), Phase III uncapped sole-source.

---

## Implications for Conley's 2026 Doctrine

This project represents a significant tension with the 2026 operating doctrine, which explicitly calls for consolidation on ACE and BA with no new project additions.

**What makes this different from a standard new-project distraction:**
- It has an active collaborator (Sam) who has already sent design plans — this is not speculative
- The market window is genuinely time-sensitive; the DoD procurement surge has a window
- The founding team thesis requires three archetypes: technical/CTO + commercial/defense-fluent CEO + operator/veteran advisor. Conley's profile (marketing systems, pipelines, business development) fits the commercial CEO role closely.

**What makes it risky to pursue in 2026:**
- Hardware + defense = multi-year capital-intensive path; ACE is designed to generate capital in months
- Requires all-in attention from a team; the 15-hour/week ACE constraint doesn't translate to a defense startup
- No BA/ACE overlap — this would be a third parallel thread

**Decision flag:** This project needs a formal go/no-go decision against the 2026 doctrine decision filter before further investment of time. The right question is not "is the opportunity real?" (it is) — but "is this the right year, and can the right team be assembled without Conley being the primary driver?"

---

## Open Questions

1. Who is Sam, and what is their background (hardware engineering? defense domain? both)?
2. What specific variant design plans has Sam shared? Are they for a Group 1 ISR quadcopter, OWA FPV, or both?
3. What is the current stage of the collaboration — exploratory conversation or active co-founder formation?
4. Is Conley pursuing this as a co-founder (operational role) or as an advisor/investor?
5. Does this require a go/no-go against the 2026 doctrine, or is Conley treating it as pre-commitment research?
