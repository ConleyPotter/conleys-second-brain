# Designing, Refining, and Maintaining Agent Skills at Perplexity

**Source:** https://research.perplexity.ai/articles/designing-refining-and-maintaining-agent-skills-at-perplexity
**Author:** Perplexity Agents team
**Published:** 2026-05-01
**Captured:** 2026-05-16

---

Perplexity's frontier agent products rest on a foundation of know-how and domain expertise packaged in modular [Agent Skills](https://agentskills.io/home). We maintain a carefully curated library of Skills across our technical environments. These Skills include many of the general-purpose utilities powering [Perplexity Computer](https://www.perplexity.ai/products/computer); vertical-specific capabilities in areas such as finance, law, and health; and a very long tail of modules for addressing user needs. Some Skills are infrequently invoked but critical when invoked. To ensure a consistently excellent user experience, Perplexity's Agents team prioritizes Skill quality just as much as code quality.

The intuitions and best practices required to develop a high-quality Skill differ significantly from those required to build traditional software. The Agents team reviews many pull requests from excellent engineers who develop Skills in the course of their work. The result is almost always numerous comments and suggestions for revision. This is because many useful patterns for writing code become antipatterns in Skill creation.

For example, if you take some of the aphorisms from [PEP20 – The Zen of Python](https://peps.python.org/pep-0020/), it quickly becomes clear that writing good Python code is unlike writing good Skills. Of the 20 lines of wisdom, at least half are fully wrong or actively misleading when writing Skills. Here are five of them:

| Zen of Python | Zen of Skills |
|---|---|
| Simple is better than complex | A Skill is a folder, not a file. Complexity is the feature. |
| Explicit is better than implicit | Activation is implicit pattern matching. Progressive disclosure. |
| Sparse is better than dense | Context is expensive. Maximum signal per token. |
| Special cases aren't special enough to break the rules | Gotchas ARE the special cases (they're the highest-value content). |
| If the implementation is easy to explain, it may be a good idea | If it's easy to explain, the model already knows it. Delete it. |

This guide is the document that engineers across Perplexity use when developing and reviewing Skills. We're also releasing this guide to the public so that our discoveries and learnings can benefit the broader community. Whether you're an engineer designing production Skills in your day-to-day work, a Computer user looking to develop your own Skill in an area you know best, or both, this guide is for you.

## What is a Skill?

When you write a Skill, you aren't writing plain old software (even though Skills are now part of the main logical engines for agent systems). Rather, you're building context for models and their environments. A Skill has different constraints and different design principles. If you write a Skill like you do code, you will fail.

A Skill is at least four things, especially in the context of how we build them at Perplexity.

### A Skill is a Directory

A Skill is not just a single `SKILL.md` file. In many cases, a Skill includes several files. Under the directory named after your Skill, you might have:

- `SKILL.md`: frontmatter and instructions
- `scripts/`: code the agent runs, not reinvents
- `references/`: heavy docs, loaded conditionally
- `assets/`: templates, schemas, and data
- `config.json`: first-run user setup

This hub-and-spoke pattern allows you to keep Skills very focused and tight, and one can use the folder structure in a very creative way. Sometimes, particularly intricate Skills benefit from multiple levels of hierarchy to help the model navigate better. Suppose a Skill requires knowledge across 300 topics, groupable into 20 subject matter areas. Reliably choosing the right topic among 300 is an unsolved challenge even for today's best frontier models. It's a much easier choice problem for a model to hone in on one of 20 areas, than among the 15 topics within that area.

As one example of how multilevel hierarchy can work, consider a Skill for the many different types of software developer roles. You might imagine a top-level `SKILL.md` that talks about what kind of developers there are (frontend, backend, platform, data, ML, and so on), which then links to sub-Skills, each containing relevant context for each type. The multi-level approach is an important technique to support effective Skill navigation.

### A Skill is a Format

A Skill is a format. The core root `SKILL.md` file must have both a name and a description. Furthermore, the Skill needs to exactly map to the directory name in which the Skill is located. The name must be all lower-case characters, have no spaces, and can use hyphens. The description is the routing trigger. This is a common failure point: the description is not internal documentation for what the Skill does. It amounts to instructions for the model for when to load the Skill. So, you will frequently see "Load when," not "This Skill does." This is important because of the way that most implementations inject the description into the model context.

### A Skill is Invocable

A Skill is invocable. The agent loads a Skill at runtime. Importantly, Skills aren't always bundled into the context. By default, most agent systems unfold Skills progressively upon specific need.

### A Skill is Progressive

Skills are progressive. In Computer, there are three different tiers of context costs, and we incur all three at various stages:

Computer builds a Skill index that has the name and the description for every available Skill. The budget for this is around 100 tokens per Skill (shorter is even better). It's so tight because you're paying this cost in every session, for every user. This is injected into the system prompt at the very beginning of the conversation. The model has access to a bunch of named Skills and descriptions so that it can decide whether to call "`load_skill()`". The bar to getting into this index is extremely high. Your Skill needs to be very useful, and the description needs to be extremely dense and terse because everyone is paying the cost all the time.

When the model calls `load_skill()`, Computer injects the full `SKILL.md` file into the conversation — this is the second tier of context cost. It's not free, but it's only paid when someone explicitly needs the Skill. The third and final tier is any files that the Skill itself loads conditionally, such as files from `references/` or `assets/`. These are loaded only when needed during execution, keeping the default cost low.

## When do you need a Skill?

