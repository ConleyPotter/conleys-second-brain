---
type: observation
tags: [dailychew, shipping, personalization]
created: 2026-06-23
source: dev-event
---

Closed the personalization loop in DailyChew. After a user listens and has a conversation about an episode, the system extracts durable interest signals from that session — topics they cared about, questions they asked, domains they leaned into. Those signals get embedded and stored with weights, then fed back into the Script Writer prompt for the next episode. Near-identical signals merge instead of duplicating (same user, same topic = bump the weight). Cold start falls back to the onboarding profile gracefully. The whole thing fires on an Inngest session/close event and uses GPT-5.4 Nano Batch API to keep extraction costs minimal.
