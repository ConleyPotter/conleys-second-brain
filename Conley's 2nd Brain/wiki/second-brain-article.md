---
type: asset
domain: personal
tags: [second-brain, claude-code, obsidian, writing, portfolio, meta]
created: 2026-04-16
updated: 2026-04-17
sources: []
---

# Building a Second Brain with Claude Code

**Related:** [[building-out-loud]], [[portfolio-website]], [[wiki-structure-planning]], [[brand-voice]], [[llm-wiki-pattern]]

---

*A persistent memory system built on markdown, Obsidian, and a CLI I didn't expect to trust.*

---

Modern AI tools from Frontier Labs feature built-in memory, allowing them to retain information rather than simply forget. However, this retention often occurs in ways users can't fully control. I'm sure other nights-and-weekends founders have struggled with decisions about how to segment their workspaces and how much context from other workspaces to share with siloed assistants to make them smart enough without poisoning their memory with irrelevant or conflicting context.

The deliberate effort required to segment your life into siloed workspaces takes a toll through decision fatigue and unnecessary mental overhead. For a complex, ongoing project (a business you're building, a career you're managing, or a life you're trying to understand), segmentation and separation are structural limitations. The knowledge lives in your head or scattered across workspaces.

I started thinking about this differently after encountering Andrej Karpathy's approach to `CLAUDE.md`. The idea is simple: use a well-structured instruction file as an operating contract between you and the model. Load it at session start, and the model knows who it's talking to, what it's maintaining, and how to behave. The instructions give the model an understanding of an ever-evolving schema. The schema helps make the model's behavior consistent across sessions, even when the model itself has no persistent state. 

That was the seed. One of [Rui Fu's](https://www.raycfu.com/) (@raycfu) videos gave me the initial frame for pairing [Obsidian](https://obsidian.md) with [Claude Code](https://claude.ai/code) and the starter prompts that shaped the first session. The result is a personal implementation of what [Tiago Forte](https://www.buildingasecondbrain.com/) calls the second brain, though this one is a persistent, compounding knowledge system, maintained by an AI. This system is designed for someone like me, juggling multiple roles across a demanding day job and multiple startups, each with different levels of formality, secrecy, and commitment. I require granular control over what my AI assistants and agents know, prioritize, and share; tailoring their behavior to specific contexts, audiences, and tones.

---

## What it is

The system works in layers.

The first is raw sources: immutable documents dropped into a folder that the model never modifies. Business plans, brand guides, weekly recaps, project briefs. The sources of truth.

The second is the wiki, a flat collection of Markdown files that Claude Code reads, writes, and keeps up to date. When a new source comes in, Claude synthesizes key information into pages, flags any contradictions with existing content, and links everything together using Obsidian's wiki-link format. A single source might touch ten pages, each updated and cross-referenced.

The third is `CLAUDE.md`, the operating contract. It defines the types of pages, how to format the index, how to write the log, and the current scope. Every session begins with Claude reading this file, which means every session begins oriented. The same conventions, every time, regardless of how long since the last one. You can use an `AGENTS.md` file to use Codex or any other coding agent, as well.

---

## How I set it up

The first session was April 14, 2026, the same day I launched the Phase I campaign for ACE, the freelance automation business I've been building. I dropped five source documents in the raw-sources folder and ran the ingest workflow. Claude built twelve wiki pages, an index, and a log in a single session.

Two days later: 37 pages, 14 source documents ingested, coverage across 4 distinct domains. ACE (the business). BA (my day job at AutoBoost | Business Actualization, a digital marketing agency serving auto repair shops). Personal (operating doctrine, long-range projects, the life context that doesn't fit neatly anywhere else). And meta: pages about the system itself.

The coverage surprised me. I went in thinking this would be a tool for the business. It became a tool for everything. The wiki now holds the kind of context that used to live in my head, the stuff that takes fifteen minutes to reconstruct each time someone asks a question touching more than one domain at once.

---

## What makes it work

Every operation gets appended to `log.md`: what was read, what was created, what changed, and why. At the start of each session, Claude reads the last several entries. That log is greppable, structured, honest, and it's what gives sessions their continuity. Without it, each session would start cold, even with a schema in place.

The index is the thing I didn't expect to matter as much as it does. A flat list of pages with one-line summaries sounds trivial until the wiki is large enough that you'd otherwise have to search or guess. I know what's in here without having to read everything.

Ingestion is where the value actually compounds. When a new source comes in, Claude summarizes it, reads existing pages, and looks for contradictions. If the new source changes what a previous page said, the old page gets updated, and the change gets noted. The wiki stays internally consistent across updates without me having to manage it manually.

And then there's the discipline, which is probably the most important part, even though it's the least interesting to describe. Flat pages, consistent frontmatter, rolling versus archival page types, and a schema that the model follows precisely. None of it is technically sophisticated. Structure is what makes a folder of markdown something you can rely on six months from now.

---

## The team angle

I've been running this as a personal tool, but the pattern doesn't require it to be.

The same mechanics work for a small team: raw sources, wiki pages, schema file, index, log. Swap the personal `CLAUDE.md` for a team schema that defines company-level conventions. Replace Obsidian with any markdown viewer or GitHub's built-in rendering, use Git for version control, and GitHub for access management. The AI becomes a maintainer of shared knowledge. Multiple contributors add source documents; the model synthesizes, cross-links, and keeps the wiki current.

What changes is the governance layer. The schema needs to define domains more carefully and account for the fact that different people will carry different mental models of the same information. The core loop translates directly: read, synthesize, flag contradictions, update index, append log. That loop doesn't care whether one person is feeding it or ten.

I'm pitching it to a friend of mine to try on a group project now, so I'm excited to see where that goes. I will report back if we make progress.

---

## Where it goes

It's been a few days. I don't have a verdict on whether this compounds the way I think it will.

What I have: I already know where to look for things. The index is genuinely useful. The log tells me what I was thinking two days ago in a way chat history doesn't. When I open a new Claude Code session on this repository, the model reads three files and immediately knows me and my life. That handoff works.

The questions that remain: Does the wiki remain useful at 200 pages? Does the schema hold when the domains get messier? Does the ingestion discipline hold up over weeks when there's no time to be methodical?

I don't know yet. But I'm building this. You're welcome to watch.

---

*Built on Andrej Karpathy's `CLAUDE.md` pattern. Initial [Obsidian](https://obsidian.md) + [Claude Code](https://claude.ai/code) setup and starter prompts from [Rui Fu](https://www.raycfu.com/).*
