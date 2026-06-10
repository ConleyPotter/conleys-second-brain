---
type: observation
tags: [dailychew, shipping, model-selection]
created: 2026-06-09
source: dev-event
---

Swapped the DailyChew script writer from Claude Sonnet 4.6 Batch to gpt-4.1. The pipeline now uses four different model families across its six nodes: GPT-5.4 Nano for source gathering and quality scoring, gpt-4.1 for script writing, gpt-4o-mini-tts for audio, and Gemini for post-delivery eval. Plus Claude for the conversation layer. Five providers in one product. The multi-model harness isn't a design philosophy — it's what happens when you pick the best tool for each job and don't lock yourself to one vendor.
