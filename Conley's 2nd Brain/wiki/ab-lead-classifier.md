---
type: operations
domain: ba
tags: [autoboost, lead-classifier, confidence-scoring, hitl, google-ads, haiku, stt, pipeline]
created: 2026-06-08
updated: 2026-06-08
sources: [ab-lead-classifier-confidence-pipeline-issue-2026-06-08.md]
---

# AutoBoost Lead Classifier — Confidence-Gated Pipeline

**Related:** [[ba-overview]], [[ba-products]], [[autoboost-vault-skills]]

---

## What It Is

A confidence-gated pipeline that classifies incoming Google Ads leads (phone calls transcribed via Deepgram STT) and submits structured feedback to Google via `ProvideLeadFeedback()`. The feedback is a 5-point `SurveyAnswer` + reason that directly feeds Google's per-advertiser lead matching algorithm and the credit/dispute system for lead quality.

This is not a passive analytics layer — it actively shapes the quality of leads Google sends to AutoBoost's clients. A wrong rating (especially a false dissatisfied/dispute) can harm a client's lead quality standing and cost them real money.

---

## The Problem

The current nightly pipeline (`pipeline.yml`, `DRY_RUN=false`) auto-submits classifications with no human oversight. The classifier uses Claude Haiku (`claude-haiku-4-5`), the smallest Anthropic model, which is fast and cheap but carries meaningful error risk on ambiguous calls.

**Error sources stack:**
1. **STT errors** — Deepgram mis-transcriptions on noisy or accented calls
2. **LLM classification errors** — Haiku misreading intent, context, or sentiment
3. **Confident misclassification** — the dominant risk; a wrong rating delivered with high certainty is worse than a random error because it systematically biases Google's matching

Systematic error is worse than random. The goal is not "eliminate hallucination" — it's **bound the error, contain the harmful direction (dissatisfied/dispute), route uncertain cases to a human, and measure against the human-reviewer baseline.**

---

## Architecture: Self-Consistency + Abstain Routing

The Anthropic Messages API exposes no token logprobs, so the system derives confidence from **self-consistency sampling**: run the Haiku classifier N times at `temperature > 0`, measure vote agreement, blend with the model's self-reported confidence, and gate on STT transcript quality.

### Routing logic

| Route | Condition | Action |
|---|---|---|
| `AUTO_SUBMIT` | Confidence ≥ threshold AND STT quality gate passes | Batched `ProvideLeadFeedback()` to Google |
| `HUMAN_REVIEW` | Below threshold / dissatisfied direction / low STT quality | Routed to review queue |
| `DROP` | No usable transcript | Never submitted |

**Key design constraint:** The dissatisfied/dispute direction carries a **higher precision bar** — it's the direction that can harm a client or a real customer. False positives in this direction are more costly than false negatives.

### Confidence scoring components

- **Self-consistency vote agreement** (primary signal) — N samples, measure consensus
- **Model self-reported confidence** (secondary signal) — blended into the composite score
- **STT quality gate** (hard gate) — low-quality transcripts are routed to `HUMAN_REVIEW` or `DROP` regardless of classifier confidence

---

## North Star Metrics

Non-inferior to a human reviewer on the binary satisfied/dissatisfied call:

| Metric | Target | Notes |
|---|---|---|
| Binary agreement | ≥ 0.95 | Calibrate against measured human-human kappa |
| Dissatisfied precision | ≥ 0.98 | Hard gate on the harmful direction |
| Cohen's kappa | ≥ 0.70 | Inter-rater agreement with human baseline |
| ECE (expected calibration error) | ≤ 0.05 | Confidence scores must be well-calibrated |
| Auto-submit accuracy | ≥ 0.97 | Only the high-confidence auto-submit band |

---

## Implementation: Sub-Issues

Six sub-issues in suggested execution order:

1. **#26 — Confidence & abstain data models** — `ReviewRoute`, `ClassifierOutput`, `AbstainPolicy`, `ClassificationDecision`
2. **#27 — Self-consistency classifier sampling** — N-sample voting + structured outputs from Haiku
3. **#28 — Review queue persistence** — human review queue + gold-set export
4. **#29 — Confidence scorer + abstain routing** — composite scoring and routing logic
5. **#30 — Pipeline confidence gate** — integrate into `pipeline.yml` scheduled runs + HITL safety
6. **#31 — Gold-set evaluation harness** — CI acceptance gate for threshold calibration

**Dependency graph:** #26 → #27 / #28 (parallel) → #29 → #30 / #31 (parallel)

---

## Gold Set and Human-in-the-Loop Loop

The gold-set eval harness serves dual purposes:

1. **Calibrate thresholds** — the gold set is the ground truth for tuning confidence thresholds and gating promotion in CI
2. **Human-review queue refills the gold set** — every reviewer resolution becomes a new ground-truth label, creating a flywheel: more reviews → better calibration → fewer reviews needed

This closes the current gap where the pipeline auto-submits everything with no human check.

> **Note:** Transcripts are PII. They live only in the local DB and must be scrubbed before any gold-set export. `gold_set.jsonl` is gitignored.

---

## Out of Scope (Tracked Separately)

- **AutoBoost Vault business-context provider:** Issue #27 ships a `BusinessContextProvider` Protocol + a default `None` provider. Wiring the actual vault MCP client (fetch real service area / services to inject into the classifier prompt) is tracked separately, partly in the vault repo. Mitigates geo/job-type error class but not caller-side errors (spam/intent).
- **Shadow mode → graduated auto-submit:** Run in dry-run alongside human reviewers, measure agreement/bias per account, expand the auto-submit band per reason-code only as gold-set metrics earn it.

---

## Technical Notes

- Model: `claude-haiku-4-5` (accepts `temperature`; not `effort`). Structured outputs supported.
- All tests mock Anthropic / Deepgram / Google Ads — `ProvideLeadFeedback()` is never called in tests.
- Transcripts are PII: local DB only, scrubbed before gold-set export.
