---
type: connection
connection-type: A
sources:
  - phase-1-lead-enrichment.md
  - financial-projections.md
  - llm-wiki-pattern.md
created: 2026-04-25
tags:
  - ace
  - caching
  - second-brain
  - compounding
  - systems-design
---

# Pre-Compute Once, Query Forever

**Bridge:** ACE's Supabase cache strategy and the LLM wiki pattern implement the same architectural principle — pre-compute and store rather than re-compute on demand — and both systems become more valuable over time as overlapping queries hit the cache instead of the source.

**Potential hook:** "My lead enrichment pipeline has a cache that makes the second client in Lancaster County dramatically cheaper to serve than the first. My second brain works the same way. Every new source I ingest touches pages that already exist — the synthesis was paid for on first ingest and is free on every query after. Pre-compute once. Query forever. I built this into ACE accidentally and into the wiki deliberately. Now I see them as the same design."

**Source notes:**
- [[phase-1-lead-enrichment]]
- [[financial-projections]]
- [[llm-wiki-pattern]]

**Why this matters:** The Supabase cache is described in financial terms: "margins approach 85–90% as cache hit rate increases." The LLM wiki pattern is described in knowledge terms: "knowledge compiled once and kept current." They're the same argument. In both cases, the first pass is expensive (API call, reading a raw source); subsequent passes that hit the same data are near-free. In both cases, choosing to operate in a narrow niche (Lancaster County manufacturing; ACE/BA domain) accelerates the compounding — overlapping coverage compounds faster than scattered coverage. The non-obvious extension: this principle should inform how the second brain expands. Adding sources that overlap with existing pages isn't redundancy — it's cache-warming. The second source on a topic makes the wiki answer faster and richer, not bloated.
