# CLAUDE.md — 2nd Brain Schema

This file is the operating contract between you (Claude) and this knowledge base. Read it at the start of every session. Follow it precisely. When in doubt, refer back here.

---

## What this is

This is Conley Potter's personal second brain — a persistent, compounding wiki that currently documents the Autonomous Content Engine (ACE) and the surrounding context of Conley's identity, career, and projects. As the wiki matures, it will expand to cover all domains: personal growth, research, reading, and life broadly.

You (Claude) are the maintainer. Conley is the curator and director. He sources material, asks questions, and guides emphasis. You do the reading, writing, cross-referencing, and bookkeeping. Nothing valuable should disappear into chat history — good answers get filed back as pages.

---

## Directory structure

```
vault/
├── .claude/
├── Clippings/
│   CLAUDE.md                  ← this file (the schema)
├── Conley's 2nd Brain/ 
│   ├── wiki/                  ← all LLM-generated markdown pages (flat)
│   │   ├── index.md           ← catalog of all wiki pages
│   │   └── log.md             ← append-only chronological record
│   └── raw-sources/           ← immutable source documents (read, never modify)
```

**Rules:**

- Never modify files in `raw-sources/`. They are the source of truth.
- All wiki pages live flat inside `wiki/`. No subfolders until we decide otherwise.
- `index.md` and `log.md` are special files — always keep them current after every operation.

---

## Wiki page types

Every page uses a `type` frontmatter field. Current types in use:

|Type|Purpose|Example pages|
|---|---|---|
|`strategy`|High-level direction and thesis|`ace-overview.md`, `financial-projections.md`|
|`operations`|How something works day-to-day|`client-acquisition.md`, `ba-overview.md`|
|`tool-analysis`|Vendor/API/platform evaluation|`data-enrichment-apis.md`, `platform-comparison.md`|
|`marketing`|Campaigns, brand, channels|`campaign-plan.md`, `brand-voice.md`|
|`identity`|Person profile, career, public presence|`conley-potter.md`, `ba-team.md`|
|`project`|A distinct project with its own arc|`the-sentinel.md`, `adam-shop-incubator.md`|
|`asset`|Ready-to-use copy or deliverable|`upwork-portfolio.md`, `portfolio-website.md`|
|`synthesis`|Cross-cutting analysis worth keeping|`wiki-structure-planning.md`|
|`work-log`|Dated snapshot of professional activity — archival, never modified post-creation|`daily-recap-2026-04-15.md`, `weekly-recap-2026-04-06.md`|

**Rolling vs. archival:** Most pages are **rolling** — updated in place as new information arrives. Pages with type `work-log` are **archival** — created once, never modified after creation. When a new daily or weekly recap is ingested, update rolling pages (e.g., `ba-clients-pipeline.md`, `ba-overview.md`) with new information, then create the dated archival page as a record.

**Frontmatter template:**

```yaml
---
type: strategy
domain: ace          # ace | ba | personal | research | general
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
---
```

---

## index.md format

The index uses a header block followed by **section tables**. Match this structure exactly.

```markdown
# [Wiki Name] — Index

**Last updated:** YYYY-MM-DD
**Source count:** N
**Page count:** N

[One-paragraph description of what this wiki covers and who maintains it.]

---

## [Section Name]

| Page | Summary |
|---|---|
| [[page-name]] | One-line description |

## Source Files

| File | Type | Ingested |
|---|---|---|
| `filename.md` | Document type | YYYY-MM-DD |
```

**Section organization** (current):

- Core Strategy
- ACE Operations & Tech
- Marketing & Brand
- Identity & Public Presence
- Day Job (BA)
- Projects
- Personal
- Day Job Logs
- Meta
- Source Files

Add new sections as the wiki expands into new domains. Do not reorganize existing sections without flagging it to Conley first.

---

## log.md format

Append-only. **Newest entries at the bottom.** Each entry starts with a greppable prefix.

```
## [YYYY-MM-DD] operation | description
```

Operations: `init`, `ingest`, `query`, `lint`, `update`

**Log entry structure** (match the existing richness — these are not one-liners):

```markdown
## [YYYY-MM-DD] ingest | Source Title

**Source type:** Brief description of what the document is
**Pages created:** N (`page-name.md`, ...)
**Pages updated:** N (`page-name.md`, ...)

### What this source contains

[2–4 sentences on what the document covers. Call out specific data points, superseding information, and anything that contradicts existing pages.]

### What changed

[Bullet list of specific edits — what was added or rewritten in each affected page, and why.]

### Notable observations

[2–5 observations connecting this source to the broader wiki. Flag contradictions, patterns, open questions, and cross-domain connections.]
```

For `query` entries, log: what was asked, how it was answered, and whether a synthesis page was filed. For `lint` entries, log: issues found, pages fixed, suggestions made.

---

## Core workflows

### 1. Session start

Every session, before taking any action:

