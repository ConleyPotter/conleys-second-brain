# Claude Code Agent Teams Documentation

**Source URL:** https://code.claude.com/docs/en/agent-teams
**Captured:** 2026-06-08
**Source type:** Official Anthropic documentation

---

# Orchestrate teams of Claude Code sessions

Orchestrate teams of Claude Code sessions with shared tasks, inter-agent messaging, and centralized management.

> **Warning:** Agent teams are experimental and disabled by default. Enable them by adding `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` to your settings.json or environment. Agent teams have known limitations around session resumption, task coordination, and shutdown behavior.

Agent teams let you coordinate multiple Claude Code instances working together. One session acts as the team lead, coordinating work, assigning tasks, and synthesizing results. Teammates work independently, each in its own context window, and communicate directly with each other.

Unlike subagents, which run within a single session and can only report back to the main agent, you can also interact with individual teammates directly without going through the lead.

> Agent teams require Claude Code v2.1.32 or later.

## When to use agent teams

Agent teams are most effective for tasks where parallel exploration adds real value. The strongest use cases are:

- **Research and review**: multiple teammates can investigate different aspects of a problem simultaneously, then share and challenge each other's findings
- **New modules or features**: teammates can each own a separate piece without stepping on each other
- **Debugging with competing hypotheses**: teammates test different theories in parallel and converge on the answer faster
- **Cross-layer coordination**: changes that span frontend, backend, and tests, each owned by a different teammate

Agent teams add coordination overhead and use significantly more tokens than a single session. They work best when teammates can operate independently. For sequential tasks, same-file edits, or work with many dependencies, a single session or subagents are more effective.

### Compare with subagents

|                   | Subagents                                        | Agent teams                                         |
| :---------------- | :----------------------------------------------- | :-------------------------------------------------- |
| **Context**       | Own context window; results return to the caller | Own context window; fully independent               |
| **Communication** | Report results back to the main agent only       | Teammates message each other directly               |
| **Coordination**  | Main agent manages all work                      | Shared task list with self-coordination             |
| **Best for**      | Focused tasks where only the result matters      | Complex work requiring discussion and collaboration |
| **Token cost**    | Lower: results summarized back to main context   | Higher: each teammate is a separate Claude instance |

Use subagents when you need quick, focused workers that report back. Use agent teams when teammates need to share findings, challenge each other, and coordinate on their own.

## Enable agent teams

Agent teams are disabled by default. Enable them by setting the `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` environment variable to `1`, either in your shell environment or through settings.json:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

## Start your first agent team

After enabling agent teams, tell Claude to create an agent team and describe the task and the team structure you want in natural language. Claude creates the team, spawns teammates, and coordinates work based on your prompt.

Example: "I'm designing a CLI tool that helps developers track TODO comments across their codebase. Create an agent team to explore this from different angles: one teammate on UX, one on technical architecture, one playing devil's advocate."

From there, Claude creates a team with a shared task list, spawns teammates for each perspective, has them explore the problem, synthesizes findings, and attempts to clean up the team when finished.

The lead's terminal lists all teammates and what they're working on. Use Shift+Down to cycle through teammates and message them directly.

## Control your agent team

### Choose a display mode

Agent teams support two display modes:

- **In-process**: all teammates run inside your main terminal. Use Shift+Down to cycle through teammates.
- **Split panes**: each teammate gets its own pane. You can see everyone's output at once and click into a pane to interact directly. Requires tmux or iTerm2.

The default is "auto", which uses split panes if already inside a tmux session, and in-process otherwise.

### Specify teammates and models

Claude decides the number of teammates to spawn based on your task, or you can specify exactly what you want. Teammates don't inherit the lead's /model selection by default. Set "Default teammate model" in /config to change this.

### Require plan approval for teammates

For complex or risky tasks, require teammates to plan before implementing. The teammate works in read-only plan mode until the lead approves their approach. If rejected, the teammate stays in plan mode, revises, and resubmits.

### Talk to teammates directly

Each teammate is a full, independent Claude Code session. You can message any teammate directly.

- **In-process mode**: use Shift+Down to cycle through teammates
- **Split-pane mode**: click into a teammate's pane

### Assign and claim tasks

The shared task list coordinates work across the team. Tasks have three states: pending, in progress, and completed. Tasks can also depend on other tasks.

The lead can assign tasks explicitly, or teammates can self-claim. Task claiming uses file locking to prevent race conditions.

