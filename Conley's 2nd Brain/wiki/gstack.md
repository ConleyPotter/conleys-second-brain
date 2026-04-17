---
type: tool-analysis
domain: general
tags: [claude-code, gstack, ai-workflow, sprint, tools, garry-tan, openclaw]
created: 2026-04-17
updated: 2026-04-17
sources: [garrytangstack Use Garry Tan's exact Claude Code setup 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA.md]
---

# gstack — Garry Tan's Claude Code Sprint Framework

**Related:** [[opus-4-7-workflow]], [[openai-codex-app]], [[tech-stack]], [[domain-general]]

*Source: garrytan/gstack GitHub README. MIT licensed, open source. Author: Garry Tan, President & CEO of Y Combinator.*

---

## What It Is

gstack is an open-source collection of Claude Code slash commands organized as a sprint workflow. It turns Claude Code into a virtual engineering team: a CEO, designer, eng manager, QA lead, security officer, and release engineer — all slash commands, all Markdown, all free.

**Stats from Garry Tan's own usage:**
- 600,000+ lines of production code in 60 days (35% tests)
- 10,000–20,000 lines per day, part-time while running YC full-time
- Last /retro: 140,751 lines added, 362 commits, ~115K net LOC in one week

The opening frame: Karpathy said in March 2026 that he hadn't "typed like a line of code probably since December." Peter Steinberger built OpenClaw (247K GitHub stars) essentially solo with AI agents. gstack is Tan's concrete answer to how one person moves faster than a traditional team.

---

## The Sprint Process

Skills run in the order a sprint runs:

**Think → Plan → Build → Review → Test → Ship → Reflect**

Each skill feeds into the next. `/office-hours` writes a design doc that `/plan-ceo-review` reads. `/plan-eng-review` writes a test plan that `/qa` picks up. `/review` catches bugs that `/ship` verifies are fixed.

---

## Key Skills

### Planning

| Skill | Specialist | What it does |
|---|---|---|
| `/office-hours` | YC Office Hours | Six forcing questions that reframe your product before code is written. Pushes back on framing, challenges premises, generates implementation alternatives. Design doc feeds downstream skills automatically. |
| `/plan-ceo-review` | CEO/Founder | Rethink the problem. Four modes: Expansion, Selective Expansion, Hold Scope, Reduction. |
| `/plan-eng-review` | Eng Manager | Lock architecture, data flow, ASCII diagrams, edge cases, test matrix, failure modes. |
| `/plan-design-review` | Senior Designer | Rates design dimensions 0–10. AI Slop detection. One AskUserQuestion per design choice. |
| `/plan-devex-review` | DX Lead | Developer persona research, competitor TTHW benchmarks, friction tracing. 20–45 forcing questions. |
| `/autoplan` | Review pipeline | One command: CEO → design → eng → DX review automatically. Surfaces only taste decisions for approval. |

### Build and Review

| Skill | Specialist | What it does |
|---|---|---|
| `/review` | Staff Engineer | Find bugs that pass CI but blow up in production. Auto-fixes obvious issues. Flags completeness gaps. |
| `/investigate` | Debugger | Root-cause debugging. Iron Law: no fixes without investigation. Stops after 3 failed fixes. |
| `/qa` | QA Lead | Real Chromium browser, tests app, fixes bugs with atomic commits, auto-generates regression tests per fix. |
| `/qa-only` | QA Reporter | Same methodology as /qa but report-only — no code changes. |
| `/cso` | Chief Security Officer | OWASP Top 10 + STRIDE threat model. 17 false positive exclusions, 8/10+ confidence gate. Concrete exploit scenario per finding. |

### Ship

| Skill | Specialist | What it does |
|---|---|---|
| `/ship` | Release Engineer | Sync main, run tests, audit coverage, push, open PR. Bootstraps test framework if needed. Auto-invokes /document-release. |
| `/land-and-deploy` | Release Engineer | Merge PR, wait for CI + deploy, verify production health. One command from "approved" to "verified in production." |
| `/canary` | SRE | Post-deploy monitoring: console errors, performance regressions, page failures. |
| `/retro` | Eng Manager | Weekly retro: per-person breakdowns, shipping streaks, test health trends. `/retro global` spans all projects and AI tools. |

### Design Pipeline

`/design-shotgun` → `/design-html` — from visual exploration to production HTML. Generate 4–6 mockup variants (with taste memory that learns preferences across rounds), then convert the approved design to shippable HTML using Pretext computed layout: 30KB, zero dependencies, React/Svelte/Vue-aware. Not a demo — the output is shippable.

### Power Tools

| Tool | What it does |
|---|---|
| `/careful` | Warns before destructive commands (rm -rf, DROP TABLE, force-push) |
| `/freeze` | Locks edits to one directory while debugging; prevents accidental changes outside scope |
| `/guard` | /careful + /freeze combined |
| `/browse` / `/open-gstack-browser` | Real Chromium with anti-bot stealth, sidebar agent, one-click cookie import, auto model routing (Sonnet for actions, Opus for analysis) |
| `/pair-agent` | Cross-agent browser coordination — Claude, OpenClaw, Codex, Cursor, Hermes each get their own tab; scoped tokens, tab isolation, ngrok tunnel for remote agents |
| `/codex` | Independent code review from OpenAI Codex CLI: three modes — review (pass/fail gate), adversarial challenge, open consultation |
| `/learn` | Session-to-session memory management; compounds codebase-specific patterns across sessions |

---

## Parallel Sprints

gstack works well with one sprint. It gets interesting with ten running at once.

[Conductor](https://conductor.build/) runs multiple Claude Code sessions in parallel, each in an isolated workspace. Tan regularly runs 10–15 parallel sprints: one on /office-hours for a new idea, another on /review for a PR, a third implementing a feature, a fourth on /qa on staging, and more simultaneously.

The sprint structure is what makes parallelism safe. Without a process, ten agents is ten sources of chaos. With Think → Plan → Build → Review → Test → Ship, each agent knows exactly what to do and when to stop. You manage them the way a CEO manages a team: check in on decisions that matter, let the rest run.

---

## OpenClaw Integration

gstack skills work inside OpenClaw via ACP — OpenClaw spawns Claude Code sessions and dispatches gstack skills. Dispatch patterns:

| Task | What OpenClaw does |
|---|---|
| Security audit | Spawns Claude Code with `Run /cso` |
| Code review | Spawns Claude Code with `Run /review` |
| QA test a URL | Spawns Claude Code with `Run /qa https://...` |
| Build a feature | Spawns Claude Code with /autoplan → implement → /ship |
| Plan before building | Spawns Claude Code with /office-hours → /autoplan, saves plan |

Relevant to [[tech-stack]]: OpenClaw is ACE's Phase III agentic framework. gstack provides a structured skill layer that OpenClaw can dispatch without Conley managing sprint steps manually.

---

## Relationship to Karpathy's AI Coding Rules

gstack explicitly addresses Karpathy's four AI coding failure modes (17K stars): wrong assumptions, overcomplexity, orthogonal edits, imperative over declarative.

- `/office-hours` forces assumptions into the open before code is written
- The Confusion Protocol stops Claude from guessing on architectural decisions
- `/review` catches unnecessary complexity and drive-by edits
- `/ship` transforms tasks into verifiable goals with test-first execution

gstack positions itself as the workflow enforcement layer that makes Karpathy-style CLAUDE.md rules stick across entire sprints, not just single prompts. This extends the verification-first approach documented in [[opus-4-7-workflow]] from individual tasks to complete sprint cycles.

---

## Availability

Free, MIT licensed, open source. Works on 10 AI coding agents (Claude Code, OpenAI Codex CLI, OpenCode, Cursor, Factory Droid, Slate, Kiro, Hermes, GBrain). 30-second install via git clone. Auto-updates silently each session (throttled to once/hour). YC is hiring to harden gstack further.

> **Relevance to ACE:** The parallel sprint model (10–15 Claude Code sessions via Conductor) is the agentic workflow Cherny's Opus 4.7 article pointed toward. gstack operationalizes it. If Conley ever runs multi-session ACE development work, the /autoplan → implement → /ship pipeline combined with OpenClaw dispatch could significantly compress operator time against ACE's 15-hour weekly constraint.
