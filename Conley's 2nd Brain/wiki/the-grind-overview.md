---
type: operations
domain: long-game-studios
tags: [the-grind, game, phaser, arcade]
created: 2026-06-05
updated: 2026-06-09
sources: [lgs-the-grind]
---

# The Grind — Product Overview

The Grind is a cozy dungeon crawler browser game — the first LGS Arcade title, mapped to the Campfire region ($0–$1K MRR). It is a content asset for Long Game Studios' build-in-public brand, not a revenue product. Players earn gold (1:1 to MRR), and the public scoreboard reflects real studio revenue including $0.

**Repo:** `ConleyPotter/lgs-the-grind` (private, TypeScript, Phaser 3)
**Stage:** Core loop playable (gray-box). RunManager + combat + scene transitions wired. 103 tests passing. First ADR recorded.

---

## Design

- **Genre:** Cozy dungeon crawler
- **Surface:** Campfire region overworld + dungeon levels
- **Currency:** Gold (1 gold = $1 MRR, displayed honestly)
- **Failure:** Soft and funny — "Back to the grind..." not "YOU DIED"
- **Cats:** Luna (all-black, observant) and Juni (tuxedo, expressive) wander as warmth
- **Art style:** Pixel art for game scenes and environmental textures only; warm cartoon/sticker for characters (never semi-realistic Pixar-adjacent)

### Brand golden rules (from CLAUDE.md)

1. Juni is spelled Juni (not Junie) in all game content
2. 7-color palette: cream #F6E6C9, golden yellow #FFD48A, coral #FF9E6B, ember amber #A25C3A, forest green #6B8C6A, twilight blue #4A6A7A, near-black #2F3342
3. Soft failure language only
4. Pixel art only in-game; never for character illustrations
5. Cats are warmth, not background texture
6. Gold = MRR displayed honestly (including $0)

---

## Core systems (implemented)

### RunManager (`src/systems/RunManager.ts`)

Owns the full run lifecycle: `startRun`, `collectGold`, `applyDamage`, `advanceDepth`, `endRun` (banked or lost), `isPlayerDead`. Manages two state tiers:
- `RunState` — volatile, per-run (HP, depth, gold collected this run)
- `MetaState` — persistent (banked gold, carried across runs)

A lost run returns "Back to the grind..." and never banks gold. Double-banking is guarded by an `isActive` check on `requireRun()`.

### Combat (`src/systems/combat.ts`)

Pure functions with no Phaser dependency: `attack` (immutable, clamps health to 0), `isDefeated`, `computeGoldReward`. Fully unit-testable without a browser.

### Scenes

- `CampfireScene` — Hub entry point. Accepts returning `MetaState` via `init()`. SPACE descends to dungeon.
- `DungeonScene` — Run scene. Constructs fresh `RunManager`, binds B (bank) and L (lose). Returns to Campfire or GameOver with updated state.
- `GameOverScene` — Soft failure display. Captures MetaState and fail message. SPACE restarts at Campfire with banked gold preserved.

---

## Tech stack

| Layer | Technology |
|-------|-----------|
| Framework | Phaser 3 |
| Bundler | Vite |
| Language | TypeScript (strict) |
| Testing | Vitest (103 passing tests) |
| Build output | Static web (no backend, no PII, localStorage only) |
| Package manager | npm |

## ADRs

| # | Decision | Status |
|---|----------|--------|
| 0001 | Phaser 3 over Godot 4 | Accepted |

Godot 4 documented as the scaling alternative if a second arcade game enters build.

## Backlog

22 issues seeded (#1–#22) in three horizons:

| Horizon | Issues | Scope |
|---------|--------|-------|
| Now (#1–#7) | P0 bootstrap, core scene, dungeon generation, player movement, inventory |  |
| Next (#8–#16) | Combat, enemy AI, loot tables, progression, audio, save system |  |
| Later (#17–#22) | Overworld, NPC dialogue, boss encounters, accessibility, polish |  |

Issues #3 (core loop) and #4 (scene transitions) closed this period.

## Development workflow

Same TDD discipline as DailyChew:
- `/tdd-from-issue` → `/implement-from-issue` Claude Code skills
- Scope contract: vertical-slice-is-the-contract; never steal hours from DailyChew

No CI pipeline yet. DEVOPS.md documents the planned gates: build + unit + brand lints (Juni spelling, soft failure language, palette enforcement).

## Deployment

Static web build. Will be embedded via iframe on the LGS site. No backend, no user accounts, no server — the game runs entirely in the browser with localStorage for save state.

---

*Last dev-log: [[lgs-devrecap-2026-06-09]]*
