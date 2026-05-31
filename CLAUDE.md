# CLAUDE.md — 2nd Brain Schema

This file is the operating contract between you (Claude) and this knowledge base. Read it at the start of every session. Follow it precisely. When in doubt, refer back here.

---

## What this is

This is Conley Potter's personal second brain — a persistent, compounding wiki covering the Personal Brand Engine (PBE), career transition strategy, BA day job, Drone Enterprises, Long Game Studios, and personal operating doctrine. It began as an ACE-only knowledge base (the ACE freelance arbitrage system has since been pivoted to the PBE). As the wiki matures, it will expand to cover all domains: personal growth, research, reading, and life broadly.

You (Claude) are the maintainer. Conley is the curator and director. He sources material, asks questions, and guides emphasis. You do the reading, writing, cross-referencing, and bookkeeping. Nothing valuable should disappear into chat history — good answers get filed back as pages.

---

## Directory structure

```
vault/
├── .claude/
│   └── commands/              ← slash commands (wiki ingest + JARVIS workflows)
├── Clippings/
│   CLAUDE.md                  ← this file (knowledge base schema)
├── Conley's 2nd Brain/
│   ├── wiki/                  ← all LLM-generated knowledge pages (flat)
│   │   ├── index.md           ← catalog of all wiki pages
│   │   └── log.md             ← append-only chronological record
│   ├── raw-sources/           ← immutable source documents (read, never modify)
│   ├── 00-INBOX/              ← JARVIS: unprocessed captures
│   ├── 01-CAPTURES/           ← JARVIS: typed observations (5 subfolders)
│   │   ├── observations/
│   │   ├── reactions/
│   │   ├── patterns/
│   │   ├── questions/
│   │   └── numbers/
│   ├── 02-CONNECTIONS/        ← JARVIS: synthesized cross-capture insights
│   ├── 03-BRIEFS/             ← JARVIS: content ready to write
│   ├── 04-PUBLISHED/          ← JARVIS: archived posts + engagement data
│   └── 05-CLAUDE/             ← JARVIS: Claude working dir (CLAUDE.md + skills/)
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
domain: ace          # ace | ba | personal | research | general | drone-enterprises | long-game-studios
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
- General Knowledge
- Day Job (BA)
- Personal Brand Engine & Tech
- Marketing & Brand
- Identity & Public Presence
- Projects
- Personal
- Day Job Logs
- Drone Enterprises
- Long Game Studios
- Long Game Studios Dev Logs
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

### 6. Content production workflows (JARVIS)

This vault has a second layer: a content production system for capturing daily observations, finding connections between them, and generating content in Conley's voice.

**Before starting any JARVIS workflow**, read `Conley's 2nd Brain/05-CLAUDE/CLAUDE.md` in full. That file is the operating contract for the content production system. Use the slash commands `/jarvis-process-inbox`, `/jarvis-connections`, `/jarvis-brief`, and `/jarvis-write` to trigger each workflow.

**Cross-system rules:**
- Captures in `01-CAPTURES/` and briefs in `03-BRIEFS/` may link to wiki pages using `[[wiki-link]]` syntax — this works natively in Obsidian
- If a capture surfaces a significant new insight about ACE, BA, or personal context, surface it as a candidate for wiki ingest — don't silently discard it
- `04-PUBLISHED/` engagement data that reveals strong audience signals can update `brand-voice.md` in the wiki — ask Conley first
- `05-CLAUDE/CLAUDE.md` is the truth on voice rules; `brand-voice.md` in the wiki is the same content in wiki page format

---

## Vault Keeper — automated maintenance

The vault is maintained by a single Hyperagent agent called **Vault Keeper** (🗄️), which operates in four modes dispatched by trigger type. All modes share the same identity, knowledge, and hard constraints; only the job differs.

### Modes

