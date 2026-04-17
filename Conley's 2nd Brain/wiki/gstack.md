---
type: tool-analysis
domain: general
tags: [ai-tools, claude-code, developer-workflow, gstack, agentic-coding]
created: 2026-04-17
updated: 2026-04-17
sources: [garrytangstack Use Garry Tan's exact Claude Code setup 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA.md]
---

# gstack — Garry Tan's Claude Code Toolkit

**Related:** [[domain-general]], [[tech-stack]], [[opus-4-7-workflow]], [[ace-overview]], [[openai-codex-2026-update]]

*Source: garrytan/gstack GitHub README — Garry Tan (YC President & CEO)*

---

## What It Is

gstack is an open-source collection of 23 slash commands for Claude Code that turns it into a virtual engineering team. Each command is a specialist: CEO who rethinks the product, eng manager who locks architecture, designer who catches AI slop, QA lead who opens a real browser, security officer who runs OWASP + STRIDE audits, release engineer who ships the PR.

**Free, MIT licensed. Available for Claude Code, OpenAI Codex CLI, Cursor, Factory Droid, Kiro, and others.**

Garry Tan's reported output with gstack: 600K+ lines of production code (35% tests) in 60 days, part-time, while running YC full-time. One recent `/retro`: 140,751 lines added, 362 commits, ~115K net LOC in one week.

---

## The Sprint Process

gstack is a process, not a collection of tools. Skills run in the order a sprint runs:

**Think → Plan → Build → Review → Test → Ship → Reflect**

Each skill feeds into the next. `/office-hours` writes a design doc that `/plan-ceo-review` reads. `/plan-eng-review` writes a test plan that `/qa` picks up. `/review` catches bugs that `/ship` verifies are fixed.

---

## Skills Reference

### Planning

| Skill | Specialist | What it does |
|---|---|---|
| `/office-hours` | YC Office Hours | 6 forcing questions that reframe the product before code is written. Pushes back on framing, challenges premises, generates implementation alternatives. Design doc feeds into all downstream skills. |
| `/plan-ceo-review` | CEO / Founder | Rethink the problem. Find the 10-star product inside the request. 4 modes: Expansion, Selective Expansion, Hold Scope, Reduction. |
| `/plan-eng-review` | Eng Manager | Architecture, data flow, ASCII diagrams, edge cases, test plan. Forces hidden assumptions into the open. |
| `/plan-design-review` | Senior Designer | Rates each design dimension 0–10, explains what a 10 looks like, then edits the plan. AI Slop detection. |
| `/plan-devex-review` | Developer Experience Lead | Interactive DX review — explores developer personas, benchmarks TTHW, traces friction points. 20–45 forcing questions. |
| `/autoplan` | Review Pipeline | One command, fully reviewed plan. Runs CEO → design → eng review automatically. Surfaces only taste decisions for approval. |

### Building + Reviewing

| Skill | Specialist | What it does |
|---|---|---|
| `/review` | Staff Engineer | Find bugs that pass CI but blow up in production. Auto-fixes obvious ones. |
| `/investigate` | Debugger | Systematic root-cause debugging. Iron Law: no fixes without investigation. Stops after 3 failed fixes. |
| `/design-review` | Designer Who Codes | Same audit as /plan-design-review, then fixes what it finds. Atomic commits, before/after screenshots. |
| `/devex-review` | DX Tester | Actually tests your onboarding: navigates docs, tries the getting started flow, times TTHW, screenshots errors. |
| `/design-consultation` | Design Partner | Build a complete design system from scratch. |
| `/design-shotgun` | Design Explorer | Generates 4–6 AI mockup variants, opens a comparison board, collects feedback, iterates. Taste memory learns preferences across rounds. |
| `/design-html` | Design Engineer | Turns an approved mockup into production HTML/CSS. 30KB overhead, zero deps, framework-aware (React/Svelte/Vue). |

### Testing + QA

| Skill | What it does |
|---|---|
| `/qa` | Opens real Chromium browser, clicks through flows, finds bugs, fixes them with atomic commits, generates regression tests for every fix. The unlock for parallel workers. |
| `/qa-only` | Same methodology as /qa but report only — no code changes. |
| `/browse` | Give the agent eyes. Real Chromium, real clicks, real screenshots. ~100ms per command. |
| `/cso` | OWASP Top 10 + STRIDE threat model. 17 false positive exclusions, 8/10+ confidence gate, independent finding verification. Each finding includes a concrete exploit scenario. |

### Shipping

| Skill | What it does |
|---|---|
| `/ship` | Sync main, run tests, audit coverage, push, open PR. Bootstraps test frameworks if needed. Auto-invokes `/document-release`. |
| `/land-and-deploy` | Merge PR, wait for CI and deploy, verify production health. One command from "approved" to "verified in production." |
| `/canary` | Post-deploy monitoring — watches for console errors, performance regressions, page failures. |
| `/benchmark` | Baseline page load times, Core Web Vitals, resource sizes. Before/after on every PR. |
| `/document-release` | Updates all project docs to match what shipped. Catches stale READMEs automatically. |
| `/retro` | Weekly retro with per-person breakdowns, shipping streaks, test health trends. `/retro global` runs across all projects and AI tools. |

### Power Tools

| Skill | What it does |
|---|---|
| `/careful` | Warns before destructive commands (rm -rf, DROP TABLE, force-push). Say "be careful" to activate. |
| `/freeze` | Locks edits to one directory. Prevents accidental changes outside scope while debugging. |
| `/guard` | `/careful` + `/freeze` in one command. Maximum safety for prod work. |
| `/codex` | Second opinion — independent review from OpenAI Codex CLI. Three modes: review (pass/fail), adversarial challenge, open consultation. Cross-model analysis when both /review and /codex have run. |
| `/learn` | Manage what gstack learned across sessions — review, search, prune, and export project-specific patterns and preferences. |
| `/pair-agent` | Multi-agent coordination — share a real browser with any AI agent (OpenClaw, Hermes, Codex, Cursor). Scoped tokens, tab isolation, rate limiting, activity attribution. |

---

## Parallel Sprints

gstack's sprint structure is what makes parallelism work. Garry Tan runs 10–15 parallel sprints via [Conductor](https://conductor.build/), which manages multiple Claude Code sessions in isolated workspaces. One doing `/office-hours` on a new idea, one doing `/review` on a PR, one implementing a feature, one running `/qa` on staging. Without a process, ten agents is ten sources of chaos; with a process, each agent knows exactly what to do and when to stop.

---

## OpenClaw Integration

gstack integrates directly with OpenClaw via the Agent Communication Protocol (ACP). When OpenClaw spawns a Claude Code session, gstack skills are available automatically. OpenClaw's AGENTS.md gets a "Coding Tasks" section that routes requests to the appropriate gstack skill — security audit → `/cso`, full feature build → `/autoplan → implement → /ship`, QA a URL → `/qa https://...`.

This is directly relevant to ACE's tech stack: see [[tech-stack]] for OpenClaw's deployment in Phase III. The gstack + OpenClaw integration is the closest thing to a public reference implementation of the kind of multi-agent stack ACE is building.

> **Karpathy context:** The gstack README opens with an Andrej Karpathy quote — "I don't think I've typed like a line of code probably since December" (No Priors podcast, March 2026). See [[llm-wiki-pattern]] for Karpathy's LLM Wiki methodology, which is the conceptual framework behind this second brain.

---

## Install

```
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup
```

Requirements: Claude Code, Git, Bun v1.0+. Supports Claude Code, Codex CLI, Cursor, Factory Droid, Kiro, Hermes, GBrain.

---

## Relevance to ACE

- **Single-operator leverage thesis** — gstack is built on the same premise as ACE: one person with the right tooling can move faster than a traditional team. The 600K LOC / 60 days stat is Tan's version of the ACE arbitrage thesis applied to software.
- **OpenClaw integration** — gstack's native OpenClaw support means ACE's Phase III agent orchestration layer and the gstack sprint framework could be combined
- **The `/qa` unlock** — "It let me go from 6 to 12 parallel workers." The browser-grounded QA agent maps to ACE's quality gate in the HITL pipeline.
- **Karpathy's Confusion Protocol** — gstack enforces a rule that Claude stops and asks rather than guessing on architectural decisions. This is the same principle behind ACE's HITL gate — human approval on decisions that exceed automated confidence thresholds.
