---
type: strategy
domain: long-game-studios
tags: [lgs, studio, dailychew, the-grind]
created: 2026-06-05
updated: 2026-06-09
sources: []
---

# Long Game Studios — Domain Anchor

Long Game Studios (LGS) is a build-in-public product studio co-run by Conley and Sami Potter. It is organized around a public $1M ARR / $83K MRR goal across five regions tied to arcade game themes.

This domain covers both LGS products and the studio-level strategy. Product repos are private; development progress is captured as `work-log` pages in this wiki under the `long-game-studios` domain.

## Products

| Product | Repo | Stack | Stage |
|---------|------|-------|-------|
| [[dailychew-overview\|DailyChew.AI]] | `ConleyPotter/daily-chew-ai` | Next.js, Inngest, LangGraph, GCS, Resend, Drizzle/Postgres, Gemini eval | Backend + eval feature-complete for v0.1 MVP |
| [[the-grind-overview\|The Grind]] | `ConleyPotter/lgs-the-grind` | Vite, Phaser 3, TypeScript, Vitest | Core loop playable (gray-box); 103 tests |

## Region / MRR Map

| Phase | Region | Game | MRR Band |
|-------|--------|------|----------|
| 1 | The Campfire | The Grind (cozy dungeon crawler) | $0 → $1K |
| 2 | The Frontier | The Crossing (trail/route-building) | $1K → $5K |
| 3 | The Machine | The Works (cozy automation builder) | $5K → $25K |
| 4 | The Expedition | The Caravan (party expedition trek) | $25K → $50K |
| 5 | The Summit | The Ascent (endurance climb capstone) | $50K → a million a year |

## Pages in this domain

| Page | Type | Summary |
|------|------|---------|
| [[dailychew-overview]] | operations | DailyChew.AI product overview — architecture, features, dev status |
| [[the-grind-overview]] | operations | The Grind product overview — game design, architecture, dev status |
| [[lgs-devrecap-2026-06-05]] | work-log | First dev-log recap — repo creation through June 5, 2026 |
| [[lgs-devrecap-2026-06-09]] | work-log | Dev-log recap — June 6–9, 2026; eval system, R2→GCS, core loop playable |

## Development cadence

Dev-log recaps are written by the Vault Keeper agent (Dev-Log Capture mode). Each recap synthesizes merged PRs, commits, releases, and CI runs from both product repos into a single archival `work-log` page. Rolling product overview pages are updated with each recap.

Neither repo cuts GitHub Releases yet. Changelogs are synthesized from merged PRs and Conventional Commits.