### Shut down teammates

To gracefully end a teammate's session: "Ask the researcher teammate to shut down." The lead sends a shutdown request. The teammate can approve or reject with an explanation.

### Clean up the team

Ask the lead to clean up. This removes the shared team resources. Always use the lead to clean up — teammates should not run cleanup.

### Enforce quality gates with hooks

Use hooks to enforce rules:

- **TeammateIdle**: runs when a teammate is about to go idle. Exit with code 2 to send feedback and keep the teammate working.
- **TaskCreated**: runs when a task is being created. Exit with code 2 to prevent creation and send feedback.
- **TaskCompleted**: runs when a task is being marked complete. Exit with code 2 to prevent completion and send feedback.

## How agent teams work

### Architecture

An agent team consists of:

| Component     | Role                                                                                    |
| :------------ | :-------------------------------------------------------------------------------------- |
| **Team lead** | The main Claude Code session that creates the team, spawns teammates, and coordinates work |
| **Teammates** | Separate Claude Code instances that each work on assigned tasks                            |
| **Task list** | Shared list of work items that teammates claim and complete                                |
| **Mailbox**   | Messaging system for communication between agents                                         |

Teams and tasks are stored locally:
- Team config: `~/.claude/teams/{team-name}/config.json`
- Task list: `~/.claude/tasks/{team-name}/`

The team config contains a `members` array with each teammate's name, agent ID, and agent type. Teammates can read this file to discover other team members.

### Use subagent definitions for teammates

When spawning a teammate, you can reference a subagent type from any subagent scope: project, user, plugin, or CLI-defined. The teammate honors that definition's tools allowlist and model. Team coordination tools (SendMessage, task management) are always available.

Note: `skills` and `mcpServers` frontmatter fields in a subagent definition are not applied when running as a teammate — teammates load skills and MCP servers from project and user settings.

### Permissions

Teammates start with the lead's permission settings. If the lead runs with `--dangerously-skip-permissions`, all teammates do too. You can change individual teammate modes after spawning.

### Context and communication

Each teammate has its own context window. When spawned, a teammate loads the same project context as a regular session: CLAUDE.md, MCP servers, and skills. The lead's conversation history does not carry over.

How teammates share information:
- **Automatic message delivery**: messages delivered automatically to recipients
- **Idle notifications**: teammate auto-notifies the lead when stopping
- **Shared task list**: all agents see task status and claim available work
- **Teammate messaging**: send a message to one specific teammate by name

### Token usage

Agent teams use significantly more tokens than a single session. Each teammate has its own context window, and token usage scales with the number of active teammates. For research, review, and new feature work, the extra tokens are usually worthwhile.

## Use case examples

### Run a parallel code review

Split review criteria into independent domains: security, performance, and test coverage. Each reviewer works from the same PR but applies a different filter. The lead synthesizes findings.

### Investigate with competing hypotheses

Spawn 5 agent teammates to investigate different hypotheses about a bug. Have them talk to each other to try to disprove each other's theories, like a scientific debate. The debate structure fights anchoring bias.

## Best practices

- **Give teammates enough context**: include task-specific details in the spawn prompt (teammates don't inherit conversation history)
- **Choose an appropriate team size**: start with 3-5 teammates; 5-6 tasks per teammate is a good balance
- **Size tasks appropriately**: not too small (coordination overhead exceeds benefit), not too large (too long without check-ins)
- **Wait for teammates to finish**: sometimes the lead starts implementing instead of waiting
- **Start with research and review**: if new to agent teams, start with tasks that don't require writing code
- **Avoid file conflicts**: break work so each teammate owns different files
- **Monitor and steer**: check in on progress, redirect as needed

## Limitations

- **No session resumption with in-process teammates**: /resume and /rewind do not restore in-process teammates
- **Task status can lag**: teammates sometimes fail to mark tasks as completed
- **Shutdown can be slow**: teammates finish their current request before shutting down
- **One team at a time**: a lead can only manage one team
- **No nested teams**: teammates cannot spawn their own teams
- **Lead is fixed**: can't promote a teammate to lead or transfer leadership
- **Permissions set at spawn**: all teammates start with the lead's permission mode
- **Split panes require tmux or iTerm2**: not supported in VS Code terminal, Windows Terminal, or Ghostty

> CLAUDE.md works normally: teammates read CLAUDE.md files from their working directory.
