---
type: tool-analysis
tags: [tools, apis, data]
created: 2026-04-14
updated: 2026-04-16
sources: [ACE Business Plan_ Autonomous Freelance Agent.md]
---

# Data Enrichment APIs

**Related:** [[tech-stack]], [[phase-1-lead-enrichment]], [[financial-projections]]

---

## Overview

The profitability of Phase I depends entirely on mastering the unit economics of data enrichment APIs. The market divides into single-source proprietary databases and multi-source "waterfall" orchestration platforms. ACE's decision: build a custom waterfall in n8n using Apollo + Cleanlist to replicate Clay-level functionality at roughly 25% of the cost.

---

## API Vendor Matrix

| API | 2026 Pricing | Strengths | Est. Cost / 1,000 Records | ACE Verdict |
|---|---|---|---|---|
| **Apollo.io** | $49–$99/month | 275M+ database; generous email limits; ~80% email accuracy | $50–$150 | ✅ **Primary layer** — highest raw volume at lowest baseline cost |
| **Cleanlist / Prospeo** | $29–$39/month | Specialized in email deliverability; 98% accuracy; real-time verification | $58–$100 | ✅ **Secondary verification layer** — validates Apollo output, guarantees low bounce rates |
| **Clay** | $149–$185/month | Cascades through 75+ data providers; best data depth; turnkey waterfall | $200–$350+ | ❌ **Avoid in Phase I** — monthly sub + rapid credit burn erodes bootstrapped margins |
| **Lusha** | $29–$52/month | Good European coverage; strong mobile dial accuracy | ~$1,230 | ❌ **Avoid** — 70–480 credits/month cap; ~$1,230/1,000 records is financially unviable for bulk |
| **SyncGTM** | $99/month | Waterfall across 50+ providers; high coverage rates | Tier-dependent | ⚠️ **Strong alternative** — if Apollo hit rates are low for a specific niche |

---

## ACE's Custom Waterfall Architecture

Instead of paying Clay $185–$349/month for pre-built waterfall logic, ACE replicates it in n8n:

1. **Apollo first** — query for email, title, LinkedIn, company size, phone
2. **If Apollo returns low-confidence or blank** → cascade to Cleanlist/Prospeo for email verification
3. **Supabase cache check before either API call** — if domain enriched in last 90 days, skip both APIs

**Total cost:** ~$78/month (Apollo + Cleanlist) vs. $185–$349/month for Clay  
**Accuracy achieved:** 95%+ email deliverability (matching enterprise-grade platforms)

The operator's n8n expertise is what makes this architecture viable. Building the waterfall internally is a skill-based cost advantage, not just a price difference.

---

## Apollo.io — Technical Details

- Database: 275M+ contacts
- Rate limits: 50–200 API calls/minute depending on subscription tier; strict hourly caps
- Phase I configuration: batch size 10–20 rows, Wait node 10–15 seconds between batches
- Error handling: dumping a 5,000-row spreadsheet simultaneously triggers 429 Too Many Requests — batching prevents this
- Outputs: email, job title, LinkedIn URL, company size, direct phone, company revenue range

## Cleanlist / Prospeo — Technical Details

- Specialized in email validation only
- 98% deliverability accuracy; real-time verification
- Used as a cascade: only called when Apollo returns uncertain or missing email
- Pay-per-success model reduces cost on high-confidence Apollo results

---

## The Supabase Cache Effect on API Costs

As volume accumulates:
- Month 1: minimal cache hits; near full API cost per gig
- Month 3: ~20–30% of queries hit cache (repeat domains, returning clients)
- Month 6+: 40–60% cache hit rate on overlapping geographies → COGS drops dramatically

This is why accepting multiple contracts in the same niche geography (e.g., Lancaster County manufacturing) is a compounding competitive advantage. The second client in that niche costs significantly less to serve than the first.
