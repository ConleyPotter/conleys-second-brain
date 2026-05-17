---
type: project
domain: drone-enterprises
tags: [drone-enterprises, defense-tech, UAS, hardware-startup, founding-team]
created: 2026-04-21
updated: 2026-05-17
sources:
  - The disposable drone opportunity - a founder's playbook for infantry-scale UAS.md
  - Questions & Notes on the Disposable Drone Research Document.md
  - Notes on Meeting with Sam Schutt - DENT.md
---

# Drone Enterprises — Company Overview

**Related:** [[domain-drone-enterprises]], [[drone-market-analysis]], [[drone-build-strategy]], [[drone-funding-gtm]], [[sam-schutt]], [[conley-potter]]

---

## The Thesis

The Pentagon has committed to equipping every US Army squad with a drone by end of FY26 — and the US has no industrial base capable of producing them at scale. China's DJI ships more drones in a week than the entire US defense drone sector produces in a year. Ukraine builds 200,000+ FPV drones per month at $400–$500 BOM. The US Switchblade 300 costs $60K–$80K.

**Drone Enterprises fills the gap:** a software-forward, modular, disposable infantry drone company with a US-compliant component stack, optimized for $500–$2,000 all-in unit economics at 100,000+/year volumes. The founding bet is that a company combining Neros-grade hardware cost, Auterion-grade software, and Anduril-grade defense fluency will capture a disproportionate share of a $5B–$15B annual US + allied market for squad-level attritable UAS through 2030.

---

## Founding Team

**Conley Potter — Chief Strategy Officer**  
Brings commercial strategy, systems architecture, and GTM fluency. His background in building automated B2B systems (ACE), managing complex stakeholder relationships at BA, and developing a public voice maps onto: fundraising narrative, GTM strategy, product-market positioning, and government relations. See [[conley-potter]].

**Sam Schutt — [Role TBD]**  
Conley's closest friend and best man at his June 12, 2026 wedding. Sam brings the technical and/or operator pedigree complementing Conley's commercial role. See [[sam-schutt]].

> **Note:** The canonical founding team archetype for a defense hardware startup has three roles: (1) technical founder with autonomous-systems pedigree (ex-SpaceX, Anduril, Skydio), (2) commercial/CEO with defense acquisition fluency (ex-DIU, ex-SOCOM, or equiv.), and (3) operator/advisor with SOCOM/Ranger/Marine credibility. Conley and Sam may fill two of these; the third may need to be recruited or filled by a board advisor.

---

## Product Vision

**Core segment:** Group 1 (<20 lbs) infantry-scale UAS — the most under-produced category in US defense today. No US-made, $500–$1,500, NDAA-compliant FPV/OWA drone exists at 100,000+/month production rate.

**Target use cases (two to three sharing a common airframe+autopilot):**
- Squad-level ISR quadcopter — 30–60 min endurance, EO/IR camera, autonomous waypointing, ATAK integration
- One-way attack (OWA) FPV — AI terminal guidance, GPS-denied operation, 5–15 km range, 0.5–2 kg warhead
- Decoy/saturation variant — ultra-cheap ($200), radar-signature-matched airframe

**Design non-negotiables:**
- Modular payload pucks — one flight stack powering 3+ SKUs via swappable payloads
- NDAA-compliant component stack — US/allied motors, batteries, flight controllers (no T-Motor, no CATL)
- Open APIs: MAVLink, ATAK plugin, documented third-party payload integration, MOSA compliance
- EW resilience: fiber-optic option, frequency-hopping mesh, inertial terminal guidance (unjammable final 500m)
- Attritable reliability spec (90%+, not mil-spec 99.9%) — enables consumer-electronics pricing

---

## Competitive Landscape

The gap is real. Closest comparables:

| Company | Product | Unit Cost | Volume | Gap |
|---|---|---|---|---|
| Neros Technologies | Archer FPV | ~$5K est. | 1,500–2,000/month, ramping to 10K | Blue UAS listed; too expensive |
| PDW | C100 | $60K+ | 350/month + 5K AM-FPV future | Not disposable economics |
| AeroVironment | Switchblade 300 | $60K–$80K | Sub-10K/year | 50–100× too expensive |
| Skydio | X10D | $17,300 | 1,000+/month, 55K total | ISR only, not OWA |

Drone Enterprises targets **$800–$1,500/unit at scale** with a modular architecture that none of the incumbents offer. Neros is the closest threat; their single-SKU approach and current pricing leave the modular/disposable segment open.

---

## Revenue Model (Target at Maturity)

- **60%** unit hardware sales (25–35% gross margin)
- **25%** software/firmware subscription (70%+ gross margin)
- **15%** training/sustainment/spares (50%+ gross margin)
- Blended gross margin target: 45–55% → 60%+ with SaaS expansion

**TAM:** $1,500 blended ASP × 300K units/year = **$450M/year Army alone**. $2,500 including software + allied sales × 500K units = **$1.25B/year**. Lifetime value per fielded unit (hardware + spares + software + training) ~$3,500.

---

## Status (April 2026)

Pre-incorporation. Research phase complete. Founding team forming. No capital raised.

**Immediate next steps:**
1. Finalize founding team composition — recruit or designate technical/operator archetype
2. Register SAM.gov, DUNS/UEI, ITAR/DDTC
3. Build functional prototype; validate BOM at $1,500 target at 1,000 units/year
4. Submit SBIR Phase I to SOFWERX or AFWERX Open Topic (~$250K, 6 months)
5. Demo at SOFIC (Tampa) or AUSA

See [[drone-funding-gtm]] for full roadmap.
