---
type: synthesis
domain: general
tags: [claude, ai-workflow, opus-4-7, tools, agentic]
created: 2026-04-17
updated: 2026-04-17
sources: [Opus 4.7 Thread by Boris Cherny.md, garrytangstack Use Garry Tan's exact Claude Code setup 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA.md]
---

# Claude Opus 4.7 — Workflow Patterns

**Related:** [[tech-stack]], [[ace-overview]], [[conley-potter]], [[domain-general]], [[gstack]]

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

## Related Tooling

**[[gstack]]** (Garry Tan's Claude Code sprint framework) operationalizes the verification-first approach across complete sprints. Where Cherny's workflow describes the pattern at the task level — test end-to-end, run /simplify, put up a PR — gstack provides enforcement across the full sprint: `/qa` for real-browser verification, `/review` for finding production bugs that pass CI, `/ship` for test-first release. gstack explicitly positions itself as the layer that makes Karpathy-style CLAUDE.md rules stick not just for individual prompts but across entire sprint cycles. The parallel sprint model (10–15 Claude Code sessions via Conductor) is the longer-horizon version of the autonomous extended run that Cherny describes.

**[[openai-codex-app]]** (OpenAI's April 2026 update) is converging on the same endpoint from a different direction: background computer use for self-verification, memory across sessions, and scheduled autonomous work. The competitive pressure from Codex reinforces the case for adopting Opus 4.7's verification-first workflow before the default becomes table stakes.
