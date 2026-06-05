---
type: observation
tags: [dailychew, shipping, backend, pipeline]
created: 2026-06-05
source: dev-event
---

DailyChew's episode generation pipeline is feature-complete. Six nodes: source gathering from Exa, script writing via Claude Sonnet 4.6 Batch (50% cost reduction), a quality gate that kills bad episodes before they reach TTS, reflection question generation, text-to-speech on gpt-4o-mini-tts with R2 upload, and delivery prep that tracks audio file size in bytes for COGS. The whole thing runs on Inngest with retries and concurrency limits, not n8n — that was the strategy doc's plan but Inngest won in practice. 198 unit tests, zero live API calls in the test suite. The core loop (generate, listen, chat, get notified) has backend coverage end-to-end. No live episodes generated yet.
