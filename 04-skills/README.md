# Skills

## What Skills Are Good For

Skills are useful when the assistant should recognize a particular kind of work and bring in richer, task-shaped guidance only when it is relevant.

That makes skills a better fit than instructions when you need:

- a repeatable workflow
- examples or supporting material tied to that workflow
- context that should activate only in a narrow problem area
- behavior that is more specific than a repo-wide rule

In this repository, a good candidate is FastAPI endpoint work that spans route shape, response models, and endpoint tests.

## Skills Versus Instructions

This distinction matters.

Instructions are best for stable rules that should apply repeatedly across the repository.

Skills are better when:

- the guidance is conditional
- the guidance is workflow-shaped rather than rule-shaped
- the guidance should appear only for a certain category of task

If you put workflow packaging into instructions, the instruction file becomes noisy.

If you put repo-wide conventions into skills, activation becomes fragile and unnecessary.

## How Skill Activation Should Be Understood

Skill activation is not something you should treat as mystical.

A skill usually becomes relevant because the request, files, or task shape match the skill description closely enough to justify attaching it. That means activation quality depends heavily on:

- how clearly the skill describes the target work
- whether the surrounding files and prompt actually match that work
- how narrowly the skill is scoped

This is why overly broad skills often disappoint. A broad skill does not become more helpful by covering more territory. It usually becomes less reliable and harder to debug.

## What Good Skills Look Like

Good skills are:

- narrow enough to activate for the right work
- rich enough to be more useful than a single sentence of instruction
- concrete enough that activation can be tested and explained

Good skill descriptions focus on the job to be done, not on the entire repository identity.

For example, a skill aimed at "adding or revising FastAPI endpoints, response models, and API tests" is much stronger than a skill that says "help with Python in this project."

## Failure Modes

The main failure modes are predictable.

Too broad:

- activates in the wrong places
- adds prompt cost without improving outcomes
- becomes difficult to reason about

Too vague:

- does not activate when expected
- does not materially change the response even when activated

Too ambitious:

- tries to encode too many workflows at once
- blurs boundaries between API, service, repository, testing, and tooling behavior

For senior developers, this chapter should sharpen one habit: if a skill cannot be explained in one sentence, it is probably too wide.

## Debugging Skills

Skills should be verified the same way instructions are verified: with evidence.

You should inspect:

- whether the skill appears when expected
- whether it stays out of unrelated requests
- whether it changes the response enough to justify its existence
- whether its activation boundary matches the design intent

The chapter is successful only if students stop saying "the skill seemed to help" and start saying "the skill activated for this kind of request and not for that one."

## Project-Specific Reading

In this repository, a strong skill boundary would be:

- active for API-layer work such as routes, response models, and endpoint tests
- inactive for repository SQL work or low-level database concerns

That distinction is valuable because it teaches students that activation boundaries are part of the design.

