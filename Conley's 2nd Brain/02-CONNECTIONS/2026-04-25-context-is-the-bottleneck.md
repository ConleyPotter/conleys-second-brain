---
type: connection
connection-type: C
sources:
  - llm-wiki-pattern.md
  - second-brain-mcp-server.md
  - gstack.md
  - opus-4-7-workflow.md
created: 2026-04-25
tags:
  - ai-workflow
  - context
  - second-brain
  - agentic
  - gstack
---

# The Bottleneck Is Context, Not Intelligence

**Bridge:** Four separate pages in this wiki — the LLM wiki pattern, the MCP server synthesis, gstack, and Boris Cherny's Opus 4.7 workflow notes — all independently converge on the same unnamed insight: the people building the best AI workflows are winning by investing in context infrastructure, not by waiting for better models.

**Potential hook:** "Everyone chasing the best model is optimizing the wrong variable. The LLM wiki pattern, gstack, and Cherny's Opus 4.7 workflow notes all say the same thing from different angles: the bottleneck is structured context, not intelligence. Build the system that tells the model what it already knows about you. The model figures out the rest."

**Source notes:**
- [[llm-wiki-pattern]]
- [[second-brain-mcp-server]]
- [[gstack]]
- [[opus-4-7-workflow]]

**Why this matters:** Each page names a different piece of this: the LLM wiki pattern says "knowledge compiled once and kept current" beats RAG retrieval from scratch; the MCP server synthesis says gstack sessions start cold without wiki context and the MCP server closes that gap; gstack's 23 slash commands only produce consistent quality because they all operate within a shared sprint framework (consistent context enforces behavior); Cherny's verification-first workflow says the reason autonomous runs fail isn't model capability — it's that the model can't verify its own work without the right tools being present. None of these pages name the shared principle. The shared principle is: **AI capability is only as good as the context frame it operates in, and context frames are things you build, not things models come with**. That insight applies directly to ACE's HITL architecture — the reason the human gate exists isn't because the model isn't smart enough, it's because the model doesn't have enough context to know when it's wrong.
