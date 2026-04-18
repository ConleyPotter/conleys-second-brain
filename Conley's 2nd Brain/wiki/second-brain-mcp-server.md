---
type: synthesis
domain: general
tags: [mcp, second-brain, gstack, claude-code, workflow, ai-infrastructure]
created: 2026-04-18
updated: 2026-04-18
sources: []
---

# Second Brain as MCP Server — Integration with gstack

**Related:** [[gstack]], [[llm-wiki-pattern]], [[tech-stack]], [[opus-4-7-workflow]], [[brand-voice]], [[ace-overview]], [[operating-doctrine-2026]]

---

## The Problem This Solves

Right now, the second brain and gstack operate in separate contexts. Every Claude Code session using gstack starts cold — no awareness of the operating doctrine, the 15-hour constraint, the brand voice, the ACE phase roadmap, or any of the strategic context that lives in this wiki. Conley has to paste it in manually or trust the model to work without it.

An MCP (Model Context Protocol) server wrapping this wiki closes that gap. Instead of context that only exists inside second brain sessions, the wiki becomes a live resource any connected Claude Code session can query — including every gstack sprint.

---

## What an MCP Server for This Wiki Looks Like

The wiki is already well-structured for this: flat directory, consistent frontmatter, two navigation files (index.md and log.md), and a governing schema in CLAUDE.md. That structure is trivially wrappable.

**Tools the server would expose:**

| Tool | What it does |
|---|---|
| `wiki_read(page_name)` | Return full markdown content of a named page |
| `wiki_search(query)` | Full-text search across all wiki pages; returns matching excerpts and page names |
| `wiki_list(domain?, type?)` | List pages matching optional domain or type filter |
| `wiki_write(page_name, content)` | Write or update a page; validates frontmatter against CLAUDE.md schema |
| `wiki_append_log(entry)` | Append a structured entry to log.md |
| `wiki_read_index()` | Return the full index — the fastest way to orient to the wiki's shape |
| `wiki_read_schema()` | Return CLAUDE.md — the operating contract for what the wiki is and how it works |

**Implementation path:** A lightweight TypeScript MCP server (same runtime gstack uses — Bun v1.0+) backed by the local git repo. Reads directly from `Conley's 2nd Brain/wiki/`. All writes go through the same schema validation logic documented in CLAUDE.md. Runs as a local process. Registered in `~/.claude/settings.json` under `mcpServers`.

This is a one-file server. The wiki's discipline (flat structure, consistent frontmatter, two navigation files) is what makes it buildable cheaply.

---

## How gstack Connects to It

Once the MCP server is registered, Claude Code sessions automatically have access to the tools. The integration point is CLAUDE.md — the same file gstack reads at session start. Adding a `## Second Brain` section tells every gstack skill that wiki context is available and how to use it.

```markdown
## Second Brain
Use the second brain MCP server for project context before planning or reviewing.
- Read [[operating-doctrine-2026]] before /office-hours or /autoplan
- Read [[brand-voice]] before any design or content work
- Read [[ace-overview]] and [[tech-stack]] for ACE-specific work
- Write learnings back via wiki_append_log after /retro
```

That's the full integration. The skills don't change — they just have access to richer context before they run.

---

## Which gstack Skills Benefit Most

**`/office-hours`**

The YC-style forcing questions work better when the model already knows the operator's constraints. Without the wiki, Claude has to infer what "practical" means for Conley. With wiki access, it knows: 15 hours/week operator ceiling, current ACE phase, revenue targets from [[financial-projections]], the decision filter from [[operating-doctrine-2026]] ("Does this compound or distract?"). The session reframes around real constraints rather than generic startup advice.

**`/autoplan` and `/plan-ceo-review`**

Strategic plans generated without ACE context tend toward scope expansion — more features, more infrastructure, more resources. The wiki gives the CEO reviewer a ground truth: what phase Conley is actually in, what tools already exist in [[tech-stack]], what the financial model looks like. `/plan-ceo-review`'s four modes (Expansion, Selective Expansion, Hold Scope, Reduction) land differently when the model knows the 15-hour ceiling is real.

**`/design-consultation` and `/design-review`**

