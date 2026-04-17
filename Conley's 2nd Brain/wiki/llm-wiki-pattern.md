---
type: synthesis
domain: general
tags: [ai-workflow, knowledge-base, llm, wiki, methodology]
created: 2026-04-17
updated: 2026-04-17
sources: [CLAUDE.md from Kaparthy.md]
---

# LLM Wiki Pattern

**Related:** [[domain-general]], [[tech-stack]], [[ace-overview]], [[opus-4-7-workflow]]

*Source: Andrej Karpathy — "LLM Wiki" pattern document (idea file, designed to be shared with LLM agents)*

---

## Core Idea

Most LLM knowledge tools use RAG: drop in documents, retrieve chunks at query time, generate answers from scratch on every question. Nothing accumulates. The LLM rediscovers the same knowledge every session.

The LLM Wiki pattern is different: **the LLM incrementally builds and maintains a persistent wiki** that sits between you and the raw sources. When a new source arrives, the LLM doesn't just index it — it reads it, integrates it into existing pages, updates cross-references, flags where new data contradicts old claims, and strengthens the synthesis. Knowledge is compiled once and kept current.

**The result is a compounding artifact.** The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything read so far. The wiki gets richer with every source and every question answered.

---

## Three-Layer Architecture

| Layer | What it is | Who owns it |
|---|---|---|
| **Raw sources** | Curated source documents (articles, papers, data) — immutable | You (curate and protect) |
| **Wiki** | LLM-generated markdown pages — summaries, entity pages, concept pages, synthesis | The LLM (creates and maintains) |
| **Schema** | CLAUDE.md / AGENTS.md — tells the LLM how the wiki is structured and what workflows to follow | You + LLM (co-evolve over time) |

The schema is the key configuration file. It's what makes the LLM a disciplined wiki maintainer rather than a generic chatbot.

---

## Core Operations

**Ingest** — Drop a new source into raw sources and tell the LLM to process it. The LLM reads the source, discusses key takeaways, writes a summary page, updates the index, updates relevant entity and concept pages (a single source may touch 10–15 pages), and appends to the log.

**Query** — Ask questions. The LLM reads the index to find relevant pages, synthesizes an answer with citations. Critically: good answers can be filed back into the wiki as new pages. Comparative analyses, connections discovered, insights that would otherwise disappear into chat history — all can compound into the knowledge base.

**Lint** — Periodically ask the LLM to health-check: contradictions between pages, stale claims superseded by newer sources, orphan pages with no inbound links, concepts mentioned without their own page, data gaps. The LLM is good at suggesting new questions and sources to find.

---

## Navigation Files

Two special files that scale as the wiki grows:

**index.md** — content-oriented catalog. Every page listed with a link, one-line summary, and optional metadata. Organized by category. The LLM reads the index first on every query to find relevant pages without needing RAG infrastructure. Works well at ~100 sources / hundreds of pages.

**log.md** — chronological, append-only record of all operations (ingests, queries, lint passes). Start each entry with a consistent prefix (e.g. `## [2026-04-02] ingest | Title`) to make it parseable with simple unix tools.

---

## Division of Labor

**You:** curate sources, direct the analysis, ask good questions, think about what it all means.

**The LLM:** everything else — summarizing, cross-referencing, filing, updating, keeping consistency across dozens of pages.

Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero.

---

## Optional Tooling

- **Obsidian** — wiki as a git repo of markdown files; graph view shows the wiki's shape (hubs, orphans, clusters); Obsidian Web Clipper converts web articles to markdown for easy sourcing
- **qmd** — local search engine for markdown files with hybrid BM25/vector search and LLM re-ranking; CLI or MCP server; useful when index.md alone isn't enough
- **Marp** — markdown-to-slide-deck format; useful for generating presentations directly from wiki content
- **Dataview** — Obsidian plugin that runs queries over page frontmatter for dynamic tables and lists

---

## Intellectual Lineage

Karpathy connects this to Vannevar Bush's **Memex** (1945) — a personal, curated knowledge store with associative trails between documents. Bush's vision was closer to this than to what the web became: private, actively curated, with connections between documents as valuable as the documents themselves. The part Bush couldn't solve was who does the maintenance. The LLM handles that.

---

## Meta: This Wiki Is an Instance

This second brain is a direct implementation of the LLM Wiki pattern:
- `raw-sources/` = the raw source layer (immutable)
- `wiki/` = the LLM-maintained artifact layer
- `CLAUDE.md` = the schema that makes this wiki maintainer disciplined rather than generic
- `index.md` and `log.md` = the exact navigation files Karpathy describes

The schema is co-evolved: when a convention proves awkward or a workflow step is missing, CLAUDE.md is updated to reflect how we actually work. See [[wiki-structure-planning]] for the structural evolution history.

> **Note:** The `qmd` search tool would become valuable once the wiki exceeds ~50 pages. Currently the index file handles navigation at moderate scale.
