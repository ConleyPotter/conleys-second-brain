# Graphiti — Google AI Mode Shared Result

**Source URL:** https://share.google/aimode/3bTJZNY8iSvXN4Dzr
**Source type:** Google AI Mode shared result (AI-generated overview)
**Captured:** 2026-06-07

---

## Original query

Graphiti

## AI Mode response

Graphiti is a powerful open-source framework designed for building temporally aware, multi-tenant knowledge graphs for AI agents. Unlike static knowledge retention, Graphiti tracks how information, entities, and relationships evolve, enabling AI to maintain persistent, real-time memory.

### How It Works

- **Episode Ingestion:** It ingests discrete pieces of information (documents, chat logs, or JSON) and breaks them down into entities, attributes, and relationships.
- **Temporal Awareness:** Graphiti stamps when facts are true. When new information contradicts or updates old information, it marks the past facts as superseded rather than deleting them, preserving an accurate historical timeline.
- **No Batch Recomputation:** New information is incrementally added to the graph instantly, without needing to rebuild or recompute the entire dataset.

### The Graphiti Advantage

- **Hybrid Retrieval:** Queries rely on a mix of semantic vector search, BM25 keyword search, and structural graph traversal in a single query, providing sub-second answers.
- **Point-in-Time Queries:** AI can answer time-specific questions like "What did we know about this client in Q2 of 2024?"
- **Agent Memory:** It integrates seamlessly into multi-agent workflows (like LangGraph) and acts as a central memory system via the Model Context Protocol (MCP).

### Integrations & Ecosystem

Under the hood, Graphiti requires a graph database to store and process the nodes and edges. It is primarily paired with Neo4j or FalkorDB.

At an enterprise level, Graphiti serves as the open-source foundation for Zep (The Context Lake), which provides managed ingestion, governance, and scaling for agentic memory systems.

### Referenced sources

- GitHub (Graphiti repo)
- Presidio
- Medium
- www.getzep.com (Zep)
- YouTube: "Build an AI Knowledge Graph with Graphiti + Neo4j" by Pradip Nichite (Aug 2025)