Design work without brand context produces AI slop that doesn't sound like Conley. With `wiki_read("brand-voice")` available, the designer specialist can load the full brand voice guide — tone attributes, language patterns, what to avoid — before generating any copy or design direction. Same applies to portfolio work: the designer can check [[portfolio-website]] to understand what the current state is before recommending changes.

**`/retro`**

Currently, `/retro` writes to a local `~/.gstack/` file. With MCP access, the retro output can flow directly into log.md as a structured entry — same format as every other log entry, same place Conley looks to understand what happened. The boundary between "gstack session history" and "second brain record" disappears. One log.

**`/learn`**

gstack's `/learn` skill manages session-to-session memory. Right now that memory lives in a project-local JSONL file. With MCP write access, codebase-specific learnings (ACE's n8n quirks, OpenClaw's dispatch conventions, Supabase schema patterns) can be filed as wiki entries — type `synthesis` or a new type — rather than in a siloed file only one gstack install can read.

**`/cso`**

A security audit that can check [[tech-stack]] before running knows which APIs handle external data, which endpoints are authenticated, and what the data flow looks like at a macro level. Fewer false positives, more targeted threat modeling.

---

## The Compounding Effect

The wiki currently grows through discrete ingest sessions. The MCP server makes it grow continuously.

Every `/retro` appends a log entry. Every `/learn` creates or updates a page. Every `/office-hours` session that surfaces a key constraint could write it back. Over time, the wiki becomes a record not just of strategy documents Conley fed it but of every sprint, every architectural decision, every lesson from a failed QA run.

This is the structural difference between a knowledge base you maintain and one that maintains itself from the work you're already doing.

---

## Parallel Sprint Context

gstack supports 10–15 parallel Claude Code sessions via Conductor. With a shared MCP server, all of them read from the same wiki. One session running `/office-hours` on a Phase II content feature reads the same [[ace-overview]] and [[brand-voice]] as another session running `/review` on the enrichment pipeline. Consistency that would otherwise require manually seeding each session becomes automatic.

The flip side: write operations need coordination. Multiple sessions writing to the same wiki pages concurrently is a race condition. The simplest fix is to make write tools session-aware (each session writes to a draft that gets merged by a primary session) or to restrict writes to the session that owns the sprint log. This is a solvable problem, not a blocker.

---

## Implementation Sketch

**Phase 1 — Read-only (low effort, high value):**
1. Build the MCP server with read-only tools: `wiki_read`, `wiki_search`, `wiki_list`, `wiki_read_index`, `wiki_read_schema`
2. Register in `~/.claude/settings.json`
3. Add the `## Second Brain` block to this repo's CLAUDE.md
4. Test with a single `/office-hours` session — see if ACE constraints surface without manual pasting

**Phase 2 — Write-back:**
5. Add `wiki_write` and `wiki_append_log`
6. Validate frontmatter against the schema before any write
7. Commit writes to the git repo automatically (the repo is already the source of truth)
8. Wire `/retro` output to `wiki_append_log`

**Phase 3 — Intelligence layer:**
9. Add semantic search (embeddings over wiki pages) instead of grep-based full-text
10. Add a `wiki_query(question)` tool that synthesizes an answer from multiple pages — the same query workflow documented in CLAUDE.md, but callable from any Claude Code session

Phase 1 is a weekend project. Phase 3 is ACE Phase II territory.

---

## Open Questions

- **Schema enforcement on writes:** The current CLAUDE.md schema is prose-documented, not machine-readable. An MCP server enforcing it needs a structured representation. Worth formalizing as a JSON schema before building write tools.
- **Concurrent writes in parallel sprints:** See the Parallel Sprint Context section. Coordination mechanism TBD.
- **The `/learn` migration:** Does it make sense to move gstack's memory entirely into the wiki, or keep them separate and sync selectively? The wiki's schema is richer but the JSONL is more durable for high-frequency ephemeral learnings.
- **n8n integration:** n8n already watches `raw-sources/` conceptually (noted in CLAUDE.md as a future automation). The same n8n infrastructure could trigger on wiki writes from the MCP server — closing the loop between automated ingest, wiki maintenance, and gstack sprint output.

> **Note:** The MCP server described here does not yet exist. Everything from Phase 1 onward is a build decision. The architectural case is solid; the question is prioritization against ACE Phase I client acquisition work.