| Mode | Trigger | What it does |
|---|---|---|
| **Capture** | Inbound email from Conley (link/note) | Fetches the link, saves a raw source, creates/updates wiki pages, updates `index.md` and `log.md`, opens a PR. Auto-merges clean ingests; leaves judgment calls for review. Replies to Conley with the page name and PR link. |
| **Dev-Log Capture** | Weekly schedule (Fri 5pm ET) or `[dev]`-tagged email | Synthesizes a changelog + build log from merged PRs, commits, releases, and CI runs across `daily-chew-ai` and `lgs-the-grind`. Writes an archival `work-log` page, updates rolling product overview pages, and ingests new ADRs. All under the `long-game-studios` domain. |
| **Audit** | Daily schedule (7am ET) + weekly deep audit (Sun 6am ET) | Daily: auto-fixes trivial drift (log/index sync, broken links, frontmatter, source attribution) via direct commit. Weekly: full catalog review — files `vault-steward`-labeled issues for judgment calls and up to 10 PRs (never auto-merged) for new wikis, splits, gap-fills, and domain changes. |
| **Remediate** | Daily schedule (12pm ET, staggered 5h after audit) | Processes open `vault-steward`-labeled issues using a content-aware confidence rubric (solvability, safety, rules compliance, truth/fidelity). Routes fixes to auto-merge (≥0.90), PR-for-review (0.70–0.89), or Slack approval in `#vault-steward` (<0.70). |

Multi-device input for Capture mode: direct email to the agent's inbound address, or the iCloud "Second Brain" Apple Shortcut (share sheet → email).

### Dev-log capture details

Long Game Studios is a studio brand, not a separate repo. Its two product repos are captured per-product under the `long-game-studios` domain:

- **`ConleyPotter/daily-chew-ai`** — DailyChew.AI, an AI-personalized daily news podcast. Active development; Conventional Commits; CI via lint + Playwright; Vercel auto-deploy on merge to main. ADRs in `docs/adr/`.
- **`ConleyPotter/lgs-the-grind`** — The Grind, a Phaser 3 browser game. Early-stage scaffolding. ADRs in `docs/adr/` (currently empty).

Neither repo cuts GitHub Releases yet — the agent synthesizes changelogs from merged PRs + commits. If Releases are adopted later, prefer release notes as the primary changelog source.

### Coordination labels

Labels coordinate across Vault Keeper's own runs. All runs must respect them.

**Issue labels:**

| Label | Meaning | Set by |
|---|---|---|
| `vault-steward` | Issue filed during an Audit run, awaiting Remediate processing | Audit mode |
| `remediator-claimed` | Remediate mode has resolved the issue (PR merged or commit landed; if still open, the linked PR is awaiting merge) | Remediate mode |
| `remediator-skipped` | Remediate mode examined and refused — hard-constraint hit or unparseable request even after a clarification round | Remediate mode |
| `claude-md-blocked` | Issue is blocked on a pending `claude-md-suggestion` PR | Remediate mode |
| `ingest-handoff` | Audit signal: Capture mode failed (raw source committed without corresponding wiki within 2 hours) | Audit mode |
| `remediator-handoff` | Audit signal: Remediate mode failed (open `vault-steward` issue sat more than 24 hours after a Remediate run should have executed) | Audit mode |

**PR labels:**

| Label | Meaning | Auto-merge eligible? |
|---|---|---|
| `vault-steward` | Audit-filed PR (new wikis, splits, gap-fills, domain changes) | Never — Conley merges |
| `remediator-review` | Medium-confidence Remediate PR awaiting Conley's review | Never — Conley merges |
| `remediator-needs-approval` | Low-confidence Remediate PR awaiting Slack approval | Never — Conley merges after Slack ack |
| `claude-md-suggestion` | Doctrine proposal touching only `CLAUDE.md` | Never — Conley merges manually |

High-confidence Remediate PRs (≥ 0.90) are not labeled — they go straight to auto-merge once required GitHub checks pass.

### Branch namespace

