---
type: tool-analysis
domain: general
tags: [claude-code, agent-teams, multi-agent, parallel, coordination, anthropic]
created: 2026-06-08
updated: 2026-06-08
sources: [claude-code-agent-teams-docs-2026-06-08.md]
---

# Claude Code Agent Teams

**Related:** [[multi-agent-orchestration]], [[gstack]], [[opus-4-7-workflow]]

---

## What this is

Agent teams are an experimental feature in Claude Code (v2.1.32+, June 2026) that coordinates multiple Claude Code sessions working together. One session acts as the **team lead**, spawning and coordinating **teammates** — each a fully independent Claude Code instance with its own context window. Unlike subagents (which run inside a single session and report back), teammates communicate directly with each other through a shared mailbox and task list.

This is the first-party implementation of the Fan-Out and Specialist Team patterns documented in [[multi-agent-orchestration]].

> **Status:** Experimental, disabled by default. Enable via `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in `settings.json` or the shell environment.

---

## Architecture

| Component     | Role |
|---|---|
| **Team lead** | The main Claude Code session — creates the team, spawns teammates, coordinates work |
| **Teammates** | Separate Claude Code instances, each with their own context window and full tool access |
| **Task list** | Shared list of work items with states (pending / in progress / completed) and dependencies |
| **Mailbox**   | Inter-agent messaging system — teammates send messages directly to each other by name |

Local storage:
- Team config: `~/.claude/teams/{team-name}/config.json`
- Task list: `~/.claude/tasks/{team-name}/`

Each teammate loads the same project context as a regular session (CLAUDE.md, MCP servers, skills) but does **not** inherit the lead's conversation history.

---

## Subagents vs. agent teams

|                   | Subagents | Agent teams |
|---|---|---|
| **Context**       | Own window; results return to caller | Own window; fully independent |
| **Communication** | Report back to main agent only | Message each other directly |
| **Coordination**  | Main agent manages all work | Shared task list, self-coordination |
| **Best for**      | Focused tasks where only the result matters | Complex work requiring discussion and collaboration |
| **Token cost**    | Lower (results summarized back) | Higher (each teammate is a separate Claude instance) |

**Decision rule:** Use subagents when workers just need to report results. Use agent teams when teammates need to share findings, challenge each other, and coordinate independently.

---

## Best use cases

- **Research and review**: multiple teammates investigate different aspects of a problem simultaneously, then share and challenge findings
- **New modules or features**: each teammate owns a separate piece without stepping on each other
- **Debugging with competing hypotheses**: teammates test different theories in parallel, debate like a scientific inquiry, and converge faster
- **Cross-layer coordination**: changes spanning frontend, backend, and tests, each owned by a different teammate

**When to avoid:** Sequential tasks, same-file edits, work with heavy dependencies, or anything where coordination overhead exceeds the benefit of parallelism.

---

## Display modes

- **In-process** (default fallback): all teammates run inside the main terminal. Shift+Down cycles through teammates. Works in any terminal.
- **Split panes**: each teammate gets its own tmux or iTerm2 pane. Requires tmux or iTerm2 with the `it2` CLI. Not supported in VS Code terminal, Windows Terminal, or Ghostty.
- **Auto** (default): uses split panes if already inside tmux, otherwise in-process.

---

## Task coordination

The shared task list is the central coordination mechanism:
- Tasks have three states: **pending**, **in progress**, **completed**
- Tasks can declare **dependencies** on other tasks — blocked tasks can't be claimed until dependencies are met
- The lead can **assign** tasks explicitly, or teammates **self-claim** the next available task
- File locking prevents race conditions when multiple teammates try to claim simultaneously
- The system automatically unblocks dependent tasks when prerequisites complete

---

## Quality gates (hooks)

Three hooks enforce rules at key moments:
- **TeammateIdle**: fires when a teammate is about to go idle; exit code 2 sends feedback and keeps them working
- **TaskCreated**: fires when a task is created; exit code 2 rejects creation with feedback
- **TaskCompleted**: fires when a task is marked complete; exit code 2 blocks completion with feedback

---

## Plan approval mode

For high-risk tasks, require teammates to plan before implementing. The teammate works in **read-only plan mode** until the lead approves. If rejected, the teammate revises and resubmits. Useful for: "only approve plans that include test coverage" or "reject plans that modify the database schema."

---

## Practical notes

- **Team size**: start with 3–5 teammates; 5–6 tasks per teammate is a productive ratio. More teammates means more communication overhead and token cost.
- **Context**: teammates load project CLAUDE.md and settings but not conversation history. Include task-specific details in the spawn prompt.
- **Models**: teammates don't inherit the lead's `/model` selection by default. Set "Default teammate model" in `/config` to change this.
- **Subagent definitions as teammates**: reference a project- or user-scoped subagent type when spawning. The teammate inherits that definition's tools allowlist and model, but `skills` and `mcpServers` frontmatter fields are not applied.
- **Avoid file conflicts**: break work so each teammate owns different files. Two teammates editing the same file causes overwrites.
- **Monitor actively**: check in on progress, redirect approaches that aren't working, and synthesize findings as they arrive.

---

## Known limitations (experimental)

- No session resumption: `/resume` and `/rewind` don't restore in-process teammates
- Task status can lag — teammates sometimes fail to mark tasks completed
- Shutdown is slow (teammates finish current request first)
- One team at a time; no nested teams
- Lead is fixed — can't transfer leadership
- Permissions set at spawn (can change individually afterward)

---

## Connections to the vault

- This is a concrete implementation of the **Fan-Out** and **Specialist Team** patterns from [[multi-agent-orchestration]]. The competing-hypotheses debugging example is a direct application of Pattern 2 with adversarial twist.
- [[gstack]]'s 23 specialist slash commands parallelize work within a single session; agent teams take parallelism to multiple sessions.
- The shared task list with dependencies mirrors project management conventions — similar to the Now/Next/Later backlog structure used in [[conley-potter]]'s GitHub Projects boards.
- **CLAUDE.md as shared context**: teammates load CLAUDE.md files from the working directory, meaning the vault's operating contract would automatically propagate to all teammates in a team working on vault-related code.
- The plan-approval gate is analogous to the vault's own PR-based review flow — no changes land without an explicit approve/merge decision.

> **Relevance to Conley's stack:** Claude Code is already Conley's primary development tool (used for DailyChew and The Grind). Agent teams could accelerate cross-layer work (frontend + backend + tests) once the feature stabilizes. The competing-hypotheses pattern is particularly useful for debugging DailyChew's multi-service pipeline (Inngest → LangGraph → TTS → GCS). Token cost is the main constraint — each teammate is a full Claude instance.
