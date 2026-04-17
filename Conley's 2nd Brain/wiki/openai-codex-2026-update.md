---
type: tool-analysis
domain: general
tags: [ai-tools, openai, codex, agentic-coding, competitor-analysis]
created: 2026-04-17
updated: 2026-04-17
sources: [Codex for (almost) everything.md]
---

# OpenAI Codex — April 2026 Update

**Related:** [[domain-general]], [[tech-stack]], [[opus-4-7-workflow]], [[gstack]]

*Source: OpenAI blog post — "Codex for (almost) everything," published April 15, 2026*

---

## What Changed

OpenAI released a major Codex app update on April 15, 2026, for 3M+ weekly developers. The update moves Codex from a focused coding assistant toward a broader agentic workspace that operates alongside the developer's full environment.

---

## New Capabilities

### Computer Use (Background Agents)
- Codex can now operate apps on your Mac with its own cursor — seeing, clicking, and typing
- Multiple agents can work in parallel without interfering with the user's own work in other apps
- Use cases: iterating on frontend changes, testing apps, working with apps that don't expose an API

### In-App Browser
- Native browser inside the Codex app; users can comment directly on pages to give precise agent instructions
- Current focus: frontend and game development (localhost apps)
- Planned expansion to full browser command beyond localhost

### Image Generation
- Integrated gpt-image-1.5 for generating and iterating on images within the same workflow
- Useful for: product concept mockups, frontend designs, games

### Plugins (90+ new)
- Combines skills, app integrations, and MCP servers
- Notable new integrations: Atlassian Rovo (JIRA), CircleCI, CodeRabbit, GitLab Issues, Microsoft Suite, Neon by Databricks, Remotion, Render, Superpowers

### Full Development Lifecycle Features
- GitHub PR review comment handling
- Multiple terminal tabs
- Remote devboxes via SSH (alpha)
- Rich previews for PDFs, spreadsheets, slides, and docs in the sidebar
- Summary pane for tracking agent plans, sources, and artifacts

### Memory and Continuity
- **Memory (preview):** remembers preferences, corrections, and previously gathered context across sessions — reduces setup time on recurring tasks
- **Automations expansion:** reuse existing conversation threads, preserving context built up over time; Codex can schedule future work and wake up automatically to continue long-term tasks across days or weeks
- **Proactive suggestions:** using context from projects, plugins, and memory, Codex suggests how to start the work day or where to pick up on a previous project (pulling from Google Docs, Slack, Notion, codebase)

---

## Availability

- Rolling out to Codex desktop app users signed in with ChatGPT (April 2026)
- Memory and context-aware suggestions: Enterprise, Edu, EU/UK — coming soon
- Computer use: macOS initially; EU/UK rollout coming

---

## Strategic Context

### What This Signals

Codex is consolidating the developer's entire workflow — code, browser, terminal, CI, docs, PR review — into one agentic workspace. The memory and automation features (reusing threads, scheduling future work, waking up autonomously) position Codex as a persistent background agent, not just a session-by-session assistant.

The proactive suggestions feature is philosophically aligned with what [[thought-leader-engine]] describes as the "heartbeat" pattern in OpenClaw — an agent that pushes rather than waits to be invoked.

### Comparison to Claude Code + gstack

The Codex update competes most directly with the Claude Code + [[gstack]] setup that Garry Tan and others in the Claude ecosystem are building. Claude Code's advantages: deeper reasoning in agentic runs, stronger on-task discipline (Karpathy-style CLAUDE.md rules), and the gstack sprint framework. Codex's advantages: tighter OpenAI ecosystem integration, native computer use at launch, the 3M developer install base.

### Relevance to ACE

- The memory/automation features describe the same "persistent agent" pattern ACE uses for The Proactive Ghost (via [[thought-leader-engine]] and OpenClaw)
- Multi-agent parallel work (multiple background agents without interfering with the user) validates the parallel sprint model [[gstack]] describes
- Codex's MCP plugin architecture is the same integration model OpenClaw uses (ACE tech stack)
- Not a direct threat to ACE Phase I — ACE operates on n8n for workflow automation, not agentic coding. Relevance increases in Phase III when OpenClaw agentic workflows become central.

> **Note:** Codex's capabilities described here apply to the desktop app (requiring ChatGPT sign-in), not the terminal/editor version of Codex CLI. These are distinct products.