The Agents team is often asked to opine on whether a Skill is truly needed for a given domain or use case. Very rarely do we have a definitive answer from first principles alone. The only way to really figure this out is to start with your agent without the Skill, run several hero queries, and then figure out whether the agent is doing a good job.

There are many tasks that are in distribution for trained models. You only need to apply a Skill if you want to change that behavior in some specific way that you can't with say, one sentence in your prompt. So, you need a Skill when the agent will get it wrong without special context, or if there's some inconsistency or non-determinism that you need to be extremely consistent across runs.

Just like Pascal, you need to invest time in every Skill. It is hard to write a short Skill. If your Skill is easy to write, it is probably too long or shouldn't exist. A good Skill is as short as it can be.

## How to build a Skill

Put another way, you need to inject your opinion into any Skill that you write. Follow these steps.

Before you start: Write some of the evals.

### Step 1: The Description

This is the hardest line in the Skill. It's a routing trigger, not documentation. To get the name and the description right, you don't care about the content of the Skill. You only care about whether the Skill is loaded and injected at the right points and is free of off-target side effects, which is the number one failure mode. Every time you add an additional Skill, you risk making every other Skill slightly worse, so you need to make sure that you're minimizing regression.

Again, a bad description describes what the Skill does or why it is useful. A good description says when the agent should load the Skill. For example, say you have something for monitoring pull requests. Don't write what the Skill does. Write what engineers say when they're frustrated and they want you to make sure that their PR works, like "babysit" or "watch CI" or "make sure this lands."

### Step 2: Write the Body

Once you have the description right, you write the body of the Skill. The body is where you put what the agent needs to do. The body should contain:

- **Gotchas**: Non-obvious things the agent might otherwise get wrong. High-value content. These are your special cases, your edge cases, your "this is the thing that will bite you."
- **Context that the model lacks**: Things that are out-of-distribution for the model — your organization's specific jargon, processes, internal systems, the layout of your codebase, etc.
- **Checklists and workflows**: Step-by-step instructions that should be followed consistently across every invocation.
- **References to scripts and assets**: Rather than inlining long code blocks or large data structures, reference external files in `scripts/` and `assets/`.

The body should not contain:

- **Things the model already knows**: If it's easy to explain, the model already knows it. Delete it.
- **Generic best practices**: These belong in a general agent prompt, not a Skill.
- **Long prose explanations**: Dense, terse instructions are better. Redundancy is waste.

The goal is maximum signal per token. Every line should be pulling its weight.

### Step 3: Use the Hierarchy

If your Skill is getting too large — meaning it covers too many distinct topics, requires too many sub-topics, or would need a lot of references — break it into a hierarchy. A top-level Skill provides a map. Sub-Skills provide detail.

A few rules of thumb:

- If a Skill covers more than ~15-20 distinct topics, consider grouping them.
- If a Skill has more than ~500-700 tokens in its body, consider splitting.
- Sub-Skills should be self-contained and loadable independently.

### Step 4: Iterate

The Skill you write first is not the Skill you ship. You will discover gotchas, update the description, and add sub-Skills as you run it against real queries and see where it fails.

This iteration process is intentional. You should plan to:

1. Run the Skill against your hero set (the set of queries where it should load and succeed).
2. Run the Skill against your adversarial set (queries where it should NOT load).
3. Update based on failures — primarily the description and the gotchas section.
4. Re-run evals until precision and recall are satisfactory.

The evals are not a formality. They are the mechanism by which you verify the Skill is working. Don't skip them.

## How to Maintain a Skill

From this point on, your list of gotchas tends to grow or change a lot. We often see engineers who make PRs that are un-evaled, for example, change the description. If you're changing the description after your Skill has been merged, you are off track. If you're making changes to the thing that decides whether to route your Skill, you need to write some evals that support the changes.

### Eval Suites

At Perplexity, we run many eval suites to check for different things. There are Skill loading and Skill file reads, which checks the precision, recall, and forbidden checks of the Skill loading itself. Will the agent route your Skill when it's supposed to? These ensure new Skills don't break existing boundaries.

The key eval dimensions are:

- **Precision**: Does the Skill load when it should?
- **Recall**: Does the Skill NOT load when it shouldn't?
- **Forbidden loads**: Does the Skill avoid loading when adjacent Skills are more appropriate?
- **File reads**: When the Skill is loaded, does it read the right sub-files?
- **End-to-end quality**: Given the Skill loads correctly, does the agent produce the right output?

Every PR that touches a Skill's description, name, or routing logic must include eval changes that validate the change.

### Final Thoughts and Takeaways

The more Skills you build, the better you will get at building them. If you're not automating or trying to make more reproducible tasks that you're doing on a day-to-day basis using Skills, start immediately.

Key takeaways:

1. Write evals before the Skill. Include negative examples and forbidden loads for adjacent but distinct skills.
2. The description is the hard part. "Load when..." (every word costs attention).
3. Gotchas are extremely high-value content. Start thin, grow as the agent fails.
4. A Skill is a directory, not a file. Use the hub-and-spoke structure.
5. Context is expensive. Maximum signal per token — if the model already knows it, delete it.
6. Use hierarchy when topics exceed ~15-20; never let a single file do too much.
7. Never merge a description change without evals that cover the new routing behavior.

Use all the available tools every time you're writing and maintaining a Skill. If you want to learn more, the Agent Skills website has plenty of good examples, and both our internal repository and the public ecosystem contain many examples of well-designed Skills.
