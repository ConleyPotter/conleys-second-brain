# Claude Code Sub-Agents — Official Documentation

**Source:** https://code.claude.com/docs/en/sub-agents
**Captured:** 2026-06-08
**Type:** Official product documentation (Anthropic)

---

## Overview

Sub-agents are specialized AI assistants in Claude Code that handle specific types of tasks. Each runs in its own context window with a custom system prompt, specific tool access, and independent permissions. When Claude encounters a task matching a sub-agent's description, it delegates to that sub-agent, which works independently and returns results.

Sub-agents help you:
- **Preserve context** by keeping exploration and implementation out of your main conversation
- **Enforce constraints** by limiting which tools a sub-agent can use
- **Reuse configurations** across projects with user-level sub-agents
- **Specialize behavior** with focused system prompts for specific domains
- **Control costs** by routing tasks to faster, cheaper models like Haiku

## Built-in Sub-agents

### Explore
- **Model:** Haiku (fast, low-latency)
- **Tools:** Read-only (denied Write and Edit)
- **Purpose:** File discovery, code search, codebase exploration
- Thoroughness levels: quick, medium, very thorough
- Skips CLAUDE.md and git status for speed

### Plan
- **Model:** Inherits from main conversation
- **Tools:** Read-only (denied Write and Edit)
- **Purpose:** Codebase research for planning mode
- Cannot spawn other sub-agents (prevents infinite nesting)

### General-purpose
- **Model:** Inherits from main conversation
- **Tools:** All tools
- **Purpose:** Complex research, multi-step operations, code modifications
- Used when tasks need both exploration and modification

### Other built-ins
- **statusline-setup** (Sonnet): configures status line via `/statusline`
- **claude-code-guide** (Haiku): answers questions about Claude Code features

## Creating Custom Sub-agents

### Methods
1. **`/agents` command** — interactive UI with guided setup or Claude generation
2. **Manual Markdown files** — YAML frontmatter + system prompt body
3. **`--agents` CLI flag** — JSON definition, session-only, not saved to disk
4. **Managed settings** — organization-wide deployment
5. **Plugins** — installed with plugin system

### Scope/Priority (highest → lowest)
1. Managed settings (organization-wide)
2. `--agents` CLI flag (current session)
3. `.claude/agents/` (current project)
4. `~/.claude/agents/` (all your projects)
5. Plugin `agents/` directory

### File Format

```markdown
---
name: code-reviewer
description: Reviews code for quality and best practices
tools: Read, Glob, Grep
model: sonnet
---

You are a code reviewer. When invoked, analyze the code...
```

### Supported Frontmatter Fields

| Field | Required | Description |
|---|---|---|
| `name` | Yes | Unique identifier (lowercase + hyphens) |
| `description` | Yes | When Claude should delegate to this sub-agent |
| `tools` | No | Allowlist of tools; inherits all if omitted |
| `disallowedTools` | No | Denylist of tools |
| `model` | No | Model: sonnet, opus, haiku, full ID, or inherit (default) |
| `permissionMode` | No | default, acceptEdits, auto, dontAsk, bypassPermissions, plan |
| `maxTurns` | No | Maximum agentic turns |
| `skills` | No | Skills to preload at startup |
| `mcpServers` | No | MCP servers (inline definitions or references) |
| `hooks` | No | Lifecycle hooks scoped to the sub-agent |
| `memory` | No | Persistent memory scope: user, project, or local |
| `background` | No | true = always run as background task |
| `effort` | No | low, medium, high, xhigh, max |
| `isolation` | No | worktree = isolated git worktree copy |
| `color` | No | Display color in UI |
| `initialPrompt` | No | Auto-submitted first turn when running as main agent |

### Model Resolution Order
1. `CLAUDE_CODE_SUBAGENT_MODEL` environment variable
2. Per-invocation `model` parameter
3. Sub-agent definition's `model` frontmatter
4. Main conversation's model

## Key Capabilities

### Tool Control
- **Allowlist:** `tools: Read, Grep, Glob, Bash`
- **Denylist:** `disallowedTools: Write, Edit`
- Can restrict which sub-agents a coordinator can spawn: `tools: Agent(worker, researcher)`
- Unavailable tools: Agent, AskUserQuestion, EnterPlanMode, ExitPlanMode, ScheduleWakeup

### MCP Server Scoping
- Inline definitions: scoped to sub-agent only (keeps tools out of main conversation context)
- String references: reuses parent session's connection
- Enterprise restrictions apply

### Permission Modes
- `default` — standard prompting
- `acceptEdits` — auto-accept file edits in working directory
- `auto` — background classifier reviews commands
- `dontAsk` — auto-deny prompts (explicitly allowed tools still work)
- `bypassPermissions` — skip all prompts (use with caution)
- `plan` — read-only exploration

### Persistent Memory
- Three scopes: user (`~/.claude/agent-memory/`), project (`.claude/agent-memory/`), local (CWD `.claude/agent-memory/`)
- Accumulates insights across conversations
- Sub-agent can read, write, and manage memory files
- Memory persists across sessions

### Hooks (Lifecycle Events)
- `PreToolUse` — before a tool runs (can block/modify)
- `PostToolUse` — after a tool runs (can post-process)
- `SubagentStart` — when sub-agent begins execution
- `SubagentStop` — when sub-agent finishes

### What Loads at Startup
Sub-agents receive:
- Their system prompt (markdown body)
- Working directory context
- Accessible MCP server tool descriptions
- CLAUDE.md files (project and user)
- User-level skills directory
- Git context (status, recent commits)

### Background/Foreground Execution
- Foreground (default): blocks main conversation until complete
- Background (`background: true`): runs concurrently, main conversation continues
- Background sub-agents appear in task list with color coding

### Worktree Isolation
- `isolation: worktree` — creates a temporary git worktree
- Sub-agent works on isolated branch (from default branch, not parent HEAD)
- Worktree auto-cleaned if no changes made
- Useful for speculative changes or parallel experimentation

## Patterns

### Forked Sub-agents
- Creates a sub-agent pre-loaded with main conversation context
- Used via @-mention or explicit delegation
- Gets snapshot of conversation, not live updates

### Example Use Cases (from docs)
- **Security auditor** — read-only, focused on vulnerability patterns
- **Documentation writer** — generates docs from code
- **Test generator** — writes tests with specific framework conventions
- **Monorepo navigator** — understands project structure
- **API developer** — follows team API conventions (preloaded skills)

### Disabling Sub-agents
- Enterprise: `disabledTools: ["Agent"]` in managed settings
- Per-sub-agent: `permissions.deny` rules with `Agent(type)` pattern
- Individual: remove `Agent` from tools list

## Related Features
- **Background agents** (`/en/agent-view`): parallel independent sessions
- **Agent teams** (`/en/agent-teams`): sessions that communicate with each other
- **Skills** (`/en/skills`): reusable knowledge modules
- **Plugins** (`/en/plugins`): installable packages with sub-agents
- **Hooks** (`/en/hooks`): lifecycle event handlers
