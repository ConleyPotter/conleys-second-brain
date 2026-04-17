---
name: second-brain-ingest
description: >
  Use this skill whenever Conley asks to ingest, process, or add a daily recap,
  weekly recap, work log, or work summary into the second brain wiki. Triggers
  include phrases like "ingest recap," "new daily recap," "process this week's
  summary," "add to the wiki," or any mention of a file in raw-sources/ that
  is a work log. Also use this skill if Conley says something like "I just added
  a recap" or points to a Daily-Recap or weekly-summary file. This skill handles
  the full ingest workflow: pre-flight orientation, rolling page updates, archival
  page creation, index update, and structured log append.
---

# Second Brain — Recap Ingest Skill

Handles ingestion of daily and weekly BA work recaps into Conley's second brain wiki. Follow every step in order. Do not skip steps or reorder them.

---

## Step 0 — Detect Recap Type

Before anything else, identify whether this is a **daily** or **weekly** recap by looking at the filename or Conley's description:

- `Daily-Recap_YYYY-MM-DD.md` → **daily**
- `weekly-summary-*` or `weekly-recap-*` → **weekly**

This determines the archival page name and which rolling pages to prioritize.

---

## Step 1 — Pre-Flight Orientation

Read these three files in order before touching anything:

1. `CLAUDE.md` — re-read the full operating contract
2. `Conley's\ 2nd\ Brain/wiki/log.md` — read the last 5–10 entries to understand recent activity and what's already been ingested
3. `Conley's\ 2nd\ Brain/wiki/index.md` — orient to current wiki shape; note page count and source count

Do not create or modify any file until Step 1 is complete.

---

## Step 2 — Read the Source

Read the raw source file in full from `raw-sources/`. Never modify files in `raw-sources/`.

As you read, build a mental map of:
- **New clients or prospects** mentioned → candidates for `ba-clients-pipeline.md`
- **Team members acting in new or notable ways** → candidates for `ba-team.md`
- **Partner interactions** (AutoVitals, Turnkey, etc.) → candidates for `ba-partners.md`
- **Product/service tiers mentioned** → candidates for `ba-products.md`
- **Operational or structural changes** → candidates for `ba-overview.md`
- **Notable one-off events** (legal catch, policy change, major deal) → flag for "What This Reveals" section and potentially a new page

---

## Step 3 — Identify Rolling Pages to Update

Read `Conley's\ 2nd\ Brain/wiki/index.md` and identify which **rolling** pages (non-work-log type) are touched by this recap. For daily recaps, always check these first:

| Page | Update if... |
|---|---|
| `ba-clients-pipeline.md` | Any new client, prospect, or status change on existing accounts |
| `ba-overview.md` | Structural changes to how BA operates, new service tiers, team changes |
| `ba-team.md` | Personnel mentioned in new roles, notable actions, or status changes |
| `ba-partners.md` | Any interaction with AutoVitals, Turnkey, or other referral partners |
| `ba-products.md` | Any service tiers, pricing, or product specifics mentioned |

For weekly recaps, also check `financial-projections.md` and `ace-overview.md` if the week touches ACE.

Read each candidate page before editing it. Update only what has genuinely changed — do not pad pages with noise from the source. Noise stays in the raw source.

After updating, set the `updated` frontmatter date on each modified page.

---

## Step 4 — Create the Archival Page

Create the dated archival wiki page. This page is **never modified after creation**.

**Filename convention:**
- Daily: `Conley's\ 2nd\ Brain/wiki/daily-recap-YYYY-MM-DD.md`
- Weekly: `Conley's\ 2nd\ Brain/wiki/weekly-recap-YYYY-MM-DD.md`

**Frontmatter:**
```yaml
---
type: work-log
domain: ba
tags: [ba, day-job, client-ops, daily-recap]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [Original-Filename.md]
---
```

**Page structure** (follow this order):

