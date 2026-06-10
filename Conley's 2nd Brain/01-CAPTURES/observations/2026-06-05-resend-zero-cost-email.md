---
type: observation
tags: [dailychew, shipping, cost, architecture]
created: 2026-06-05
source: dev-event
---

Picked Resend over SendGrid for DailyChew's transactional email (ADR-0004). The deciding factor was not price — both are $20/month at 50k emails. It was developer experience: TypeScript-native SDK, one-line send call, React Email templates that live as .tsx files in the repo and preview locally. The free tier (3,000/month) covers the entire early beta at $0 marginal cost. One email per user per day at launch means the first 100 daily active users cost nothing on email. Revisit trigger is deliverability below 95% or DAU above 10,000.
