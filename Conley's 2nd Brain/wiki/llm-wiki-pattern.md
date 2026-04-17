---
type: synthesis
domain: general
tags: [second-brain, llm-wiki, knowledge-management, pattern, obsidian, rag]
created: 2026-04-17
updated: 2026-04-17
sources: [CLAUDE.md from Kaparthy.md]
---

# LLM Wiki Pattern

**Related:** [[second-brain-article]], [[wiki-structure-planning]], [[domain-general]], [[opus-4-7-workflow]]

*Source: "LLM Wiki" — pattern document for building personal knowledge bases using LLMs, associated with Andrej Karpathy*

---

## The Core Distinction

Most LLM-document workflows are RAG: upload files, retrieve relevant chunks at query time, generate an answer. The model rediscovers knowledge from scratch on every question. Nothing accumulates. NotebookLM, ChatGPT file uploads, and most RAG systems work this way.

The LLM wiki pattern is different. Instead of retrieval, the LLM **incrementally builds and maintains a persistent wiki** — a structured, interlinked collection of markdown files that sits between the user and raw sources. When a new source arrives, the LLM reads it, integrates the key information into existing pages, updates cross-references, and flags contradictions. Knowledge is compiled once and kept current.

**The key shift:** the wiki is a persistent, compounding artifact. The LLM is the programmer; the wiki is the codebase.

---

## Three Layers

**1. Raw sources** — immutable source documents. Articles, papers, data files, meeting transcripts. The LLM reads from them; never modifies them. Source of truth.

**2. The wiki** — LLM-generated markdown files. Summaries, entity pages, concept pages, syntheses. The LLM owns this layer entirely: creates pages, updates them as new sources arrive, maintains cross-references, resolves contradictions. The human reads; the LLM writes.

**3. The schema** — a configuration document (CLAUDE.md for Claude Code, AGENTS.md for Codex) that tells the LLM how the wiki is structured, what conventions to follow, and what workflows to run. This is what makes the LLM a disciplined wiki maintainer rather than a generic chatbot. The human and LLM co-evolve it over time.

---

## Three Operations

**Ingest.** Drop a new source into the raw collection. The LLM reads it, discusses key takeaways, writes or updates wiki pages, updates the index, appends to the log. A single source may touch 10–15 wiki pages. Can be done one at a time (high-involvement) or batched (low-supervision) — workflow style is documented in the schema.

**Query.** Ask questions against the wiki. The LLM reads relevant pages and synthesizes with citations. Key insight: **good answers can be filed back as new wiki pages.** Comparisons, analyses, connections discovered — these should compound in the knowledge base rather than disappear into chat history.

**Lint.** Periodic health check: contradictions between pages, stale claims superseded by newer sources, orphan pages with no inbound links, concepts lacking their own page, data gaps. The LLM also suggests new questions to investigate and new sources to find.

---

## Two Navigation Files

**index.md** — content-oriented. A catalog of every wiki page with a link, one-line summary, and optional metadata. Organized by category. The LLM reads this first on every query to find relevant pages, then drills into them. Works well at moderate scale (~100 sources, hundreds of pages) without embedding infrastructure.

**log.md** — chronological. Append-only record of every ingest, query, and lint pass. Each entry starts with a greppable prefix (`## [YYYY-MM-DD] ingest | Article Title`). Gives the LLM a timeline of recent activity so sessions don't start cold even without persistent memory.

---

## Division of Labor

**The human's job:** curate sources, direct the analysis, ask good questions, think about what it all means.

**The LLM's job:** everything else — summarizing, cross-referencing, maintaining consistency, updating pages, all the bookkeeping that humans reliably abandon.

The observation that drives the pattern: humans abandon wikis because maintenance burden grows faster than perceived value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero.

---

## Applicable Domains

The pattern isn't specific to any domain. It applies wherever knowledge accumulates over time and benefits from organization:

- **Personal** — goals, health, psychology, journaling, self-improvement
- **Research** — reading papers, building an evolving thesis over weeks or months
- **Reading** — filing chapters, building character/theme/plot-thread pages (fan wikis like Tolkien Gateway, built by one person in real time)
- **Business/team** — internal wiki fed by Slack threads, meeting transcripts, customer calls; LLM handles the maintenance no one wants to do
- **Competitive analysis, due diligence, trip planning, course notes, hobby deep-dives**

---

## Optional Infrastructure

**qmd** — local search engine for markdown files: hybrid BM25/vector search + LLM re-ranking, all on-device. Has both a CLI and an MCP server. Useful when the wiki grows past index-file scale.

**Obsidian** — the natural IDE for the wiki. Graph view shows shape and connectivity. Web Clipper converts web articles to markdown. Marp plugin generates slide decks. Dataview plugin runs queries over page frontmatter.

**Git** — version history, branching, and collaboration for free, since the wiki is just markdown files in a directory.

---

## Connection to This Wiki

This second brain is a direct implementation of the pattern. The raw-sources / wiki / CLAUDE.md layering maps exactly to the three-layer architecture above. The ingest, query, and lint workflows in CLAUDE.md implement the three operations. log.md and index.md are exactly the two navigation files described here.

The connection to Vannevar Bush's Memex (1945) is worth noting: a personal, curated knowledge store with associative trails between documents. Bush's vision was closer to this than to what the web became — private, actively curated, with connections as valuable as documents themselves. The part he couldn't solve was who does the maintenance. The LLM handles that.

> **Note:** The source document is explicitly abstract and implementation-agnostic. Directory structure, schema conventions, page formats, and tooling all depend on domain and preference. The document's only job is to communicate the pattern.
