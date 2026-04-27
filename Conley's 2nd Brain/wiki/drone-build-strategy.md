---
type: operations
domain: drone-enterprises
tags: [drone-enterprises, defense-tech, UAS, hardware, manufacturing, NDAA, Blue-UAS]
created: 2026-04-21
updated: 2026-04-21
sources:
  - compass_artifact_wf-cf062d2d-8ed4-460c-a460-02e0262b03b7_text_markdown.md
---

# Drone Build Strategy

**Related:** [[drone-enterprises]], [[drone-market-analysis]], [[drone-funding-gtm]], [[domain-drone-enterprises]]

---

## Architecture: Hardware + Software + Services

The optimal shape for a new entrant is **vertically integrated on the airframe and flight stack, but open on payloads and C2 integration.** Three reference archetypes:

- **Anduril** — closed-loop hardware + Lattice software, premium margins, $60B valuation (March 2026). Aspirational ceiling.
- **Skydio** — closed hardware, open cloud, mid-market ISR. Blue UAS dominant in Group 1 ISR.
- **Auterion** — pure software ("Android for drones"), $130M Series B at $600M+ valuation, ~$100M ARR.

**Drone Enterprises target:** Neros-style vertically integrated hardware at FPV price points, Auterion-compatible software stack (Skynode + AuterionOS) to minimize NRE and maximize ecosystem leverage, plus a services layer for training and fleet management.

---

## Design Principles (Non-Negotiables)

**(a) Modularity.** Single flight-stack platform powering 3+ SKUs (ISR, OWA, decoy) via swappable payload pucks. Standardized power/data connector (SMBus + USB-C-PD or an internally-defined open spec).

**(b) Repairability.** Tool-free battery swap. ESC/motor replaceable in <5 minutes in the field. Modular airframe sections held by captive screws. Accept throwaway economics on frames below $200.

**(c) Open APIs.** MAVLink + REST API for mission planning. ATAK plugin for C2. Publicly documented payload integration to attract third-party ecosystem. MOSA compliance per 10 U.S.C. §4401(c).

**(d) Autonomy tiers.** Manual → assisted → autonomous GPS-denied terminal guidance via visual-inertial odometry. At least one onboard Jetson Orin Nano or Qualcomm RB5 variant.

**(e) EW resilience.** Fiber-optic tether option (like Russian fiber FPVs — physically immune to jamming). Frequency-hopping MANET mesh. Inertial terminal guidance (last 500m unjammable via visual-inertial or acoustic homing). See [[drone-market-analysis]] for EW context.

---

## NDAA Compliance — What It Means

