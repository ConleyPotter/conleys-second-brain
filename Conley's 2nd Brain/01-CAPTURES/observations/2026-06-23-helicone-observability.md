---
type: observation
tags: [dailychew, shipping, observability, cost]
created: 2026-06-23
source: dev-event
---

Wired Helicone observability into every LLM and TTS call in DailyChew — 6 pipeline nodes, memory extraction, and the conversation layer. Every call is tagged with user_id and node name, so I can slice cost per-user and per-model without building custom tracking. Caching is on for non-personalized nodes (source gathering, quality gate, eval) and explicitly off for personalized ones (script writer, conversation, TTS). The fallback system is visible too — when Claude goes down and GPT picks up, Helicone shows exactly which calls fell back. 57 tests covering header correctness and routing. Free tier for now.
