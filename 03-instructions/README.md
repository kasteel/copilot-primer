# Instructions

## What Instructions Are Good For

Instructions are persistent markdown guidance that Copilot can include when constructing requests. They are best used for stable repository rules that you want applied repeatedly.

Good instruction material usually looks like this:

- architectural boundaries
- naming or typing expectations
- preferred command surface
- validation expectations
- language- or file-specific conventions

In this repository, strong examples include:

- routes stay thin
- services own business logic
- repositories own SQL
- commands should go through `just`
- `uv`, `ruff`, and `pytest` are part of the normal workflow

These are useful because they are stable, specific, and testable.

## How Instructions Enter The Request

Instructions are not magic policy objects. They are context.

That matters because context has cost and because context only helps when it is relevant to the request. If an instruction is too broad, too generic, or too verbose, it can consume space without improving behavior.

The practical model is:

- instructions are loaded according to their scope
- relevant instruction content is attached to the request
- the model is guided by that content, but not mechanically forced to obey it

That is why instructions should be written to support reasoning, not to imitate a style guide appendix.

## Project-Wide Versus Scoped Instructions

There are two broad categories worth teaching.

Project-wide instructions:

- useful for repository architecture and workflow rules
- should contain stable, high-value guidance
- should avoid language that is only relevant in one narrow slice of the repo

Scoped instructions:

- useful for language-specific or file-pattern-specific behavior
- should activate only where they are clearly relevant
- help reduce prompt noise compared to one large global file

The tradeoff is straightforward. Broad instructions are simple to manage but easy to bloat. Scoped instructions are more precise but require more deliberate design.

## How To Create Scoped Instructions

Scoped instructions are just instruction files with a scope declaration so Copilot can decide when to load them.

In this chapter's examples, the split looks like this:

- [examples/copilot-instructions.md](examples/copilot-instructions.md) holds repository-wide guidance for the FastAPI app.
- [examples/python.test.instructions.md](examples/python.test.instructions.md) holds test-specific Python guidance that should only apply to matching test files.

The scoped example uses frontmatter like this:

```md
---
applyTo: "python-app/tests/**/*.py"
---
```

That `applyTo` pattern means the instruction content is relevant when the active work touches Python test files under `python-app/tests`. It will not be pulled in for general application code like routes, services, or repositories. That makes the scoping behavior easier to observe than a broad pattern like `python-app/**/*.py`, which would match nearly the whole app.

To create a scoped instruction file:

1. Create a `*.instructions.md` file for the slice of the repo you want to target.
2. Add frontmatter with an `applyTo` glob that matches only the files that should receive the guidance.
3. Keep the body narrow and behavioral, such as language conventions, layering rules, or validation commands for that slice.

For example, [examples/python.test.instructions.md](examples/python.test.instructions.md) is now intentionally scoped just to tests. Its guidance is useful there, but would be noisy or misplaced in general application code:

- keep tests focused on one behavior at a time
- prefer clear setup and explicit assertions
- use the existing `pytest` workflow when tests change
- name tests after the behavior they verify

That is the basic pattern to teach: keep global instructions for repo-wide rules, and create scoped instruction files when a rule only makes sense for a defined part of the tree. A tests-only file makes that visible immediately because you can compare a prompt against `python-app/app/...` with a prompt against `python-app/tests/...` and inspect which instruction file enters context.

## What Good Instructions Look Like

Good instructions have three qualities.

They are specific:

- "routes stay thin and delegate business logic to services" is useful
- "write clean code and follow best practices" is nearly useless

They are testable:

- you can review a response and tell whether the rule was followed
- you can often confirm inclusion using request debugging

They are stable:

- they represent long-lived repository norms rather than temporary task notes

If a rule is temporary, conversational, or task-specific, it usually belongs in the prompt, not in a persistent instruction file.

## What Instructions Are Bad At

Instructions are guidance, not enforcement.

That means they are bad at:

- guaranteeing formatting or lint compliance
- replacing tests or static analysis
- rescuing a vague prompt
- encoding complex workflows that should only activate in narrow contexts

When a team tries to use instructions for those jobs, the common result is disappointment followed by overlong instruction files.

That is the handoff point to later chapters:

- use skills for richer workflow packaging
- use hooks for deterministic enforcement

## Debugging Instructions

Instructions should be treated as observable system inputs.

That means you should verify:

- whether the instruction file was actually included
- whether the scope matched the active file
- whether the wording is precise enough to influence the answer
- whether the instruction changed behavior meaningfully enough to justify its token cost

If you cannot tell whether an instruction helped, the instruction is probably too vague, too broad, or too weakly scoped.