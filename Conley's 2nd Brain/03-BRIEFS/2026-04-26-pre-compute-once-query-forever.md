---
type: brief
status: ready-to-write
connection: [[2026-04-25-cache-as-compounding-architecture]]
created: 2026-04-26
tags: [ready-to-write, ace, second-brain, compounding, systems]
---

# Brief: Pre-Compute Once, Query Forever

**ONE THING:** Every system that compounds in value is doing the same thing — paying the compute cost once at the source and making every subsequent query near-free — a design decision most people make accidentally, if at all.

**PROOF:** ACE lead enrichment on a $450 contract: 85% net margin on the first run of a Lancaster County geography. 92%+ margin on every cached run after. The 7-point difference is entirely a Supabase deduplication table that costs nothing to query after the first API call. Three months of working the same geography and the margin is nearly permanent. Zero additional work — just time inside a narrow niche.

**READER TRANSFORMATION:** Before: "My system generates results." After: "I can identify every operation in my stack that re-computes the same thing from scratch — and replace each one with a pre-compute-and-store step. That's the only lever that improves margin without adding work or headcount."

---

## Hooks (ranked)

1. **Aggressive** — "You're paying full price every time. Your system should have paid once."
2. **Curious** — "Why does my lead enrichment business get 7% more profitable every month without me changing anything?"
3. **Personal** — "I built the same architecture twice — once by accident and once deliberately. The day I realized they were the same design, I stopped building new systems and started asking which existing ones needed a cache."

---

## Closers (ranked)

1. "Find the thing you're computing from scratch every time. Pay the cost once. Store the result. That's the whole move."
2. "ACE's margins didn't improve because I got better. They improved because the geography stayed the same. The cache compounds. Most businesses don't have one."
3. "The first client in a new niche costs full price. Every one after is cheaper. That's not network effects — that's a cache. Build the cache first."

---

## Source notes
- [[2026-04-25-cache-as-compounding-architecture]]
- [[phase-1-lead-enrichment]]
- [[financial-projections]]
- [[llm-wiki-pattern]]
- [[2026-04-26-supabase-cache-is-a-moat]]
- [[2026-04-26-ace-unit-economics]]
- [[2026-04-26-cache-and-wiki-same-idea]]
