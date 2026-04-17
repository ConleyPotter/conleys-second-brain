---
type: tool-analysis
domain: general
tags: [openai, codex, ai-tools, computer-use, agentic, developer-tools]
created: 2026-04-17
updated: 2026-04-17
sources: [Codex for (almost) everything.md]
---

# OpenAI Codex — April 2026 Update

**Related:** [[tech-stack]], [[opus-4-7-workflow]], [[gstack]], [[domain-general]]

*Source: OpenAI blog, published April 15, 2026. 3M+ developers weekly.*

---

## What Changed

OpenAI released a major update to the Codex desktop app (macOS/Windows) extending it beyond coding into a general-purpose developer agent. The update adds five capability categories:

---

## 1. Background Computer Use

Codex can now operate any app on your computer using its own cursor — sees, clicks, types. Multiple agents can run in parallel without interfering with the user's own work in other apps. Useful for: iterating on frontend changes, testing apps, working in software that doesn't expose an API.

Available: macOS initially; EU/UK rolling out soon. Requires ChatGPT sign-in.

---

## 2. In-App Browser and Image Generation

**In-app browser** — a real browser where users can comment directly on pages to give the agent precise visual instructions. Currently scoped to localhost web apps and games; expanding to full browser control over time.

**Image generation** — integrates gpt-image-1.5 for generating and iterating on images inside the same workflow as code: product concepts, frontend mockups, game assets.

---

## 3. Plugins — 90+

90+ additional plugins covering skills, app integrations, and MCP servers. Notable additions:
- **Dev workflow**: GitLab Issues, CircleCI, CodeRabbit
- **Project management**: Atlassian Rovo / JIRA, Microsoft Suite
- **Infrastructure**: Neon by Databricks, Render, Superpowers
- **Other**: Remotion

---

## 4. Software Development Lifecycle Features

- **PR review**: address GitHub review comments inside Codex
- **Multi-terminal**: multiple terminal tabs in one workspace
- **Remote devboxes** (alpha): SSH to remote development environments
- **File sidebar**: rich previews for PDFs, spreadsheets, slides, docs
- **Summary pane**: tracks agent plans, sources, and artifacts across a session

---

## 5. Memory and Long-Running Work

**Memory** — Codex remembers preferences, corrections, and information that took time to gather across sessions. Future tasks complete faster without re-explaining context. Rolling out to Enterprise/Edu/EU/UK users soon.

**Automations** — reuse existing conversation threads, preserving built-up context. Codex can schedule future work for itself and wake up automatically to continue long-term tasks across days or weeks. Teams use this for landing open PRs, following up on tasks, tracking fast-moving conversations across Slack/Gmail/Notion.

**Proactive suggestions** — Codex proposes how to start the work day or where to pick up on a previous project, based on projects, connected plugins, and memory. Example: identifies open Google Docs comments requiring attention, pulls context from Slack and Notion, surfaces a prioritized action list.

---

## Competitive Context

This release positions OpenAI Codex as a direct competitor to Claude Code's agentic development workflow — and a complement to it. The feature surface overlaps significantly with patterns described in [[opus-4-7-workflow]] (verification-first, extended autonomous runs) and [[gstack]] (specialist role pipeline, browser QA, parallel sprints).

Key differentiators vs. Claude Code:
- Codex: computer use at OS level (any app, parallel agents), tight ChatGPT/memory integration, scheduled autonomous work
- Claude Code / gstack: richer sprint methodology, cross-agent coordination via /pair-agent, open-source skill layer

The scheduled work capability — Codex waking itself up to continue long-term tasks across days and weeks — is the most forward-looking feature. It points toward a model where developer agents operate more like background workers than interactive assistants.

> **Relevance to ACE:** The computer use and memory features directly parallel ACE's HITL co-pilot thesis. If an agent can verify its own work (computer use for frontend, bash for backend), remember operator preferences, and run extended workstreams uninterrupted, the human gate compresses further toward final approval. Codex's automation roadmap is tracking toward the same endpoint as ACE's architecture, arriving via a different product path.
