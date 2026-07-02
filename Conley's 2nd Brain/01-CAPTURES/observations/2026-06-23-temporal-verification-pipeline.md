---
type: observation
tags: [dailychew, shipping, architecture, verification]
created: 2026-06-23
source: dev-event
---

Shipped the full temporal verification pipeline for DailyChew in three stacked PRs over two weeks. The problem: an episode told users GPT-4o "released recently" when it was months old. The fix is a two-stage post-generation gate. First stage is a zero-cost regex scan that catches recency language ("recently," "just," "this week") and checks whether the backing source is actually recent. Second stage is a Haiku-class LLM judge scoring faithfulness and temporal accuracy, with automatic retry-and-feedback before blocking an episode from delivery. Total verification cost is about $0.001 per episode against the $0.24 generation COGS. The generator never grades its own work — the judge is a separate model from a separate provider.
