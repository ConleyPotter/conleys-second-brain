---
type: draft
status: written
brief: [[2026-04-25-context-debt]]
created: 2026-04-25
tags: [written, ace, ai-workflow, context, second-brain]
---

# You Don't Have a Model Problem. You Have Context Debt.

You don't have a model problem. You have context debt.

Every time your AI gives you inconsistent output, the reflex is to upgrade the model, rewrite the prompt, or switch providers. I did this. It almost never fixed anything.

The problem is context debt.

Context debt is what accumulates when you run AI sessions without ever giving the model a structured picture of your world. You paste in a brief every time. You re-explain your voice. You re-describe your constraints. The model figures out roughly what you need and then forgets it when the session ends. Next session, you start over.

You're not burning time because the model is bad. You're burning time because you never built the thing that would let it work without you.

---

Here's what it looks like when you fix it.

I run a freelance arbitrage pipeline on Upwork. Before I built the scoring gate, I was spending Connects on every job that looked plausible. Industry average reply rate on the platform: around 5%. My cost-per-hire: $192. Not sustainable.

The scoring gate is a Gemini node that knows what a qualified job looks like. Same model. No version upgrade. Just structured context — a scoring rubric, a decision framework, a set of rules baked in before any proposal is drafted. Reply rate went to 25–35%. Cost-per-hire dropped to under $60. Three times better. Same LLM.

That's what retiring context debt looks like.

The lead enrichment side works the same way. My pipeline checks a Supabase table before calling any external API. If I've already enriched a company in Lancaster County, that record costs nothing on the second pull. After three months working the same geography, margins hit 92%. Not because the API got cheaper. Because the context accumulated.

Same structure both times. Spend time once building the thing that knows your world. Every run after that is cheaper than the one before.

---

RAG systems retrieve on demand. They go back to the source every time. Nothing compounds. A real, maintained wiki — where knowledge is compiled once and updated as new material arrives — is structurally different. The second query on a topic is cheaper than the first. The tenth is nearly free.

Context debt is the gap between what your AI could do if it knew your world and what it actually does starting cold every session.

The fix is not a new model. It's a CLAUDE.md. A Supabase table. A scoring rubric. A structured wiki the model can operate from without you re-explaining the same thing for the fourteenth time.

You don't need a custom pipeline to start. You need one document that answers one question: what does this model need to know every time I open a session? Write that down. File it somewhere the model can reach it. That's the build.

It's a construction problem. One weekend. Zero interest after.

The model is not the bottleneck. You are — every time you start from scratch.

Build the context once. Stop paying the tax.
