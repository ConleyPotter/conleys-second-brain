---
type: strategy
tags: [finance, unit-economics]
created: 2026-04-14
updated: 2026-05-06
status: archived
sources: [ACE Business Plan_ Autonomous Freelance Agent.md, ACE Phase 1 Reference Brief.md]
---

> **⚠ ARCHIVED — May 2026.** This page documented ACE's Upwork-based revenue projections (Month 1–6 ramp to $4,025+ net). The freelance arbitrage model has been deprioritized in favor of the Personal Brand Engine — see [[personal-brand-engine]].

# Financial Projections

**Related:** [[ace-overview]], [[phase-1-lead-enrichment]], [[phase-2-content-vectors]], [[phase-3-infrastructure]], [[data-enrichment-apis]]

---

## Monthly OPEX (~$190/month)

| Item                                         | Cost/Month |
| -------------------------------------------- | ---------- |
| VPS (n8n + Apify)                            | ~$12       |
| Apollo.io Basic                              | $49        |
| Cleanlist / Prospeo                          | $29        |
| Upwork Connects (AI-filtered, ~30% win rate) | ~$50       |
| Gemini / Anthropic API tokens                | ~$35       |
| Other (misc tools)                           | ~$15       |
| **Total**                                    | **~$190**  |

---

## Revenue Ramp (Months 1–6)

| Month | Activity | Gross Revenue | Net (after fees + OPEX) |
|---|---|---|---|
| 1 | 4 enrichment gigs @ $150 (system validation) | $600 | ~$350 |
| 2 | 10 enrichment gigs @ $150 (cache building) | $1,500 | ~$1,160 |
| 3 | 10 enrichment + 5 SEO/YT gigs @ $250 (Phase II begins) | $2,750 | ~$2,255 |
| 4–6 | Steady covert volume + 1 RevOps retainer @ $2k/mo | $4,750+ | ~$4,025+ |

Upwork takes ~10% commission. Margins approach 85–90% as Supabase cache matures and API costs per gig drop.

---

## Unit Economics — Lead Enrichment

**Single 500-contact list at $450 (mid-range of $400–600)**

| Item | Value |
|---|---|
| Gross contract value | $450 |
| Upwork commission (10%) | -$45 |
| API COGS (Apollo + Cleanlist, first run) | ~$25–$30 |
| API COGS (repeat geography, cache hits) | ~$5–$10 |
| **Net margin (first run)** | **~85%** |
| **Net margin (cached geography)** | **~92%+** |

The Supabase cache is the primary driver of margin improvement over time. Overlapping geographies and industries compound.

---

## Cost Per Hire (Connects)

- Connects cost: $0.15 each; proposals require 10–20 Connects = $1.50–$3.00 per submission
- Industry average reply rate without targeting: ~5% → CPH ~$192
- ACE target with Gemini scoring gate (8+) and Spartan Tone: 25–35% response rate → CPH <$60
- Win rate assumption: ~30%

**The scoring gate is the key cost control.** Discarding sub-8 jobs before any Connect expenditure is what makes the acquisition economics work.

---

## Campaign Phase I Financial KPIs

- **90-day gross revenue target:** $2,000–$3,000
- **Contract target:** 5 completed contracts with 5-star reviews by July 13, 2026
- **Phase I objective:** Generate 6–12 months of OPEX runway (= $1,140–$2,280)
- **No paid media budget** — all channels are owned or earned

---

## Long-Term Scaling Logic

Because COGS is tied to API calls (computational cycles) rather than human hours, the profit margin is not eroded by volume growth. Adding a 10th simultaneous lead enrichment contract costs approximately the same in API credits as the 1st, but the Supabase cache may already have 40–60% of the required records, dropping COGS further.

The only constraint on scaling is the 15-hour/week operator bandwidth — which is why the transition to RevOps retainers (Phase III) is the highest-leverage end state. Retainer income is largely passive once the underlying system is deployed.
