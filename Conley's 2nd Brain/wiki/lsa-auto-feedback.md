---
type: project
domain: ba
tags: [autoboost, lsa, lead-feedback, pipeline, automation, google-ads, deepgram, haiku]
created: 2026-06-08
updated: 2026-06-08
sources: [lsa-auto-feedback-description-2026-06-08.md]
---

# lsa-auto-feedback — Automated LSA Lead Feedback Pipeline

**Related:** [[ba-overview]], [[ba-products]], [[ab-lead-classifier]], [[autoboost-vault-skills]]

---

## What It Is

An internal AutoBoost engineering project that automates the review and rating of Google Local Services Ads (LSA) call leads. The pipeline replaces manual human review of call recordings with an end-to-end automated flow: pull leads, download recordings, transcribe, classify, and submit structured feedback back to Google.

The feedback is a 5-point survey rating plus a reason string, submitted via `ProvideLeadFeedback()`. This directly shapes the quality of leads Google sends to each client — good feedback trains better lead matching; bad feedback (especially false negatives on legitimate leads) actively harms a client's account.

---

## Pipeline Architecture

Five steps, end to end:

1. **Pull new call leads** from the Google Ads API
2. **Download the call recording audio** for each lead
3. **Transcribe** the audio with Deepgram (speech-to-text)
4. **Classify lead quality** with Claude Haiku (`claude-haiku-4-5`)
5. **Submit the 5-point survey rating + reason** back to LSA via `ProvideLeadFeedback()`

---

## Client Scope

Only clients on the **Advanced LSA tier** ($599/mo, $399 onboarding — see [[ba-products]]) are processed. The tier filter is sourced from HubSpot. The pipeline never runs against all accounts in the MCC.

This aligns with [[ba-products]]'s LSA tier structure: Standard LSA ($199/mo) provides basic lead management; Advanced LSA adds active lead rating, call recording review, and detailed call notes to train Google's LSA algorithm. The `lsa-auto-feedback` pipeline automates the core Advanced-tier deliverable.

---

## Confidence Pipeline (Sub-Component)

The classification step (step 4) has a confidence-gated architecture layered on top to prevent harmful auto-submissions. See [[ab-lead-classifier]] for full detail:

- **Self-consistency sampling** with Claude Haiku — N runs at temperature > 0, measure vote agreement
- **Three-way routing:** `AUTO_SUBMIT` (high confidence) / `HUMAN_REVIEW` (uncertain or dissatisfied-direction) / `DROP` (no usable transcript)
- **North-star metrics** targeting non-inferiority to human reviewers (binary agreement ≥ 0.95, dissatisfied precision ≥ 0.98, Cohen's kappa ≥ 0.70)
- **Gold-set evaluation harness** for threshold calibration, with a human-review flywheel that continuously refines the ground truth

---

## Technology Stack

| Component | Technology |
|---|---|
| Lead data source | Google Ads API (LSA leads) |
| Audio download | Google Ads API (call recordings) |
| Speech-to-text | Deepgram |
| Lead classification | Claude Haiku (`claude-haiku-4-5`) |
| Confidence gating | Self-consistency sampling + abstain routing |
| Feedback submission | `ProvideLeadFeedback()` (Google Ads API) |
| Client filtering | HubSpot (Advanced LSA tier check) |
| Review queue | Local DB (transcripts are PII — never exported unredacted) |

---

## Why It Matters

This is Conley's first major automation initiative at BA that bridges his AI/systems skills with the agency's core service delivery. The pipeline automates the most labor-intensive part of the Advanced LSA product — manually listening to and rating every call recording — while maintaining the quality bar through the confidence pipeline's human-in-the-loop safety net.

The lead feedback loop is strategically important: it directly controls what leads Google sends to BA's clients. Better feedback → better leads → better client outcomes → stronger retention → higher LTV per client.

> **Note:** The project name `lsa-auto-feedback` appears to be an internal repo name at AutoBoost. The confidence pipeline engineering spec is documented in [[ab-lead-classifier]]; additional implementation details may arrive as the project progresses.
