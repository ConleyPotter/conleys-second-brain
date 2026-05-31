---
type: synthesis
domain: general
tags: [ai-risk, software-engineering, mitchell-hashimoto, infrastructure, mtbf-mttr]
created: 2026-05-17
updated: 2026-05-17
sources: [mitchellh-ai-psychosis-software-development.md]
---

# Mitchell Hashimoto on "AI Psychosis" in Software Development

Mitchell Hashimoto (@mitchellh, co-founder of HashiCorp) posted a widely-shared thread warning about "AI psychosis" in software development — a pattern where organizations adopt AI-assisted development with an uncritical "MTTR is all you need" mentality.

## The Core Argument

Hashimoto draws a direct parallel to the **MTBF vs. MTTR reckoning** during the cloud infrastructure transition:

- **Then**: infrastructure teams argued that mean-time-to-recovery trumped mean-time-between-failure — "just automate the fix."
- **Now**: the same logic is applied to AI-assisted software development — "it's fine to ship bugs because the agents will fix them so quickly and at a scale humans can't."

The infrastructure world learned that **MTTR alone creates resilient catastrophe machines**: systems that appear healthy by local metrics while globally becoming incomprehensible.

## Warning Signs (Hashimoto's Parallels)

| Infrastructure era | AI development era |
|---|---|
| Automated recovery masks cascading failures | Bug reports go down while latent risk explodes |
| Local metrics healthy, global architecture decaying | Test coverage rises while semantic understanding falls |
| Nobody notices the underlying infrastructure rot | Changes happen so fast nobody notices architecture decay |
| "We have full monitoring" dismissals | "It has full test coverage" dismissals |

## Why Conversations Are Blocked

Hashimoto notes that raising this concern leads to immediate dismissals citing surface-level metrics: "no no, it has full test coverage" or "bug reports are going down." These local signals genuinely improve under AI assistance — the problem is they don't paint the whole picture.

## Relevance

- At 12K+ likes and 1M+ views, this resonated broadly across the engineering community
- Directly relevant to the [[personal-brand-engine]]'s positioning in AI-augmented work
- Connects to the [[operating-doctrine-2026]]'s emphasis on using AI as leverage without losing comprehension
- A useful counterpoint when evangelizing AI workflows: acknowledge the real risk of over-delegation

> **Note:** This captures Hashimoto's May 2026 thread. The discussion is ongoing and may evolve into a longer-form piece.
