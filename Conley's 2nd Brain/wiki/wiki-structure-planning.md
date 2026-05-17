---
type: synthesis
domain: general
tags: [meta, planning, structure, wiki]
created: 2026-04-16
updated: 2026-04-16
sources: []
---

# Wiki Structure Planning — Expanding Beyond ACE

**Related:** [[index]], [[domain-personal]], [[operating-doctrine-2026]], [[conley-potter]]

This page is a standing recommendation for how to evolve this wiki's structure as it expands from an ACE-centric knowledge base into a full second brain covering all of Conley's life domains. It was written in response to the two new recurring source types introduced in `raw-sources/`: the weekly work summary and the daily work recap.

---

## 1. Flat vs. Segmented — Recommendation: Stay Flat, But Segment the Index

**Keep the flat `wiki/` directory** for now. No subfolders.

The wiki is at 28 pages. Subfolders create navigation debt before the volume justifies it — you'd need to update cross-links, ingest workflows, and mental models all at once. The current flat structure works well in Obsidian: graph view, quick-switcher, and wiki-links don't care about directories.

**The right move is not a directory split — it's domain-tagging and index discipline.**

The `index.md` section structure is already doing the real organizational work. What breaks down as the wiki grows isn't findability (Obsidian handles that) — it's the index becoming unwieldy. Solve that by:

- Adding a `domain:` frontmatter field to every page (e.g., `domain: ace`, `domain: ba`, `domain: personal`, `domain: research`)
- Using this to quickly filter pages by domain without needing folder paths
- Keeping `index.md` sections clean by treating each domain as its own table block

**Revisit the subfolder question at ~80 pages.** At that scale, a structure like `wiki/ace/`, `wiki/ba/`, `wiki/personal/` starts making sense. Until then, the complexity isn't worth it.

---

## 2. New Wikis to Create — Day Job Domain (BA)

The weekly summary (`conley-weekly-summary-apr-6-12-2026.md`) and daily recap (`Daily-Recap_2026-04-15.md`) introduce an entire operational domain that currently has no proper home in the wiki. The existing pages (`career-history.md`, `conley-potter.md`) treat BA as background context. These sources reveal BA is a full operational environment worth documenting.

**New standing pages to create (6):**

### `ba-overview.md` — type: `operations`
The foundation page for the BA domain. What Business Actualization does, Conley's role (sales/client success hybrid), the team structure, and how the job connects to the 2026 Operating Doctrine (BA = income floor, ACE = owned asset). This is the "what is this domain" anchor, the same role `ace-overview.md` plays for ACE.

