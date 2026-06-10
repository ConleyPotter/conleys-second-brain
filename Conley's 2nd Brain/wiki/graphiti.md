---
type: tool-analysis
domain: general
tags: [knowledge-graph, temporal, ai-agents, memory, neo4j, langraph, mcp, zep, graphiti]
created: 2026-06-07
updated: 2026-06-07
sources: [graphiti-google-ai-mode-2026-06-07.md]
---

# Graphiti

**Related:** [[multi-agent-orchestration]], [[second-brain-mcp-server]], [[tech-stack]]

---

## What Graphiti is

Graphiti is an open-source framework for building **temporally aware, multi-tenant knowledge graphs** for AI agents. It solves a specific problem: agents need persistent memory that tracks how facts change over time, not just a static snapshot of what's currently true.

Built by the team behind **Zep** (which provides the managed enterprise layer on top of Graphiti), it is designed to serve as a central memory system for agentic workflows.

---

## How it works

### Episode ingestion

Graphiti ingests discrete pieces of information — documents, chat logs, or JSON — and decomposes them into **entities**, **attributes**, and **relationships** within a graph structure.

### Temporal awareness

Every fact is timestamped. When new information contradicts or updates old information, Graphiti marks past facts as **superseded** rather than deleting them. This preserves an accurate historical timeline and enables point-in-time queries.

### Incremental updates

New information is added to the graph instantly, without batch recomputation. There is no need to rebuild or reprocess the entire dataset when a new episode arrives.

---

## Retrieval model

Graphiti uses a **hybrid retrieval** approach combining three methods in a single query:

1. **Semantic vector search** — meaning-based similarity
2. **BM25 keyword search** — term-frequency matching
3. **Structural graph traversal** — following relationships between entities

This produces sub-second answers and supports **point-in-time queries** — an agent can answer "What did we know about this client in Q2 of 2024?" by querying the temporal state of the graph at that date.

---

## Agent integration

Graphiti integrates into multi-agent workflows (specifically mentions LangGraph compatibility) and exposes itself as a central memory system via the **Model Context Protocol (MCP)**.

This makes it a drop-in persistent memory layer for agent orchestration systems that already use MCP for tool/context management.

---

## Infrastructure requirements

Graphiti requires a **graph database** backend. Supported options:

| Database | Notes |
|---|---|
| **Neo4j** | Primary pairing; Neo4j Aura (free tier) available for development |
| **FalkorDB** | Alternative graph database option |

---

## Zep — the enterprise layer

Graphiti is the open-source foundation for **Zep** ("The Context Lake"), which adds:

- Managed ingestion pipelines
- Governance and access controls
- Scaling infrastructure for production agentic memory

Zep positions itself as the enterprise-grade wrapper around Graphiti's core temporal graph engine.

---

## Vault relevance

Graphiti is directly relevant to DailyChew's planned v3.0 knowledge layer. The current DailyChew roadmap includes a phased knowledge architecture:

- **v0** — inject source dates + consistency gate (shipping now)
- **v2.0** — persistent claim-based knowledge store on Supabase/pgvector
- **v3.0** — temporal knowledge graph using **Graphiti + Kuzu**

The Graphiti overview confirms the framework's core capabilities align with what DailyChew v3.0 needs: temporal fact tracking (when was this true?), incremental updates (no batch recomputation when new episodes ingest), and hybrid retrieval (semantic + keyword + graph traversal).

Notable differences from the current plan: the DailyChew v3.0 design names **Kuzu** as the graph database, while Graphiti primarily pairs with **Neo4j** or **FalkorDB**. Whether Graphiti's graph layer can be swapped to Kuzu (an embedded graph database) would need investigation before committing to this stack combination.

The MCP integration is also relevant to the second brain's own architecture — Graphiti could theoretically serve as a temporal memory layer for the vault's agent pipeline, though that is not on any current roadmap.

> **Note:** Source is a Google AI Mode overview, not primary documentation. Cross-reference with the Graphiti GitHub repo and Zep docs before making engineering decisions.
