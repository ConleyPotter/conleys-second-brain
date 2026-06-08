# Claude Code Dynamic Workflows — Official Documentation

**Source:** https://code.claude.com/docs/en/workflows
**Captured:** 2026-06-08
**Type:** Official product documentation (Anthropic)

---

## Overview

Dynamic workflows orchestrate many subagents from a script Claude writes and you can rerun. Use them for codebase audits, large migrations, and cross-checked research.

Dynamic workflows are in research preview. They require Claude Code v2.1.154 or later and are available on all paid plans, with Anthropic API access, and on Amazon Bedrock, Google Cloud Vertex AI, and Microsoft Foundry.

A dynamic workflow is a JavaScript script that orchestrates subagents at scale. Claude writes the script for the task you describe, and a runtime executes it in the background while your session stays responsive.

Use cases: codebase-wide bug sweep, 500-file migration, research question needing cross-checked sources, hard plan worth drafting from several independent angles.

## When to use a workflow

Comparison table — subagents vs. skills vs. agent teams vs. workflows:

| | Subagents | Skills | Agent teams | Workflows |
|---|---|---|---|---|
| What it is | A worker Claude spawns | Instructions Claude follows | A lead agent supervising peer sessions | A script the runtime executes |
| Who decides what runs next | Claude, turn by turn | Claude, following the prompt | The lead agent, turn by turn | The script |
| Where intermediate results live | Claude's context window | Claude's context window | A shared task list | Script variables |
| What's repeatable | The worker definition | The instructions | The team definition | The orchestration itself |
| Scale | A few delegated tasks per turn | Same as subagents | A handful of long-running peers | Dozens to hundreds of agents per run |
| Interruption | Restarts the turn | Restarts the turn | Teammates keep running | Resumable in the same session |

Key insight: a workflow moves the plan into code. With subagents/skills/agent teams, Claude is the orchestrator deciding turn by turn what to spawn. A workflow script holds the loop, branching, and intermediate results itself, so Claude's context holds only the final answer.

Moving the plan into code also enables repeatable quality patterns: independent agents adversarially reviewing each other's findings before reporting, or drafting a plan from several angles and weighing them against each other.

## Bundled workflows

`/deep-research` — fans out web searches on a question across several angles, fetches and cross-checks the sources, votes on each claim, and returns a cited report with unverified claims filtered out. Requires WebSearch tool.

### Running /deep-research

1. Run `/deep-research` with a question
2. Approve the workflow when prompted
3. Watch progress via `/workflows` — shows each phase with agent count, token total, elapsed time
4. Read the synthesized report when the run finishes

### Watch the run

Run `/workflows` at any time. Progress view keyboard controls:

| Key | Action |
|---|---|
| ↑/↓ | Select phase or agent |
| Enter/→ | Drill into selected phase/agent |
| Esc | Back out one level |
| j/k | Scroll within agent detail |
| p | Pause/resume the run |
| x | Stop selected agent or whole workflow |
| r | Restart selected running agent |
| s | Save the run's script as a command |

## Creating custom workflows

### Ask for a workflow in your prompt

Include keyword `ultracode` in prompt, or ask directly ("use a workflow", "run a workflow"). Before v2.1.160, the literal trigger keyword was `workflow`.

Example: `ultracode: audit every API endpoint under src/routes/ for missing auth checks`

Claude writes a workflow script instead of working turn by turn.

### Ultracode effort level

`/effort ultracode` — combines `xhigh` reasoning effort with automatic workflow orchestration. Claude decides when a task warrants a workflow. A single request can turn into several workflows in sequence.

Ultracode lasts for the current session. Available on models that support `xhigh` effort.

### Approval behavior

Depends on permission mode:

| Permission mode | When prompted |
|---|---|
| Default, accept edits | Every run (unless "don't ask again" was selected) |
| Auto | First launch only |
| Bypass permissions, `claude -p`, Agent SDK | Never — starts immediately |

Desktop app shows approval card with Once/Always/Deny actions.

Subagents spawned by workflows always run in `acceptEdits` mode and inherit the tool allowlist.

### Saving workflows

From `/workflows`, select a run, press `s`. Save to:
- `.claude/workflows/` in project (shared with repo)
- `~/.claude/workflows/` in home directory (personal, all projects)

Project workflow overrides personal if names conflict. Saved workflows appear in `/` autocomplete.

### Passing input

Saved workflows accept input through `args` parameter. Script reads it as global named `args`.

Example: `> Run /triage-issues on issues 1024, 1025, and 1030`

Claude passes the list as structured data — script can call array/object methods directly.

## How a workflow runs

The runtime executes the script in an isolated environment, separate from conversation. Intermediate results stay in script variables.

Every run writes its script to a file under `~/.claude/projects/`. You can read, diff, edit, and relaunch from the script file.

### Behavior and limits

| Constraint | Why |
|---|---|
| No mid-run user input | Only permission prompts can pause. For sign-off between stages, run each as its own workflow |
| No direct filesystem/shell access from workflow itself | Agents read/write/run commands. The script coordinates agents |
| Up to 16 concurrent agents (fewer on limited CPU) | Bounds local resource use |
| 1,000 agents total per run | Prevents runaway loops |

## Managing runs

### Resume after a pause

Stopped runs can be resumed — completed agents return cached results, rest run live. Resume from `/workflows` by pressing `p`. Resume works within the same Claude Code session; exiting starts fresh.

### Cost

Workflows spawn many agents — a single run can use meaningfully more tokens than conversational approach. Runs count toward plan usage and rate limits.

Mitigation: run on a small slice first (one directory vs. whole repo). `/workflows` view shows each agent's token usage. Agent caps (16 concurrent, 1000 total) bound costs.

Every agent uses session's model unless script routes to a different one.

### Turning workflows off

- Toggle Dynamic workflows off in `/config`
- Set `"disableWorkflows": true` in `~/.claude/settings.json`
- Set `CLAUDE_CODE_DISABLE_WORKFLOWS=1` environment variable
- Org-level: `"disableWorkflows": true` in managed settings or via admin settings page

When disabled: bundled commands unavailable, `ultracode` keyword doesn't trigger, `ultracode` removed from `/effort` menu.

## Related concepts

- Subagents: the worker primitive workflows orchestrate
- Agent teams: lead-supervised peer sessions
- Skills: instruction-based task guidance
- Cost management for multi-agent runs