```markdown
# Daily Recap — [Month DD, YYYY]

**Related:** [[conley-potter]], [[ba-overview]], [[ba-clients-pipeline]]

*Source: [list sources from the recap header]*

---

## What This Is

[1–2 sentence description of the day/week — volume, type of work, notable context.]

---

## Key Themes

### 1. [Theme Name]
[Organized by theme, not by source. Each client, partner thread, or internal topic gets its own sub-section. Use the raw source's detail level as a floor, not a ceiling — synthesize where possible.]

---

## Open Items Carrying Forward

[Table of open items with Owner and Status columns. Only include genuinely unresolved items.]

| # | Item | Owner | Status |
|---|---|---|---|

---

## What This Reveals

[3–6 analytical observations connecting this day/week to broader patterns in the wiki. Cross-link to relevant pages using [[page-name]]. Flag contradictions, signals, or open questions. This section is the highest-value part of the page — don't skip it or make it shallow.]
```

**Writing standard:** Write for future Conley, not for the LLM. Be concise. Use bullets for facts, prose for analysis. Match the brand voice: direct, technical-but-human, no corporate filler.

---

## Step 5 — Update index.md

Open `Conley's\ 2nd\ Brain/wiki/index.md` and make exactly these changes:

1. Increment **Source count** by 1
2. Increment **Page count** by 1 (for the archival page; add 1 more for each new rolling page created, if any)
3. Update **Last updated** to today's date
4. Add a row to the **Day Job Logs** section table:
   ```
   | [[daily-recap-YYYY-MM-DD]] | BA workday recap [Month DD]: [2–5 word summary of key themes] |
   ```
5. Add a row to the **Source Files** table:
   ```
   | `Daily-Recap_YYYY-MM-DD.md` | BA workday log — [one-line description] | YYYY-MM-DD |
   ```

Do not reorganize sections or change anything else in index.md.

---

## Step 6 — Append to log.md

Append a new entry to the **bottom** of `Conley's\ 2nd\ Brain/wiki/log.md`. Use this exact structure — do not abbreviate:

```markdown
## [YYYY-MM-DD] ingest | Daily Recap — [Month DD, YYYY]

**Source type:** [Brief description of what the document is]
**Pages created:** N (`page-name.md`, ...)
**Pages updated:** N (`page-name.md`, ...)

### What this source contains

[2–4 sentences on what the day/week covered. Call out specific data points, superseding information, and anything that contradicts or updates existing pages.]

### What changed

- `page-name.md` — [What was added or rewritten, and why]
- [One bullet per touched page]

### Notable observations

[2–5 observations connecting this source to the broader wiki. Flag contradictions, patterns, open questions, and cross-domain connections.]
```

---

## Step 7 — Report to Conley

After all files are written, report:

1. **Pages created:** list with filenames
2. **Pages updated:** list with filenames and a one-line summary of what changed in each
3. **Open items flagged:** count and any that look like they need Conley's attention beyond normal follow-up
4. **Anything surprising or worth flagging:** contradictions with existing pages, high-signal patterns, items that suggest a new wiki page should exist

Keep the report tight. Conley can read the files — you don't need to repeat their full content.

---

## Edge Cases

**Duplicate ingest:** Before creating the archival page, check log.md to confirm this date hasn't already been ingested. If it has, tell Conley before proceeding.

**New entity with no existing page:** If a client, partner, or concept appears that has no wiki page and is mentioned substantively enough to warrant one, create a stub page with correct frontmatter and a note that it needs expansion. Add it to index.md and log it.

**Conflicting information:** If the recap contradicts something in an existing rolling page, update the rolling page, note the contradiction explicitly in the log entry under "Notable observations," and flag it in your report to Conley.

**Missing rolling page:** If a rolling page that should be updated (e.g., `ba-clients-pipeline.md`) doesn't exist yet, create it with appropriate frontmatter before updating it. Log the creation.