### `ba-products.md` — type: `operations`
The full BA service/product catalog: Standard Website, Jumpstart, Jumpstart+, Advanced LSA, Google Ads, Social Content Curation, Landing Pages, Review Management. Document each tier's scope, approximate pricing, and where it fits in the sales motion. This knowledge is embedded across dozens of client interactions and never made explicit in the wiki. It's also directly relevant to ACE (Conley's day-job product knowledge informs what he can pitch credibly as a freelancer).

### `ba-partners.md` — type: `operations`
AutoVitals and Turnkey Auto Marketing are not just vendor relationships — they're referral channels and co-selling partners that drive meaningful pipeline. Jared Baker's multi-shop lead (Apr 15) is a prime example. This page documents the commercial structure, key contacts (Steve at AV, Jared/Suzanne at Turnkey), and how these partnerships work operationally (joint calls, co-managed accounts, inbound referral flow).

### `ba-team.md` — type: `identity`
The internal team: Jon Fonner (sales/management), Adam (ownership, broader shop incubator vision), Ethan Wauls (websites/delivery), Micah (operations/HR), Courtney Nguyen (scheduling/intake), Kyle Sarnowski, Josh (Gauge maintenance), Abby. This page documents roles, working relationships, and the team dynamics relevant to understanding Conley's position. It's also useful for any query that touches internal communications.

### `ba-clients-pipeline.md` — type: `operations`
A rolling (not archival) reference to the active client pipeline. **Not a deal log** — HubSpot is the system of record for deals. This page documents the *recurring client relationships* and key accounts that appear repeatedly across sources: Heights Expert, Bernhard Auto Works, Aspen Auto Clinic, Turbo Tim's, Tilson's, CarLink360, etc. Includes deal context (stage, approximate value, key contacts) when relevant. Updated in place as clients move through the pipeline.

### `adam-shop-incubator.md` — type: `project`
Adam's 6-location auto repair shop chain is a distinct strategic initiative that surfaced in the weekly summary — not a client account, not an ACE project, but a meaningful context element. Adam bought shop #1 as an incubator for BA's marketing work and a real estate hold. GC referral (Jim Walton, Conley's mom's boyfriend) has now walked the site. This project will generate recurring mentions in BA recaps and deserves its own page rather than being buried in log entries.

---

## 3. Recurring Source Types — Naming Convention

The weekly summaries and daily recaps are going to be regular inputs. They need a consistent naming and page-type convention.

**Proposed conventions:**

| Source type | File naming | Wiki page naming | Page type |
|---|---|---|---|
| Daily work recap | `Daily-Recap_YYYY-MM-DD.md` | `daily-recap-YYYY-MM-DD.md` | `work-log` |
| Weekly work summary | `[descriptive]-summary-[date-range].md` | `weekly-recap-YYYY-MM-DD.md` (week start date) | `work-log` |

Use `weekly-recap-2026-04-06.md` for the Apr 6–12 weekly summary (keyed to the Monday start date).

**Important distinction:** Dated recap pages are **archival** — created once, never modified. Standing BA pages (`ba-overview.md`, `ba-clients-pipeline.md`, etc.) are **rolling** — updated in place as new information arrives. Recaps feed the standing pages; they don't replace them.

---

## 4. Full Domain Map — Where the Wiki Is Headed

Based on current sources and the Operating Doctrine expansion path, the wiki will eventually need these domains:

| Domain | Status | Anchor page | What it covers |
|---|---|---|---|
| ACE | Active | `ace-overview.md` | Strategy, ops, tech, marketing for the freelance engine |
| BA (Day Job) | **Needs foundation** | `ba-overview.md` (to create) | Professional role, clients, partners, products, team |
| Personal | Seeded | `domain-personal.md` | Doctrine, relationships, body, inner work |
| Projects | Active (mixed ACE/personal) | (index section) | Sentinel, River Room, Building Out Loud, Muse, Companion, Book |
| Research | Not yet started | — | Deep topic dives, reading notes |
| General Knowledge | Not yet started | — | Articles, podcasts, web clips |

The biggest immediate gap is BA. It's generating the most raw source volume (daily + weekly cadence) but has the least wiki infrastructure. Fix that first.

---

## 5. Recommended Changes to CLAUDE.md

These are targeted additions and edits — not a restructure. The CLAUDE.md schema is working well. These changes make it accurate for the domains that are now active.

### 5a. Add `work-log` to the page type table

```
| `work-log` | Dated snapshot of professional activity | `daily-recap-2026-04-15.md`, `weekly-recap-2026-04-06.md` |
```

Work-log pages are archival by definition — they document what happened on a given day or week and are never updated after creation (unlike `operations` pages, which are living references). This distinction matters for the ingest workflow: when a new daily/weekly recap arrives, don't update the dated page — update the relevant standing pages instead, then create the dated page as a record.

### 5b. Update "Active domain" in Current Scope

Change:
```
**Active domain:** ACE — strategy, operations, marketing, identity, projects.
```

To:
```
**Active domains:**
- **ACE** — strategy, operations, marketing, identity, projects
- **BA (Day Job)** — professional operations, client pipeline, partners, team
- **Personal** — doctrine, relationships, body, inner work
```

### 5c. Add `domain:` to the frontmatter template

```yaml
---
type: strategy
domain: ace
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
---
```

This is a low-effort addition that pays off when the wiki reaches 60+ pages and you want to quickly filter or audit by domain.

### 5d. Add a "Rolling vs. Archival" distinction to the Page Types section

Add a note after the type table:

> **Rolling pages** are updated in place as new information arrives (most pages). **Archival pages** are created once and never modified (`work-log` type, dated recaps). When a new recap source is ingested, update rolling pages with new information, then create the dated archival page as a record.

### 5e. Add an ingest pattern for recurring log sources

Add to Section 2 (Ingest a source), after the existing steps:

> **For recurring log sources (daily/weekly recaps):**
> 1. Read the recap fully.
> 2. Update all relevant standing pages (e.g., `ba-clients-pipeline.md`, `ba-overview.md`) with any new information — new clients, personnel changes, product developments, notable events.
> 3. Create the dated archival page (`daily-recap-YYYY-MM-DD.md` or `weekly-recap-YYYY-MM-DD.md`) as a structured summary.
> 4. Do not file every granular detail — extract what changes standing pages or signals meaningful patterns. Noise stays in the raw source.

### 5f. Update index.md section list

Change the index section list from:
```
- Core Strategy
- Operations & Tech
- Marketing & Brand
- Identity & Public Presence
- Projects
- Source Files
```

To:
```
- Core Strategy
- ACE Operations & Tech
- Marketing & Brand
- Identity & Public Presence
- Day Job (BA)
- Projects
- Personal
- Day Job Logs
- Source Files
```

### 5g. Update "Known pages needing attention"

Add after existing items:
```
- `[[ba-overview]]` — needs creation; BA domain has no foundation page despite being the primary income source
- `[[ba-products]]` — needs creation; product catalog knowledge is embedded in recaps but never consolidated
- `[[ba-partners]]` — needs creation; AutoVitals and Turnkey relationships generate recurring mentions with no home
- `[[weekly-recap-2026-04-06]]` — weekly summary source ingested but no dated wiki page created yet
```

---

## Summary — Priority Order

If you were to act on all of this in one session, here's the sequence that makes the most sense:

1. **Create `ba-overview.md`** — unlocks the domain and gives all subsequent BA pages a home to link back to
2. **Create `ba-products.md`** — highest informational value; product knowledge appears constantly
3. **Create `ba-partners.md`** — AutoVitals and Turnkey are referenced in almost every recap
4. **Create `weekly-recap-2026-04-06.md`** — complete the Apr 6–12 source ingest that's currently half-done
5. **Create `ba-team.md`** — lower urgency but useful once recaps accumulate
6. **Create `ba-clients-pipeline.md`** — becomes most useful after 3–4 weekly recaps have been ingested
7. **Create `adam-shop-incubator.md`** — when a second source mentions it
8. **Update CLAUDE.md** — do this in a dedicated session so the schema changes don't get buried in a content session
9. **Add `domain:` frontmatter** — lowest urgency; backfill during a lint pass
