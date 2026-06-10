---
type: observation
tags: [dailychew, shipping, ai-evaluation]
created: 2026-06-09
source: dev-event
---

Landed the post-delivery episode eval system with Gemini as the judge. gemini-3.1-flash-lite scores each episode across 5 dimensions on a 1-4 anchored rubric, with gemini-3.5-flash as escalation for anything scoring 2 or below. Cost is $0.0006 per episode — well under the $0.002 target. The judge is deliberately cross-family from both Claude (script writer) and GPT (source gathering) to dodge self-preference bias. Also satisfies the hackathon's "use Gemini" requirement without being a gimmick — it's a real architectural choice. Cohen's kappa calibration job runs weekly to keep the judge honest against human labels.
