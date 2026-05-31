---
type: synthesis
domain: general
tags: [agent-skills, perplexity, skill-design, llm-patterns, agent-architecture]
created: 2026-05-17
updated: 2026-05-17
sources: [designing-refining-and-maintaining-agent-skills-at-perplexity.md]
---

# Perplexity Agent Skills — Design, Refinement, and Maintenance

Perplexity's Agents team published their internal guide to building and maintaining Agent Skills — the modular knowledge packages powering Perplexity Computer and their vertical-specific agent products. The guide inverts many conventional software engineering intuitions.

## Core Concept: A Skill Is Not Code

A Skill builds **context for models and their environments**, not traditional software. Writing a Skill like code guarantees failure. The Perplexity team contrasts five "Zen of Python" principles with their Skill equivalents:

| Zen of Python | Zen of Skills |
|---|---|
| Simple is better than complex | A Skill is a folder, not a file. Complexity is the feature. |
| Explicit is better than implicit | Activation is implicit pattern matching. Progressive disclosure. |
| Sparse is better than dense | Context is expensive. Maximum signal per token. |
| Special cases aren't special enough | Gotchas ARE the special cases (highest-value content). |
| Easy to explain = good idea | If it's easy to explain, the model already knows it. Delete it. |

## Four Properties of a Skill

1. **A Skill is a Directory** — hub-and-spoke: `SKILL.md` + `scripts/` + `references/` + `assets/` + `config.json`. Multi-level hierarchy helps models navigate large topic spaces (~300 topics → 20 groups → 15 per group).

2. **A Skill is a Format** — name (lowercase, hyphenated, matches directory) + description (routing trigger, not documentation). The description says *when to load*, not *what it does*.

3. **A Skill is Invocable** — loaded at runtime via `load_skill()`, not bundled into every context.

4. **A Skill is Progressive** — three tiers of context cost:
   - **Tier 1 (always paid):** ~100 tokens per Skill in the system prompt index. Every session, every user.
   - **Tier 2 (on load):** Full `SKILL.md` injected when `load_skill()` fires.
   - **Tier 3 (conditional):** References and assets loaded only during execution.

## Building a Skill — Four Steps

1. **The Description** — the hardest line. It's a routing trigger. Bad: "This Skill monitors PRs." Good: "Load when the user says 'babysit', 'watch CI', 'make sure this lands'." Every new Skill risks making every other Skill slightly worse.

2. **The Body** — should contain:
   - **Gotchas**: non-obvious failure modes (highest-value content)
   - **Out-of-distribution context**: org jargon, internal systems, codebase layout
   - **Checklists and workflows**: step-by-step for consistent execution
   - **Script/asset references**: never inline large code blocks
   
   Should NOT contain: things the model already knows, generic best practices, long prose.

3. **Hierarchy** — break Skills exceeding ~15–20 topics or ~500–700 body tokens. Sub-Skills should be self-contained and independently loadable.

4. **Iterate** — run against hero queries (should load + succeed) and adversarial queries (should NOT load). Update description and gotchas based on failures. Re-run evals until precision/recall satisfy.

## Maintenance and Eval Suites

Gotchas grow over time. Any description change post-merge requires supporting evals. Perplexity runs eval suites covering:

- **Precision**: Does the Skill load when it should?
- **Recall**: Does the Skill NOT load when it shouldn't?
- **Forbidden loads**: Avoids loading when adjacent Skills are more appropriate
- **File reads**: Loads correct sub-files when activated
- **End-to-end quality**: Produces correct output given correct loading

## Key Takeaways

1. Write evals before the Skill — include negative examples and forbidden loads
2. The description is the hard part — "Load when..." (every word costs attention)
3. Gotchas are extremely high-value — start thin, grow as the agent fails
4. A Skill is a directory, not a file — use hub-and-spoke structure
5. Maximum signal per token — if the model already knows it, delete it
6. Use hierarchy when topics exceed ~15–20
7. Never merge a description change without evals

## Connections

- Directly applicable to [[second-brain-mcp-server]] and this vault's own Skill architecture
- The progressive disclosure pattern echoes [[gstack]]'s specialist slash command approach
- The "description as routing trigger" principle is relevant to building Hyperagent agent skills
- Contrasts with [[llm-wiki-pattern]]'s emphasis on persistent context — Skills are ephemeral, loaded on demand
