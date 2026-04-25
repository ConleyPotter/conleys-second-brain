---
type: synthesis
domain: general
tags: [jarvis, content-production, claude, obsidian, vault-meta]
created: 2026-04-24
updated: 2026-04-24
sources: []
---

# JARVIS System

JARVIS (name from the @cyrilXBT guide) is the content production layer of Conley's second brain vault. It sits alongside the knowledge base (`wiki/` + `raw-sources/`) and handles the daily observation → connection → brief → published pipeline.

**Status:** Built and integrated (2026-04-24)

---

## What It Is

A structured workflow system inside the same Obsidian vault as the wiki. The core function: turn what Conley notices, builds, and thinks into published content that sounds exactly like him.

**The pipeline:**

```
Daily observation → 00-INBOX
      ↓ (process-inbox)
01-CAPTURES/{observations,reactions,patterns,questions,numbers}
      ↓ (weekly-connections)
02-CONNECTIONS (synthesized cross-capture insights)
      ↓ (generate-brief)
03-BRIEFS (structured content brief)
      ↓ (write-content)
04-PUBLISHED (archived + engagement data)
```

---

## Folder Structure

| Folder | Purpose |
|---|---|
| `00-INBOX/` | Unprocessed captures — zero organization at capture time |
| `01-CAPTURES/observations/` | Things noticed, raw and unpolished |
| `01-CAPTURES/reactions/` | Honest gut response to something read or heard |
| `01-CAPTURES/patterns/` | Same principle appearing in two different domains |
| `01-CAPTURES/questions/` | Things genuinely not known |
| `01-CAPTURES/numbers/` | Real data points with specific numbers attached |
| `02-CONNECTIONS/` | Synthesized cross-capture insights — content comes from here |
| `03-BRIEFS/` | Content ready to write — hook written, closer written, sources linked |
| `04-PUBLISHED/` | Archived posts with engagement data; never modify without explicit instruction |
| `05-CLAUDE/` | Claude working directory — operating contract + skill files |

---

## Slash Commands

| Command | What it does |
|---|---|
| `/jarvis-process-inbox` | Processes every note in `00-INBOX` — sharpens, tags, moves to correct subfolder |
| `/jarvis-connections` | Finds 3–5 non-obvious connections across last 7 days of captures |
| `/jarvis-brief` | Generates a structured content brief from a connection or topic |
| `/jarvis-write` | Writes the full post from a brief in Conley's exact voice |

---

## Operating Contract

`05-CLAUDE/CLAUDE.md` is the primary operating contract for all JARVIS work. It contains:

- Conley's full identity context (BA, ACE, Sentinel, River Room, personal)
- Complete audience definition
- Detailed voice rules (word choice, rhythm, what failure looks like)
- Hard rules (banned phrases, identity separation between BA/ACE/LinkedIn)
- Skill definitions cross-referenced to individual skill files in `05-CLAUDE/skills/`

---

## Connection Types

The weekly connection session looks for four types:

| Type | Description |
|---|---|
| A | Same underlying principle in two different domains |
| B | Contradiction between two notes that creates interesting tension |
| C | Pattern connecting three or more notes into one unnamed insight |
| D | A question from one note that another note accidentally answers |

The quality bar: a connection must be non-obvious. If it would surprise the person who wrote the notes, it qualifies.

---

## Integration with the Wiki

JARVIS and the knowledge base share the same vault. Captures and briefs can link to wiki pages using `[[wiki-link]]` syntax — these resolve natively in Obsidian.

**Cross-system rules:**
- Significant captures (new ACE signals, BA intelligence, personal context) surface as wiki ingest candidates
- `04-PUBLISHED/` engagement data that reveals strong audience signals can update `[[brand-voice]]` — ask Conley first
- `05-CLAUDE/CLAUDE.md` is truth on voice rules; `[[brand-voice]]` in the wiki is the same content in wiki page format

---

## Why JARVIS Instead of Traditional Content Workflow

The second brain separates knowledge accumulation (wiki) from content production (JARVIS). The wiki compounds forever — it gets smarter as more sources arrive. JARVIS produces — it turns daily raw material into published output.

The distinction matters because knowledge accumulation and content production have different rhythms. The wiki is slow, patient, permanent. JARVIS is fast, daily, perishable-input → permanent-output.

Building both in one vault gives Conley native cross-linking without syncing across systems. A brief can reference `[[ace-overview]]` and the link resolves.

> **See also:** [[llm-wiki-pattern]], [[brand-voice]], [[building-out-loud]]
