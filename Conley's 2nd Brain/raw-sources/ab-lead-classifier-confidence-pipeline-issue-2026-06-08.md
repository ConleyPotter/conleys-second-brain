# Confidence-Gated Lead Classifier Pipeline — AutoBoost Internal Issue

**Source:** GitHub issue on AutoBoost (AB) internal repo, shared by Conley via email 2026-06-08
**Type:** Engineering design document / issue specification

---

## Problem

The pipeline submits a 5-point `SurveyAnswer` + reason to Google via
`ProvideLeadFeedback()`. That feedback is not a passive label — it feeds
Google's per-advertiser lead matching and the credit/dispute system. The
dominant risk is **confident misclassification** (more than strict
hallucination): a wrong rating from an ambiguous or mis-transcribed call.
Systematic error is worse than random here — it biases Google's matching
and can hurt clients' lead quality and standing. STT errors stacking on LLM
errors, plus Haiku being the smallest model, make this a real risk on hard
calls.

LLM error **cannot be driven to zero**. So the goal is not "eliminate
hallucination" — it's **bound the error, contain the harmful direction,
route uncertain cases to a human, and measure against the human-reviewer
baseline.**

## Approach

The Anthropic Messages API exposes **no token logprobs**, so confidence
comes from **self-consistency** (sample the Haiku classifier N times at
`temperature>0`, measure vote agreement) blended with the model's
self-reported confidence and gated by STT quality. A scorer routes each
lead:

```
AUTO_SUBMIT   confidence ≥ threshold AND quality gate passes → batched
ProvideLeadFeedback
HUMAN_REVIEW  below threshold / dissatisfied direction / low STT quality →
review_queue
DROP          no usable transcript → never submitted
```

The dissatisfied/dispute direction carries a **higher precision bar** (it's
the one that can harm a client or a real customer). A **gold-set eval
harness** calibrates the thresholds and gates promotion in CI; the
**human-review queue refills the gold set** (each reviewer resolution
becomes a ground-truth label). This also closes the gap where
`pipeline.yml` (nightly, `DRY_RUN=false`) currently auto-submits with no
human — only the `AUTO_SUBMIT` slice will.

## Sub-issues

- [ ] #26 — Confidence & abstain data models (`ReviewRoute`,
`ClassifierOutput`, `AbstainPolicy`, `ClassificationDecision`)
- [ ] #27 — Self-consistency classifier sampling + structured outputs
- [ ] #28 — Review queue persistence + gold-set export
- [ ] #29 — Confidence scorer + abstain routing
- [ ] #30 — Pipeline confidence gate + scheduled-run HITL safety
- [ ] #31 — Gold-set evaluation harness + CI acceptance gate

Suggested order: #26 → #27 / #28 → #29 → #30 / #31.

## North star (acceptance)

Non-inferior to a human reviewer on the binary satisfied/dissatisfied call,
with the dissatisfied direction gated hard and confidences calibrated.
Starting bar (calibrate against measured human–human κ): `binary_agreement
≥ 0.95`, `dissatisfied_precision ≥ 0.98`, `cohen_kappa ≥ 0.70`, `ECE ≤
0.05`, `autosubmit_accuracy ≥ 0.97`.

## Out of scope / follow-up

- **autoboost-vault business-context provider**: #27 ships a
`BusinessContextProvider` Protocol + a default `None` provider. Wiring the
actual vault MCP client (fetch real service area / services to inject into
the classifier prompt) is tracked separately, partly in the vault repo. It
mitigates the geo/job-type error class but not caller-side errors
(spam/intent) — a further mitigation, not an elimination.
- **Shadow mode → graduated auto-submit**: run in dry-run alongside human
reviewers, measure agreement/bias per account, and expand the auto-submit
band per reason-code only as the gold-set metrics earn it.

## Notes

- Model id `claude-haiku-4-5` (accepts `temperature`; not `effort`).
Structured outputs supported on Haiku.
- All tests mock Anthropic / Deepgram / Google Ads — never call
`ProvideLeadFeedback()` in tests (per `CLAUDE.md`).
- Transcripts are PII: they live only in the local DB and must be scrubbed
before any gold-set export; `gold_set.jsonl` is gitignored.
