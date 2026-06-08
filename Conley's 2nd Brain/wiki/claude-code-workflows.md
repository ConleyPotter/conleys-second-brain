---
type: tool-analysis
domain: general
tags: [claude-code, workflows, multi-agent, orchestration, subagents, ultracode, deep-research]
created: 2026-06-08
updated: 2026-06-08
sources: [claude-code-workflows-docs-2026-06-08.md]
---

# Claude Code Dynamic Workflows

**Related:** [[multi-agent-orchestration]], [[gstack]], [[perplexity-agent-skills]], [[opus-4-7-workflow]]

---

## What it is

Dynamic workflows are a Claude Code feature (research preview, v2.1.154+) that orchestrate subagents at scale via JavaScript scripts. Unlike conversational subagents (where Claude decides turn by turn what to spawn), a workflow moves the orchestration plan into code: Claude writes the script, and a dedicated runtime executes it in the background while the session stays responsive.

The key distinction from other multi-agent patterns: workflows put the loop, branching, and intermediate results in a script, keeping Claude's context window clean for the final synthesis. This enables hundreds of agents per run, repeatable quality patterns (adversarial cross-checking, multi-angle drafts), and rerunnable orchestrations.

Available on all paid Claude Code plans (Pro, Max, Team, Enterprise), with Anthropic API access, and on Amazon Bedrock, Google Cloud Vertex AI, and Microsoft Foundry.

---

## Workflow vs. other orchestration patterns

| | Subagents | Skills | Agent teams | Workflows |
|---|---|---|---|---|
| **What it is** | A worker Claude spawns | Instructions Claude follows | A lead agent supervising peer sessions | A script the runtime executes |
| **Who decides what runs next** | Claude, turn by turn | Claude, following the prompt | The lead agent, turn by turn | The script |
| **Where intermediate results live** | Claude's context window | Claude's context window | A shared task list | Script variables |
| **What's repeatable** | The worker definition | The instructions | The team definition | The orchestration itself |
| **Scale** | A few delegated tasks per turn | Same as subagents | A handful of long-running peers | Dozens to hundreds of agents per run |
| **Interruption** | Restarts the turn | Restarts the turn | Teammates keep running | Resumable in the same session |

The practical trade-off: subagents are fastest for quick delegation (a few tasks); agent teams are best for sustained parallel work; workflows are best when you need many agents, cross-checking, or a script you'll rerun.

---

## Built-in: /deep-research

Claude Code ships a bundled workflow called `/deep-research`. It fans out web searches across several angles on a research question, fetches and cross-checks sources, votes on each claim, and returns a cited report with claims that didn't survive cross-checking filtered out.

Requires the WebSearch tool. This is the fastest way to see workflows in action.

---

## Creating custom workflows

### Triggering a workflow

Two ways to get Claude to write a workflow for your task:

1. **Keyword trigger:** Include `ultracode` in your prompt (or ask directly — "use a workflow," "run a workflow"). Example: `ultracode: audit every API endpoint under src/routes/ for missing auth checks`
2. **Effort level:** Run `/effort ultracode` — combines `xhigh` reasoning effort with automatic workflow orchestration for every substantive task in the session. Lasts until session end or `/effort high`.

### Approval

The approval prompt depends on your permission mode:

- **Default / accept edits:** Prompted every run (unless you've opted out for that workflow in that project)
- **Auto:** First launch only
- **Bypass permissions / `claude -p` / Agent SDK:** Never prompted

Subagents spawned by the workflow always run in `acceptEdits` mode and inherit the session's tool allowlist.

### Saving and reusing

After a successful run, save it as a reusable command:

1. Run `/workflows`, select the run, press `s`
2. Save to `.claude/workflows/` (project-level, shared via repo) or `~/.claude/workflows/` (personal, all projects)
3. The workflow appears in `/` autocomplete for future sessions

Saved workflows accept structured input via the `args` parameter — pass a list of issue numbers, target paths, or configuration objects at invocation time without editing the script.

---

## Runtime constraints

| Constraint | Rationale |
|---|---|
| No mid-run user input | Only permission prompts pause. For stage sign-off, run each stage as a separate workflow |
| No direct filesystem/shell from the workflow itself | Agents handle file I/O — the script coordinates agents |
| Up to 16 concurrent agents | Bounds local resource use (fewer on limited-CPU machines) |
| 1,000 agents total per run | Prevents runaway loops |

Workflows are resumable within the same Claude Code session. Exiting starts fresh.

---

## Cost and token usage

A single workflow can use meaningfully more tokens than the same task done conversationally — it spawns many agents. All usage counts toward plan limits and rate limits.

Mitigation strategies:
- Run on a small slice first (one directory, not the whole repo; a narrow question, not a broad one)
- Monitor via `/workflows` — shows each agent's token usage in real time
- Agent caps (16 concurrent, 1,000 total) bound worst-case
- Use a smaller model for routine stages; every agent uses the session's model unless the script routes elsewhere

---

## Disabling workflows

For individual users: toggle off in `/config`, or set `"disableWorkflows": true` in `~/.claude/settings.json`, or set `CLAUDE_CODE_DISABLE_WORKFLOWS=1`. For organizations: set in managed settings or the Claude Code admin settings page.

When disabled: bundled workflows unavailable, `ultracode` keyword doesn't trigger, `ultracode` removed from `/effort` menu.

---

## Vault relevance

- **Extends the multi-agent orchestration page** ([[multi-agent-orchestration]]): workflows are Anthropic's production answer to the "how do I run hundreds of agents reliably" question. The Fan-Out pattern from that page is the closest parallel, but workflows codify the orchestration as a rerunnable script rather than leaving it in Claude's context.
- **Relevant to gstack** ([[gstack]]): Garry Tan's Claude Code sprint framework uses slash commands; workflows can be saved as slash commands with the same `/` invocation pattern.
- **DailyChew engineering potential:** codebase-wide audits, large migrations (like the web-to-native pivot with 10+ issues), and cross-checked research are all DailyChew development scenarios where workflows could save significant time.
- **Vault agent operations:** the adversarial cross-checking pattern (independent agents reviewing each other's findings) is directly applicable to the vault's own audit/remediation pipeline.

> **Note:** This is the official product documentation, not a third-party synthesis. Cross-reference the [Claude Code docs](https://code.claude.com/docs/en/workflows) for the latest state — feature is in research preview and may evolve.