| Prefix | Mode | Pattern |
|---|---|---|
| `ingest/<slug>-<yyyymmdd>` | Capture | Content ingest branch |
| `devlog/<slug>-<yyyymmdd>` | Dev-Log Capture | Dev-log recap branch |
| `steward/...` | Audit | Audit-owned PR branches |
| `remediator/issue-<num>-<slug>` | Remediate | Regular fix branch |
| `remediator/claude-md-<slug>` | Remediate | Doctrine suggestion branch |

Treat any of these prefixed branches as expected in-flight agent work. Do not file noise issues about them, do not modify them, and do not treat their presence as a vault inconsistency.

### Re-filing protocol (Audit → Remediate)

Before the Audit mode files a new issue, it searches open issues for a match (by file path, content area, or its existing title patterns). If found with any of `remediator-claimed`, `remediator-skipped`, or `claude-md-blocked`, Audit does NOT re-file. For a `remediator-skipped` match, if conditions have genuinely changed (refined scope, new evidence), Audit may file a fresh new issue — never reopen the skipped one.

### Coordination failure detection

If the Audit mode observes an open `vault-steward` issue (no Remediate labels) that has sat for more than 24 hours after a Remediate run should have executed, it files a `remediator-handoff` issue (label `vault-steward`) describing what it observed. This mirrors the existing `ingest-handoff` pattern that signals a Capture mode failure.

### CLAUDE.md change policy

This file is the operating contract. Direct edits to `CLAUDE.md` as part of a per-issue fix are forbidden in Remediate mode. Remediate mode may PROPOSE changes via `claude-md-suggestion` draft PRs — but ONLY when the source issue explicitly proposes the change, or when drafting the fix exposes a real doctrine gap that blocks resolving the source issue. Such PRs:

- Contain ONLY the proposed `CLAUDE.md` edit; no other files.
- Are always draft PRs labeled `claude-md-suggestion`.
- Are always announced in Slack (`#vault-steward` in the ACE workspace) with the issue link, PR link, rationale, and proposed change.
- NEVER auto-merge regardless of confidence. Conley reviews and merges manually.
- Are capped at one open at a time. If one exists, Remediate mode labels the source issue `claude-md-blocked` and waits.

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
- **Personal Brand Engine (PBE)** — the unified ACE + TLE successor; public presence building, open source portfolio, content automation, career transition
- **Career Transition** — strategy, target companies, resume, LinkedIn positioning
- **BA (Day Job)** — professional operations, client pipeline, partners, team
- **Personal** — doctrine, relationships, body, inner work
- **Drone Enterprises** — defense hardware co-founding venture with Sam Schutt; infantry-scale attritable UAS; Conley is CSO
- **Long Game Studios** — parent studio brand; products: DailyChew.AI (AI-personalized daily news podcast) and The Grind (browser game). Dev progress captured as `work-log` pages under this domain.

**Expansion order** (as new sources arrive):

1. Personal — journaling, goals, psychology, self-improvement
2. Research — deep topic dives, reading notes
3. General knowledge — articles, podcasts, web clips

When a new domain becomes active, create a `domain` page for it and add a new section to `index.md`. Update this section of CLAUDE.md to reflect the new scope.

---

## Known pages needing attention

Track pages with open issues here so they aren't forgotten between sessions:

- `[[ba-clients-pipeline]]` — seeded from two sources only; full client base not yet represented
- `[[conley-potter]]` — wedding date June 12, 2026; update "engaged to Sami" to "married" post-June 12
- `[[portfolio-website]]` — wiki's "What the Site Currently Says" section is pre-update (April 14 state); ingest a new site snapshot to sync the copy
- `[[portfolio-update-plan]]` — was scoped around the old ACE/freelance persona; review whether the pending queries (5–8) still apply after the PBE pivot

Clear items from this list when resolved; add new ones as they're discovered.

---

## Evolution

This schema is a living document. When a convention proves awkward, a workflow step is missing, or the wiki outgrows its current structure, update this file to reflect how we actually work. The schema is only useful if it matches reality.
