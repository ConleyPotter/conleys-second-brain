---
type: synthesis
domain: general
tags: [claude-code, subagents, multi-agent, ai-tools, developer-workflow]
created: 2026-06-08
updated: 2026-06-08
sources: [claude-code-subagents-docs-2026-06-08.md]
---

# Claude Code Sub-Agents

Sub-agents are specialized AI assistants within Claude Code that run in their own context window — custom system prompt, restricted tool access, independent permissions. Claude delegates matching tasks automatically based on each sub-agent's description. The sub-agent works in isolation and returns only the summary, preserving the main conversation's context budget.

This is the primary mechanism for **context management** and **task specialization** in Claude Code sessions, and the architectural pattern behind the `gstack` sprint framework's 23 specialist commands.

## Why sub-agents matter

- **Context preservation** — exploration, search results, and log output stay in the sub-agent's window, not the main conversation
- **Tool constraints** — read-only sub-agents can't accidentally write; coordinators can restrict which sub-agent types get spawned
- **Cost control** — route routine tasks to Haiku instead of Opus
- **Reusable configurations** — user-level sub-agents (`~/.claude/agents/`) work across every project
- **Isolation** — `isolation: worktree` gives a sub-agent its own git branch for speculative changes

## Built-in sub-agents

| Sub-agent | Model | Tools | Purpose |
|---|---|---|---|
| **Explore** | Haiku | Read-only | Fast codebase search and analysis; three thoroughness levels (quick / medium / very thorough) |
| **Plan** | Inherited | Read-only | Research context during plan mode; cannot spawn children |
| **General-purpose** | Inherited | All | Complex multi-step tasks requiring both exploration and modification |
| **statusline-setup** | Sonnet | — | Configures the status line via `/statusline` |
| **claude-code-guide** | Haiku | — | Answers questions about Claude Code features |

Explore and Plan skip CLAUDE.md and git status to stay fast and cheap. All other sub-agents (built-in and custom) load both.

## Creating custom sub-agents

### Definition format

Markdown files with YAML frontmatter. The body becomes the system prompt.

```markdown
---
name: code-reviewer
description: Reviews code for quality and best practices
tools: Read, Glob, Grep
model: sonnet
---

You are a code reviewer. Analyze code and provide specific,
actionable feedback on quality, security, and best practices.
```

### Scope and priority

Sub-agents live at different scopes (highest priority wins when names collide):

1. **Managed settings** — organization-wide, deployed by admins
2. **`--agents` CLI flag** — current session only, JSON format, not saved to disk
3. **`.claude/agents/`** — project-level, version-controlled, team-shared
4. **`~/.claude/agents/`** — user-level, available everywhere
5. **Plugin `agents/`** — installed via the plugin system

Project sub-agents (`.claude/agents/`) are the team collaboration sweet spot — check them into version control so everyone uses the same configurations.

### Key configuration fields

| Field | What it controls |
|---|---|
| `name` | Unique identifier (lowercase + hyphens); hooks receive this as `agent_type` |
| `description` | When Claude should delegate (the routing signal) |
| `tools` / `disallowedTools` | Allowlist or denylist of available tools |
| `model` | `sonnet`, `opus`, `haiku`, full model ID, or `inherit` (default) |
| `permissionMode` | `default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions`, `plan` |
| `skills` | Skills preloaded at startup (full content injected, not just description) |
| `mcpServers` | MCP servers: inline definitions (scoped to sub-agent) or string references (shared connection) |
| `hooks` | Lifecycle hooks: `PreToolUse`, `PostToolUse`, `SubagentStart`, `SubagentStop` |
| `memory` | Persistent memory scope: `user`, `project`, or `local` |
| `isolation` | `worktree` = isolated git worktree for speculative changes |
| `background` | `true` = runs concurrently with main conversation |
| `effort` | `low`, `medium`, `high`, `xhigh`, `max` — overrides session level |
| `maxTurns` | Cap on agentic turns before forced stop |
| `initialPrompt` | Auto-submitted first user turn when running as main agent via `--agent` |

### Model resolution order

When Claude invokes a sub-agent, the model is resolved in priority order:
1. `CLAUDE_CODE_SUBAGENT_MODEL` environment variable
2. Per-invocation `model` parameter
3. Sub-agent definition's `model` frontmatter
4. Main conversation's model

## Advanced patterns

### Persistent memory

Sub-agents can accumulate insights across conversations via memory directories:
- **User scope:** `~/.claude/agent-memory/<name>/` — learnings available everywhere
- **Project scope:** `.claude/agent-memory/<name>/` — project-specific patterns
- **Local scope:** CWD `.claude/agent-memory/<name>/` — most constrained

### MCP server scoping

Inline MCP server definitions keep tool descriptions out of the main conversation's context — the sub-agent gets the tools, the parent doesn't see them. String references share an existing session connection.

```yaml
mcpServers:
  - playwright:
      type: stdio
      command: npx
      args: ["-y", "@playwright/mcp@latest"]
  - github  # reuses already-configured server
```

### Restricting sub-agent spawning

Coordinators can control which sub-agent types are spawnable:
- `tools: Agent(worker, researcher)` — only these two types
- `tools: Agent` — any sub-agent (unrestricted)
- Omit `Agent` entirely — no spawning allowed
- Sub-agents cannot spawn other sub-agents (prevents infinite nesting)

### Worktree isolation

`isolation: worktree` creates a temporary git worktree branched from the default branch (not the parent session's HEAD). The worktree auto-cleans if the sub-agent makes no changes. Useful for speculative refactors or parallel experimentation without polluting the main branch.

### Forked sub-agents

A forked sub-agent is pre-loaded with the main conversation's context — like spawning a specialist with full situational awareness. Used via @-mention or explicit delegation. Gets a snapshot, not live updates.

## Vault relevance

- **Direct parallel to Hyperagent's agent architecture.** Hyperagent named agents (the vault's own operating model) are conceptually similar — custom system prompts, tool restrictions, specialized behavior, persistent memory. Claude Code sub-agents are the local-machine counterpart to Hyperagent's cloud-hosted agents.
- **Connects to [[gstack]]** — Garry Tan's 23-command sprint framework builds on sub-agents. Each specialist command (CEO, Designer, QA, etc.) is a sub-agent with a focused prompt and tool set.
- **Extends [[multi-agent-orchestration]] patterns.** Sub-agents implement the Fan-Out and Specialist Team patterns at the IDE level rather than the infrastructure level.
- **Relevant to [[perplexity-agent-skills]]** — skill preloading via the `skills` frontmatter field mirrors Perplexity's progressive disclosure pattern for agent knowledge.
- **Context management is the core value proposition.** The same principle that makes the vault's wiki approach work (structured knowledge persisted outside of ephemeral context) applies here — sub-agents keep exploration artifacts in their own context window, preserving the main conversation's budget for decision-making.

## See also

- [[gstack]] — Claude Code sprint framework built on sub-agents
- [[multi-agent-orchestration]] — broader multi-agent patterns (Pipeline, Fan-Out, Specialist Team)
- [[perplexity-agent-skills]] — agent skill design patterns and progressive disclosure
- [[opus-4-7-workflow]] — workflow patterns for Claude, including verification-first approaches