> **What does NDAA-compliant mean?** The National Defense Authorization Act (NDAA) §848 (FY20) plus the American Security Drone Act (FY24) prohibit the US Department of Defense and all federal agencies from buying drones that contain components from "covered foreign countries" (primarily China). These laws focus on *communication-capable* components: flight controllers, radios, cameras, gimbals, ground control stations, and software. A drone using Chinese-made T-Motor motors technically complies today (motors aren't communication-capable) but the DoD is tightening definitions over time. Building NDAA-compliant from day one — including motors, batteries, and PCBs — is the stronger long-term position and is required for Blue UAS certification.

**Full Blue UAS certification** takes 6–12 months and approximately $500K all-in. Since December 3, 2025, certification is managed by DCMA (US-X, Col. Dustin Thomas, Palmdale, CA) via third-party "Recognized Assessors." Blue UAS certification unlocks federal Government Purchase Card buys (up to $10K per transaction, no contract needed) and near-automatic consideration for service sUAS contracts. **Getting on Blue UAS is an explicit Series A milestone.**

---

## Reference BOM (NDAA-Compliant Stack)

| Component | Compliant Option | Notes |
|---|---|---|
| Motors | Vertiq, KDE Direct, Dynamic Aerospace Systems | Avoid T-Motor |
| Batteries | Amprius (silicon anode, US), Panasonic/LG (allied) | Avoid CATL/BYD |
| Flight controller | Auterion Skynode S or X, ARK Electronics, CubePilot Orange+ | Skynode preferred for software integration |
| Compute | Nvidia Jetson Orin Nano | TSMC-fab, OK per CHIPS Act rules |
| Cameras | Sony (Japan), Teledyne FLIR (thermal) | |
| Radios | Doodle Labs RM-2025 Mesh Rider, Silvus StreamCaster, Persistent Systems MPU5 | |
| GPS | Locus Lock or u-blox (Swiss) | u-blox is acceptable; not covered by NDAA |
| Carbon fiber frame | Toray or Mitsubishi Rayon via US fabricators | |

**Resulting BOM cost:** ~$600–$900/unit depending on spec (vs. $280–$310 with Chinese parts).

**Unit economics at scale:**
- 1,000/year → ~$1,800 ACV
- 10,000/year → ~$1,200
- 100,000/year → ~$800
- 500,000/year → ~$500

---

## Manufacturing Strategy

**Onshore is the default** — NDAA compliance, political optics, and procurement preference all point here.

**Hub-and-spoke model:**
- One principal US facility (Texas, Arizona, Alabama, Ohio, or Florida — PDW in Huntsville, Neros in El Segundo, Anduril in Columbus are the precedents)
- Allied-shore supplement for cost relief: Mexico (simple subassembly), Poland (European FMS fulfillment), Taiwan (ICs where Samsung/TSMC alternatives exist)
- Contract-manufacturing partners to evaluate: Jabil, Benchmark Electronics, Flex, Sanmina, TT Electronics

**Low-cost-at-scale playbook:** Design for <3-minute end-of-line flying test (PDW and Skydio do 9-minute builds with 550+ QA checkpoints). Design for tool-free assembly. Use standard consumer-grade RC hobby parts where NDAA-permitted. Volume breakpoints to model at each round of CapEx.

**CapEx requirements:** Skydio built 90,000 sq ft Hayward facility; PDW's Drone Factory 01 is 90,000 sq ft targeting 5,000 AM-FPV/month; Neros is building 250,000 sq ft for 1M/year. Rough benchmark: $200M+ CapEx to reach 500K/year capacity.

---

## Open Standards and Regulatory Compliance

**MOSA (Modular Open Systems Approach):** Legally mandatory under 10 U.S.C. §4401(c) for all MDAPs. Relevant open standards: MAVLink, PX4, FACE, SOSA, OpenVPX/VITA, MORA, VICTORY, CMOSS.

**ITAR (International Traffic in Arms Regulations):** Most loitering munitions are ITAR-controlled under USML Category VIII. Armed UAS requires State Department DDTC registration ($3,000/year) and a license for every export. Non-armed ISR may fall under EAR ECCN 9A610 or 9A012 — less burdensome. Register DDTC at incorporation.

**CMMC 2.0 Level 2:** Required for any contractor handling Controlled Unclassified Information. Third-party assessment: ~$100K–$300K and 6–12 months. Required before most SBIR Phase II and OTA contracts.

**Facility Clearance (FCL):** Must be sponsored by an agency or cleared prime. FOCI mitigation required for any non-US investors. Enables classified work that competitors without clearance cannot perform — a meaningful moat at scale.

**FAA:** Part 107 for commercial operations. BVLOS waivers for testing. Remote ID mandatory since March 2024.

---

## Team Composition by Stage

**Seed (~20–30 people):**
- ~12 hardware engineers (mechanical, electrical, RF, aerospace)
- 6 software engineers (embedded, autonomy, fleet management)
- 4 ops/manufacturing
- 2–3 BD/defense

**Series A (~60–100):**
- Add: cleared-personnel security lead (FSO)
- Add: DFM/DFX engineers
- Add: dedicated field support engineers to embed with units

**Series B (~200+):**
- Add: production line management
- Add: 2–3 cleared program managers per major customer
- Add: international sales team for FMS/DCS
- Add: regulatory/compliance leads (ITAR, CMMC)

Veterans at 20%+ of workforce and 60%+ of leadership is the signal DoD acquirers and SOCOM respect. See PDW as precedent: Gen. Tony Thomas (ex-SOCOM) and former DoD CDO David Spirk on the board.

---

## IP and Defensibility

Hardware patents are a weak moat in drones — reverse engineering + Chinese copying is near-frictionless. Real moats stack from:

1. **Software and autonomy** — flight stack, computer vision, EW resilience; protect via trade secret, not patent
2. **Manufacturing process** — DFM automation, assembly speed, process know-how
3. **Fleet telemetry** — data from deployed units enables iteration competitors can't match
4. **Clearance / classified capability** — FCL + cleared personnel enables SCIF work competitors cannot access
5. **Long-term contracts** — POR dependency creates switching cost

Patent hardware only where it directly blocks copycat production (unique payload mechanisms, novel power architectures).

---

## What's Missing in the Market

**"USB-C of drones"** — there is no true open, industry-standard payload/power/data connector spec usable across manufacturers. Auterion's Skynode/AuterionOS is the most credible contender for "Android for drones." Drone Enterprises can either adopt Skynode + extend, or compete with a tighter-integrated stack optimized for the disposable segment. **This architectural decision is the most consequential early call.**
