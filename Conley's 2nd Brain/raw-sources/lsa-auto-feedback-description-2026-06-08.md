# lsa-auto-feedback

Automated Google Local Services Ads (LSA) lead feedback pipeline. Replaces manual human review by:

1. Pulling new call leads from the Google Ads API
2. Downloading the call recording audio
3. Transcribing it with Deepgram
4. Classifying lead quality with Claude Haiku
5. Submitting the 5-point survey rating + reason back to LSA via `ProvideLeadFeedback()`

Only clients on the **Advanced** LSA tier (sourced from HubSpot) are processed — the pipeline never runs against all accounts in the MCC.

---

*Captured from Conley's email, June 8, 2026. Context: "This is the LSA/lead project I'm working on at work (AB/BA)"*
