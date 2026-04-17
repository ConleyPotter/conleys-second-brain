---
type: asset
domain: personal
tags: [second-brain, claude-code, obsidian, writing, portfolio, meta]
created: 2026-04-16
updated: 2026-04-16
sources: []
---

# Building a Second Brain with Claude Code

**Related:** [[building-out-loud]], [[portfolio-website]], [[wiki-structure-planning]], [[brand-voice]]

---

*A persistent memory system built on markdown, Obsidian, and a CLI I didn't expect to trust.*

---

I have a problem that I suspect most people building with AI share: the model forgets everything.

Every session starts cold. You brief it, it helps you, and when the window closes, the context evaporates. For one-off tasks, that's fine. For a complex, ongoing project — a business you're building, a career you're managing, a life you're trying to understand — it's a structural limitation. The knowledge lives in your head, or scattered across documents, or buried in chat histories you can't search.

I started thinking about this differently after encountering Andrej Karpathy's approach to `CLAUDE.md`. The idea is simple: use a well-structured instruction file as an operating contract between you and the model. Load it at session start, and the model knows who it's talking to, what it's maintaining, and how to behave. It's not memory — it's a schema. A way of making the model's behavior consistent across sessions, even when the model itself has no persistent state.

That was the seed. Ray C Fu gave me the initial frame for pairing Obsidian with Claude Code and the starter prompts that shaped the first session. What I built from both of those ideas is something I've been calling the second brain method.

---

## What it is

The second brain is a persistent, compounding wiki — a flat collection of markdown files that Claude Code reads, writes, and maintains as a knowledge system. It works in three layers.

**Raw sources** — immutable documents: business plans, brand guides, weekly recaps, project briefs. These go in a folder the model never modifies. They are the source of truth.

**Wiki pages** — LLM-generated markdown summaries, cross-referenced and kept current. When a new source comes in, Claude reads it, synthesizes key information into pages, flags contradictions with what already exists, and links everything together using Obsidian's wiki-link format. A single source might touch ten pages.

**The schema** — `CLAUDE.md`, a detailed operating contract. It defines what types of pages exist, how to format the index, how to write the log, what the current scope is, and what to prioritize. It's read at the start of every session, which means every session starts oriented instead of cold. The schema is also what makes the system feel like a system — the same conventions, every time, regardless of which session is running.

---

## How I set it up

The first session was April 14, 2026 — the same day I launched the Phase I campaign for ACE, the freelance automation business I've been building. I dropped five source documents in the raw-sources folder and ran the ingest workflow. Claude built twelve wiki pages, an index, and a log in a single session. That was the init.

Two days later: thirty-seven pages, fourteen source documents, three distinct domains. ACE (the business I'm building). BA (my day job at Business Actualization, a digital marketing agency serving auto repair shops). Personal (operating doctrine, long-range projects, life context that doesn't fit neatly anywhere else).

The coverage surprised me. I went in thinking this would be a tool for the business. It became a tool for everything. The wiki now holds the kind of context that used to live in my head — the stuff that takes fifteen minutes to reconstruct each time someone asks a question that touches more than one domain at once.

---

## What makes it work

A few things surprised me about how well this actually functions.

**The log is a signal.** Every operation is appended to `log.md` — what was read, what was created, what changed, and why. At the start of each session, Claude reads the last several entries to understand recent context. The log is greppable, structured, and honest. It's not just bookkeeping. It's the continuity that makes sessions feel connected across days and weeks.

**The index earns its keep.** A flat list of pages sounds simple. In practice, it's the thing that lets you orient quickly. You know what's in the wiki without reading everything. You know where to look. That's surprisingly hard to replicate any other way when the knowledge base grows.

**Ingestion is where the value compounds.** When a new source comes in, Claude doesn't just summarize it — it reads existing pages and actively looks for contradictions. If the new source changes what a previous page said, the old page gets updated and the change gets noted. The wiki stays internally consistent across updates. That's the thing that's hard to maintain manually and that the model handles without friction.

**The discipline is the system.** Flat pages, consistent frontmatter, rolling versus archival page types, a schema that the model follows precisely — none of it is technically sophisticated. It's structure. But structure is what turns a folder of markdown into something you can actually use six months from now.

---

## The team angle

I've been running this as a personal tool, but the pattern doesn't require it to be.

The same mechanics — raw sources, wiki pages, schema file, index, log — work for a small team. Swap the personal `CLAUDE.md` for a team schema that defines company-level conventions. Replace Obsidian with any markdown viewer or GitHub's built-in rendering. Use Git for version control and GitHub for access management. The AI becomes a shared knowledge maintainer rather than a personal one. Multiple contributors add source documents; the model synthesizes, cross-links, and keeps the wiki current.

What changes is the governance layer. The schema needs to define domains more carefully, handle the fact that different people have different mental models of the same information, and account for permissions. But the core mechanics translate directly. Read, synthesize, flag contradictions, update index, append log. That loop doesn't care whether one person is feeding it or ten.

I'm calling it the second brain method even when it scales to a team because the underlying logic is the same: persistent, compounding knowledge, maintained by a model that knows the schema.

---

## Where it goes

It's been two days. I don't have a verdict on whether this compounds the way I think it will.

What I have is this: I already know where to look for things. The index is genuinely useful. The log tells me what I was thinking two days ago in a way that chat history doesn't. When I open a new Claude Code session on this repository, the model reads three files and is immediately oriented. That handoff works.

The questions that remain: does the wiki stay useful at two hundred pages? Does the schema hold when the domains get messier? Does the ingestion discipline survive weeks where there's no time to be methodical?

I don't know yet. But I'm building this. You're welcome to watch.

---

*Built on Andrej Karpathy's `CLAUDE.md` pattern. Initial Obsidian + Claude Code setup and starter prompts from Ray C Fu.*
