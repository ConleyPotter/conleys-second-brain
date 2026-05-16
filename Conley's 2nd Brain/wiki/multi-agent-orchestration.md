---
type: synthesis
domain: general
tags: [multi-agent, claude, orchestration, anthropic, managed-agents]
created: 2026-05-16
updated: 2026-05-16
sources: [how-to-build-a-team-of-ai-agents-that-actually-work-together.md]
---

# Multi-Agent Orchestration

Comprehensive guide to building teams of AI agents that work together, based on Anthropic's Claude Managed Agents announcement (May 6, 2026) and production patterns from Netflix, Harvey, Shopify, and Mercado Libre.

## Key context

On May 6, 2026, Anthropic announced multi-agent orchestration for Claude Managed Agents at their Code with Claude event. Up to 20 specialized agents can now run in parallel on a single task. Apple also announced Claude integration into iOS 27 via a new Extensions system.

## Why multi-agent beats single-agent

- **Speed:** Five parallel agents finish in ~1/5 the time of one sequential agent
- **Specialization:** Each agent focuses on one thing and does it well — a generalist agent spreading attention across research, analysis, writing, coding, and review produces mediocre results across the board
- Same logic as human teams outperforming individuals on complex projects

## The three patterns that work

### Pattern 1: Pipeline
Agents work in sequence, each passing output to the next.

`Research Agent → Analysis Agent → Writing Agent → Review Agent`

Best when each step has clear input/output and later steps depend on earlier ones.

### Pattern 2: Fan-Out
A commander agent breaks a task into subtasks and distributes to parallel workers.

- Commander assigns N workers, each handling an independent subtask
- All workers run simultaneously; results collected and synthesized
- Netflix uses this for analyzing hundreds of build logs simultaneously
- Ideal for same-operation-on-many-items tasks

### Pattern 3: Specialist Team
Multiple agents with different specializations collaborate on one complex task.

- Harvey (legal AI) uses this: research, precedent analysis, document drafting, compliance checking — assembled into a complete legal package
- For a product launch: market research, technical, financial, copy, and review agents

## Seven-step build process

1. **Define your team** — goal, sub-tasks, parallelism, specialist roles
2. **Design each agent** — clear role, specific tools, defined output format (standardize output formats across agents — most important technical decision)
3. **Build orchestration** — parallel vs. sequential, data passing, failure handling
4. **Add memory with Dreaming** — scheduled background process that reviews past sessions, extracts patterns, curates memory. Harvey reported ~6x completion rate increase from Dreaming alone
5. **Define Outcomes** — rubric-based grading system; Claude evaluates its own output and iterates until it passes
6. **Test incrementally** — start with 2 agents, get communication right, then add more
7. **Monitor and iterate** — watch for handoff failures, redundant work, quality degradation, token bloat

## Production example: Weekly Market Intelligence Report

Six agents (3 parallel researchers → analysis → writer → quality review). Total time: under 15 minutes vs. over an hour single-agent vs. half a day manual.

## Common mistakes

- Making agents too general (defeats the purpose of specialization)
- Not standardizing output formats (breaks handoffs)
- Running too many agents in parallel too early (manage complexity incrementally)
- No error handling between agents (define fallback behavior)
- Ignoring token costs (each agent has its own context and output)

## Connections to the wiki

- [[jarvis-system]] already uses a multi-stage pipeline (inbox → captures → connections → briefs → published) — structurally similar to Pattern 1
- [[gstack]] uses 23 specialist slash commands — similar philosophy of narrow specialization
- [[thought-leader-engine]] could benefit from Pattern 3 (specialist team) for content production
- The Dreaming feature maps conceptually to what this second brain does — extracting patterns across sessions and building persistent institutional knowledge
- [[opus-4-7-workflow]] covers verification-first patterns that complement multi-agent quality review

> **Note:** The source is a social media thread by @eng_khairallah1 — specific claims about Harvey's 6x improvement and Shopify's 90% autonomous coding target by Q3 2026 are not independently verified here. The architectural patterns themselves are well-established.
