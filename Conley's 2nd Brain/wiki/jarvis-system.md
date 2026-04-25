---
type: synthesis
domain: general
tags: [second-brain, claude-code, obsidian, content-production, jarvis, system-design]
created: 2026-04-24
updated: 2026-04-24
sources:
  - How to Build a JARVIS Inside Obsidian With Claude Code — The Full Setup From Scratch.md
  - New JARVIS Repo CLAUDE.md File.md
---

# JARVIS System

**Related:** [[second-brain-article]], [[llm-wiki-pattern]], [[brand-voice]], [[building-out-loud]], [[second-brain-mcp-server]], [[gstack]]

---

## What It Is

JARVIS (from the @cyrilXBT April 2026 guide) is a content production system built inside Obsidian, powered by Claude Code. It is distinct from the existing 2nd Brain wiki system.

The existing 2nd brain is a **knowledge base**: it ingests raw sources, produces wiki pages, and maintains an index of accumulated knowledge across ACE, BA, and personal domains.

JARVIS is a **content production engine**: it captures raw observations and reactions, finds non-obvious connections between them, generates content briefs from those connections, and produces finished posts in the operator's exact voice. Its output is published content, not reference pages.

These two systems are complementary. The second brain holds what Conley knows and has built. JARVIS turns that material into content.

---

## Vault Structure

```
JARVIS/
├── 00-INBOX/                  — unprocessed captures, zero organization
├── 01-CAPTURES/
│   ├── observations/          — things noticed, raw and unpolished
│   ├── reactions/             — honest gut response to something read/heard
│   ├── patterns/              — same principle appearing in two different domains
│   ├── questions/             — things genuinely unknown
│   └── numbers/               — real data points with specific numbers attached
├── 02-CONNECTIONS/            — synthesized insights from 2+ captured notes
├── 03-BRIEFS/                 — content ready to write (hook + closer already done)
├── 04-PUBLISHED/              — archived content with impression + bookmark data
└── 05-CLAUDE/
    ├── CLAUDE.md              — identity, voice, vault structure, hard rules, jobs
    ├── skills/                — reusable workflow files
    └── context/               — background files Claude should read
```

**Key architectural decision:** CAPTURES is organized by note type, not topic. A note about AI content strategy and a note about how attention works psychologically both land in `patterns/` — not in separate topic folders — so Claude can find the connection between them automatically.

---

## The Four Core Skills

Skills are reusable workflows stored as markdown files in `05-CLAUDE/skills/`. Call them by name; Claude executes the full process.

**Skill 1 — Process Inbox:**
Read every note in `00-INBOX/`. For each: determine the correct CAPTURES subfolder, sharpen the raw note into one specific punchy sentence, add exactly three tags, move it. Report what was processed, patterns noticed, and one connection worth exploring.

**Skill 2 — Weekly Connections:**
Read all notes added to `01-CAPTURES/` in the last 7 days. Surface connections across all subfolders simultaneously. Strong connections are one of four types: same underlying principle in two unrelated domains; contradiction creating interesting tension; pattern connecting 3+ notes into one unnamed insight; a question from one note that another accidentally answers. Obvious connections don't qualify. Minimum 3, maximum 5.

**Skill 3 — Generate Brief:**
Turn a strong connection into a structured content brief with five fields: ONE THING (single insight, one sentence), PROOF (specific real number or example), READER TRANSFORMATION (what they know/feel at the end they didn't before), THREE HOOKS (aggressive / curious / personal, ranked), THREE CLOSERS (ranked by urgency). Save in `03-BRIEFS/`.

**Skill 4 — Write Content:**
Read the brief. Read all source notes it links. Write in the operator's exact voice. Structure: hook → proof → body → closer. No filler. Save draft next to the source brief.

---

## The Daily JARVIS Ritual (20 minutes)

- **Minutes 1–5:** Dump raw captures into `00-INBOX/`. Voice memo transcriptions, things noticed, reactions to what was read last night. Raw. Unpolished.
- **Minutes 6–10:** Run "Process Inbox." Read the report. Note what patterns Claude found.
- **Minutes 11–15:** "Are there strong connections between today's captures and anything in my vault from the last 14 days?" This is where JARVIS earns its name.
- **Minutes 16–20:** "Generate a brief for the connection about [whatever surprised you most]."

Result: a content brief ready before opening any social media. The rest of the day is execution, not ideation.

---

## Performance Loop

After content is published, open the note in `04-PUBLISHED/` and add engagement data: impressions, bookmarks, top comment, what worked. Once a month, ask: which topics drove the most bookmarks per impression, which hook formats outperformed their topic average, what three angles haven't been tried yet.

This is the compounding mechanism. The system learns what works from actual data, not instinct.

---

## Relationship to the Existing Second Brain

The existing second brain wiki and JARVIS serve different functions:

| | 2nd Brain Wiki | JARVIS |
|---|---|---|
| Purpose | Knowledge accumulation | Content production |
| Input | Source documents, recaps, research | Raw daily observations |
| Output | Reference pages, analysis | Published posts and briefs |
| Schema file | `CLAUDE.md` (this vault's root) | `05-CLAUDE/CLAUDE.md` |
| Temporal rhythm | Ingest on new sources | Daily capture + weekly connection |

The second brain is the context that makes JARVIS smarter. JARVIS is the output layer that turns that context into signal.

Long-term integration path: the second brain exposed as an MCP server (see [[second-brain-mcp-server]]) could feed into JARVIS's connection sessions, making the 14-day lookback window draw from the full accumulated wiki rather than only recent JARVIS captures.

---

## Status

As of April 2026: planned but not yet built. The JARVIS CLAUDE.md has been written (saved at vault root as `JARVIS-CLAUDE.md`). Next step is creating the new Obsidian vault with the folder structure above, installing the required plugins (Templater, Dataview, QuickAdd, Obsidian Git), and writing the four skill files.

> **Note:** The JARVIS CLAUDE.md saved in this vault is a Conley-specific, fully filled-in version of the @cyrilXBT template. It includes deep identity context, exact voice rules, all hard rules, and the Primary Jobs definition. It is not a generic template.
