---
type: observation
tags: [dailychew, shipping, infrastructure]
created: 2026-06-09
source: dev-event
---

Migrated DailyChew audio storage from Cloudflare R2 to Google Cloud Storage. Cloudflare keeps denying the billing setup (support ticket still pending), so R2 was a dead end. GCS adds ~$0.001/episode in egress costs that R2 didn't have, but it also checks the "use a Google Cloud product" box for the Gemini XPRIZE hackathon entry. The migration touched tests, mocks, upload methods, signed URL generation, and all the env vars. Four tests broke in the process — source.test.ts and audio/upload.test.ts need cleanup.
