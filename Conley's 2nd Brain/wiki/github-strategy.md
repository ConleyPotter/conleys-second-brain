---
type: strategy
domain: personal
tags: [github, open-source, portfolio, code, career, pbe]
created: 2026-05-06
updated: 2026-05-06
sources: []
---

# GitHub Strategy

**Related:** [[portfolio-projects]], [[personal-brand-engine]], [[content-strategy]], [[career-transition-strategy]]

---

## Goal

Build a GitHub profile that functions as hard proof-of-work for the career transition. A hiring manager or technical hiring partner should look at it and conclude: *this person actually builds things.*

Three things make that impression:
1. A polished profile with a clear README
2. Active, consistent contribution graph — not just burst activity around launches
3. Projects with real READMEs, stars, and visible use

---

## Profile Setup

**Profile README** (`conleypotter/conleypotter/README.md`):
- State clearly what you build (AI systems + marketing automation)
- Link to portfolio website, LinkedIn, Substack
- Show active projects with status badges
- Update quarterly — a stale profile README is worse than none

**Pinned repos (6 slots):** Pin active projects as they're completed. Better to have 2 polished pinned repos than 6 half-built ones. Unpin anything that's obviously unfinished or embarrassing.

**Bio:** Short. "Building AI-powered marketing automation systems. Writing about it at [Substack URL]."

---

## Activity Cadence

Target a contribution graph with consistent activity, not just spikes at launch time.

**Ways to maintain cadence without large time blocks:**
- README updates and documentation improvements count as commits
- Small bug fixes and improvements to existing projects
- Adding a new template to the HubSpot workflow library each week (see [[portfolio-projects]])
- Issue responses and PR reviews on repos you use

A weekly commit to each active project is enough to maintain a visible green graph. The commit doesn't have to be a major feature. Consistent > impressive-but-rare.

---

## Repository Standards

Every public repo needs:

| Element | Standard |
|---|---|
| **README** | Problem statement, solution description, architecture overview, install/usage, screenshots or demo GIF. The README is marketing. |
| **LICENSE** | MIT for open source — makes it clear others can use and modify |
| **CONTRIBUTING.md** | Brief contribution guide — signals maturity, invites community |
| **Release tags** | Version your releases (v1.0.0) — signals "this is stable and real" |
| **Issues** | Enable issues even if you don't expect many — shows you're open to feedback |

A repo without a good README is invisible. A repo with a great README can get stars and forks from people who never read the code.

---

## Open Source Contribution Strategy

Contributions to established external repos serve two purposes: your GitHub name appears in repos people already recognize, and you learn how other teams build — which improves your own code.

**Process:**
1. Identify a repo you actually use (n8n community nodes, LangChain, a HubSpot library)
2. Look at "good first issue" labels
3. Start with documentation improvements — high acceptance rate, real value, low code review overhead
4. Move to bug fixes once comfortable with the codebase
5. Feature contributions last — most likely to require extended discussion

**Don't contribute to repos you don't use.** Low-quality PRs to unrelated repos generate noise, not signal. Compound in the tools that matter to you.

**Target repos (see [[portfolio-projects]] Project 5):**
- n8n community nodes
- LangChain/LangGraph
- Dify or Flowise
- HubSpot API utility libraries

---

## The GitHub → Content Pipeline

GitHub activity should automatically trigger content. This is the key to making the time spent building compound beyond the code itself.

| GitHub event | Content generated |
|---|---|
| Project launched | Substack article + LinkedIn series (3–4 posts) + X thread |
| Major feature shipped | LinkedIn post + X thread |
| 50 stars on a repo | LinkedIn milestone post |
| PR merged to external repo | LinkedIn post + X thread ("I just contributed to [repo]") |
| Interesting architecture decision | X thread showing the diagram |
| README updated with new diagrams | X thread |

**Rule:** Any commit that ships a meaningful feature gets an X thread the same day. Don't batch and forget — the immediacy of the post is part of the signal.

---

## Relationship to Portfolio Projects

[[portfolio-projects]] defines what to build and in what order. This page defines how to show up on the platform once things are built — profile setup, activity standards, contribution strategy, and the GitHub-to-content pipeline.

The two pages work together: portfolio-projects answers *what*; github-strategy answers *how*.
