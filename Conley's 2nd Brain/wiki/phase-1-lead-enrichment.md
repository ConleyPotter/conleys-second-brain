---
type: operations
domain: ace
tags: [phase-1, operations, fulfillment]
created: 2026-04-14
updated: 2026-05-06
status: archived
sources: [ACE Business Plan_ Autonomous Freelance Agent.md, ACE Phase 1 Reference Brief.md]
---

> **⚠ ARCHIVED — May 2026.** This page documented the Phase I B2B lead enrichment pipeline (Apollo + Cleanlist + Supabase), which was designed but never built. ACE has been pivoted to the Personal Brand Engine — see [[personal-brand-engine]].

# Phase I — B2B Lead Enrichment

**Related:** [[ace-overview]], [[tech-stack]], [[client-acquisition]], [[data-enrichment-apis]], [[financial-projections]], [[upwork-portfolio]]

---

## Why Lead Enrichment First

Phase I focuses exclusively on B2B lead enrichment for three structural reasons:

1. **Deterministic deliverable** — the output is a structured CSV. No subjective client feedback, no scope creep.
2. **Fully automatable** — the pipeline is: domain → Apollo → Cleanlist → Supabase → Google Sheet. No judgment required.
3. **Infinite horizontal scalability** — accept 10 identical contracts simultaneously at zero marginal COGS increase.

The arbitrage works because clients pay for perceived days of manual labor. For a human, cross-referencing 500 prospects against LinkedIn, guessing email formats, and verifying deliverability takes dozens of hours. For the ACE pipeline, a 500-row list completes in under 15 minutes unattended.

---

## Target Micro-Niche

**Lancaster County, PA — Manufacturing and Industrial Firms**

The operator (Conley Potter, based in Palmyra, PA) targets this niche for geographic proximity and market density:
- Manufacturing = 16%+ of Lancaster County jobs
- Key anchor employers: Dart Container Corporation, Armstrong World Industries, Arconic US LLC; industrial parks along I-83 corridor
- Average Cost Per Qualified Lead (CPQL) in manufacturing: ~$341 — makes a $400–600 verified list an obvious buy for local B2B agencies

**Decision-maker titles to enrich:**
- Procurement Manager
- Plant Director
- VP of Operations

**Pricing:** 500-contact verified lists at $400–600 fixed price. COGS = <$30 in API credits. Margin ≈ 95%.

---

## Fulfillment Pipeline

| Step | Tool | Detail |
|---|---|---|
| 1. Ingest | Google Sheets Trigger / Webhook | Client provides raw CSV or Google Sheet of domains/company names |
| 2. Cache Check | Supabase PostgreSQL | Was this domain enriched in the last 90 days? Hit → free. Miss → call Apollo |
| 3. Enrich | Apollo.io API | Returns: email, title, LinkedIn, company size, phone. Batch: 10–20 rows, Wait: 10–15s between batches |
| 4. Verify | Cleanlist / Prospeo API | Validates email deliverability. Cascades here only if Apollo returns low-confidence result |
| 5. Sanitize | Gemini node | Normalizes company names — removes LLC/GmbH, fixes ALL-CAPS. Output looks hand-cleaned |
| 6. Write Back | Google Sheets node | Appends enriched rows to formatted output sheet |
| 7. Deliver | Slack → Operator | Delivery message queued in Slack #new-upwork-gigs for operator approval |

**Rate limiting:** Apollo enforces 50–200 calls/minute. Split In Batches (size: 10–20) + Wait node (10–15s) keeps well below threshold.

---

## The Supabase Cache Strategy

Every unnecessary Apollo call costs money. The Supabase cache layer:
- Checks domain against PostgreSQL before any external API call
- Cache hit = free; cache miss = API call + write-back to Supabase
- 90-day TTL on records
- Over months of operation, builds a proprietary, zero-cost data lake
- Margins approach 85–90% as cache hit rate increases and COGS per gig drops

This is why accepting multiple enrichment gigs in overlapping geographies is a compounding advantage — the second client in Lancaster County costs dramatically less to serve than the first.

---

## Phase I Operating Rules

- NEVER disclose automation to clients. They must believe fulfillment is manual.
- NEVER skip the Supabase cache check — every unnecessary Apollo call costs money.
- NEVER use batch sizes above 20 on Apollo without verifying the account's rate limit tier.
- ALWAYS route n8n workflow errors to the dedicated Slack error channel.
- ALWAYS enable 'Continue On Fail' on non-critical enrichment nodes (e.g., LinkedIn URL lookup).

---

## Phase I KPIs

- **Revenue target:** $2,000–$3,000 gross in 90 days
- **Contract target:** 5 completed Upwork contracts with 5-star reviews by Day 90 (July 13, 2026)
- **Margin target:** ≥85% net (as Supabase cache matures)
- **Phase I objective:** Secure 6–12 months of OPEX runway before expanding to Phase II

See [[financial-projections]] for monthly revenue model. See [[upwork-portfolio]] for proof-of-concept spec project.
