---
type: synthesis
domain: general
tags: [claude, ai-workflow, opus-4-7, tools, agentic]
created: 2026-04-17
updated: 2026-04-17
sources: [Opus 4.7 Thread by Boris Cherny.md]
---

# Claude Opus 4.7 — Workflow Patterns

**Related:** [[tech-stack]], [[ace-overview]], [[conley-potter]], [[domain-general]]

*Source: Boris Cherny (@boris_cherny), Threads post #6, April 16, 2026*

---

## Core Insight

Give Claude a way to verify its own work. Cherny calls this a consistent 2–3x multiplier on output quality — and with Opus 4.7's increased agentic capability, it matters more than ever. The model runs longer and operates more autonomously than prior versions; without a verification step, you lose the benefit of that autonomy.

---

## Verification by Context

| Context | Verification method |
|---|---|
| Backend / server work | Start the server and test end to end via bash |
| Frontend work | Claude Chromium extension — gives Claude direct browser control |
| Desktop apps | Computer use |

---

## Recommended Workflow

For long-running agentic tasks:

1. Test end to end (bash, browser, or computer use)
2. Run the `/simplify` skill
3. Put up a PR

The rationale: when you return to a long-running task, you know the code works without re-verifying manually. Verification closes the loop that longer autonomous runs leave open.

---

## The Opus 4.7 Shift

Cherny's framing: "a nice improvement with old workflows, and a significant leap once you take the time to adjust." The adjustment is treating Claude less as a turn-by-turn assistant and more as an autonomous agent running extended workstreams. That shift requires:

- Building in verification checkpoints rather than relying on spot-checks
- Trusting longer runs without micro-interrupting
- Matching the verification tooling to the task type (bash/server, Chromium, computer use)

---

## Relevance to ACE

Opus 4.7's agentic capability directly affects how Claude can be positioned in ACE's HITL co-pilot mode (see [[ace-overview]]). If Claude can run longer with self-verification baked in, the human gate shifts from active monitoring to final approval — compressing operator time against the 15-hour weekly constraint.

The router model strategy in [[tech-stack]] already designates Claude Opus as the premium layer for core creative output. Opus 4.7 is a direct upgrade to that layer, with the verification-first workflow pattern being the key behavioral change to adopt.

---

## Related: gstack and the Verification-First Ecosystem

[[gstack]] (Garry Tan's Claude Code toolkit) enforces the same verification-first discipline across an entire sprint structure — not just single prompts. The `/qa` skill gives Claude a real Chromium browser to verify its own frontend work, directly implementing the "browser verification" method Cherny describes. The Confusion Protocol in gstack (Claude stops and asks rather than guessing) is the architectural version of the same rule: don't proceed without a verification mechanism.

Karpathy — quoted in the gstack README as not having "typed a line of code since December" — is operating at the same mode Cherny's framework describes: treating Claude as an autonomous agent with built-in verification loops rather than a turn-by-turn assistant.