1. Read this file (`CLAUDE.md`).
2. Read the last 5–10 entries in `wiki/log.md` to understand recent activity.
3. Read `wiki/index.md` to orient to the current wiki shape.
4. Wait for Conley's instruction.

Do not begin editing files until given a task.

---

### 2. Ingest a source

When Conley points you to a file in `raw-sources/`:

1. **Read** the source fully.
2. **Discuss** — surface key takeaways, connections to existing pages, and anything that contradicts the wiki. Wait for Conley's input before writing.
3. **Write or update pages** — create a summary page if warranted; update all entity, concept, and project pages touched by the source. A single source may touch 5–15 pages.

**For recurring log sources (daily/weekly recaps specifically):**
1. Read the recap fully.
2. Update relevant rolling pages (`ba-clients-pipeline.md`, `ba-overview.md`, `ba-team.md`, etc.) with any new information — new clients, personnel changes, product developments, notable events.
3. Create the dated archival page (`daily-recap-YYYY-MM-DD.md` or `weekly-recap-YYYY-MM-DD.md`) as a structured summary.
4. Extract what changes standing pages or signals meaningful patterns. Noise stays in the raw source — not every granular detail belongs in the wiki.
4. **Check for superseding information** — if the source overrides something in an existing page, update that page and note the change explicitly.
5. **Update `index.md`** — increment source count and page count; add new pages to the correct section table; add a row to Source Files.
6. **Append to `log.md`** — use the full structured format above.

> **n8n automation opportunity:** An n8n workflow watching `raw-sources/` for new files could trigger the ingest conversation automatically, eliminating the manual "hey, new file" step. High value once the manual workflow is stable.

---

### 3. Answer a query

When Conley asks a question:

1. Read `index.md` to identify relevant pages.
2. Read those pages and synthesize an answer with citations (`[[page-name]]`).
3. Decide if the answer is worth keeping. If it's comparative, analytical, or likely to be asked again — file it as a `synthesis` page.
4. Update `index.md` and append to `log.md` if a new page was created.

---

### 4. Update a page directly

When Conley asks you to revise, expand, or correct an existing page:

1. Read the current page.
2. Make the edit.
3. Update the `updated` frontmatter date.
4. Append to `log.md` using operation type `update`.
5. Update `index.md` if the page's one-line summary has meaningfully changed.

---

### 5. Lint the wiki

When Conley asks for a health check:

1. Read all pages via `index.md`.
2. Report:
    - Orphan pages (no inbound links)
    - Contradictions between pages
    - Concepts mentioned repeatedly without their own page
    - Pages with stale information superseded by newer sources
    - Known gaps in tech-stack or project pages
3. Suggest 3–5 questions worth investigating or sources worth finding.
4. Append to `log.md` with operation type `lint`.

---

## Cross-linking conventions

- Use Obsidian wiki-link format: `[[page-name]]`
- Link on first mention within a page — not every occurrence
- Prefer linking to entity, project, and concept pages over source-summary pages
- If a page you want to link to doesn't exist yet, create a stub rather than leaving an unlinked reference

---

## Writing style

- Write for future Conley, not for the LLM. Assume he hasn't read the source.
- Be concise. Use bullets for facts, prose for analysis.
- Flag contradictions and open questions explicitly — don't smooth them over.
- Use `> **Note:**` blockquotes for uncertain claims or things needing verification.
- Match Conley's brand voice (see `[[brand-voice]]`): direct, technical-but-human, no corporate filler.

---

## Current scope and expansion path

**Active domains:**
- **ACE** — strategy, operations, marketing, identity, projects
- **BA (Day Job)** — professional operations, client pipeline, partners, team
- **Personal** — doctrine, relationships, body, inner work

**Expansion order** (as new sources arrive):

1. Personal — journaling, goals, psychology, self-improvement
2. Research — deep topic dives, reading notes
3. General knowledge — articles, podcasts, web clips

When a new domain becomes active, create a `domain` page for it and add a new section to `index.md`. Update this section of CLAUDE.md to reflect the new scope.

---

## Known pages needing attention

Track pages with open issues here so they aren't forgotten between sessions:

- `[[tech-stack]]` — missing OpenClaw and LangGraph (added in ACE pivot; not yet reflected)
- `[[portfolio-website]]` — About page flagged as needing human revision; ACE description is highest-priority fix
- `[[the-sentinel]]` — status confirmed "aspirational / not yet built"; portfolio copy says "In Development" (inaccurate)
- `[[ba-products]]` — built by inference; needs validation against BA's actual rate card
- `[[ba-team]]` — roles inferred from behavioral observation; formal titles need verification
- `[[ba-clients-pipeline]]` — seeded from two sources only; full client base not yet represented
- `[[conley-potter]]` — wedding date June 12, 2026 (now 57 days out); update "engaged to Sami" to "married" post-June 12

Clear items from this list when resolved; add new ones as they're discovered.

---

## Evolution

This schema is a living document. When a convention proves awkward, a workflow step is missing, or the wiki outgrows its current structure, update this file to reflect how we actually work. The schema is only useful if it matches reality.