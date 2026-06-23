---
type: observation
tags: [dailychew, shipping, resilience, architecture]
created: 2026-06-23
source: dev-event
---

Built inference-crunch resilience into DailyChew so episodes still generate when Anthropic is saturated. The system detects 429s, 529s, and timeouts as failover triggers, switches from Claude to GPT automatically, and trips a circuit breaker after repeated failures so it stops hammering the primary. Auto-recovers after a cooldown window. Every generated script is now tagged with which model actually produced it, so the eval system can compare fallback episode quality against primary. All model IDs extracted to a single config module — no more hardcoded strings scattered across the pipeline. 48 tests.
