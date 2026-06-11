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

## Project-Specific Reading

For this repository, a good instruction strategy would separate:

- repo-wide architecture rules
- tooling and validation expectations
- Python-specific guidance where appropriate

That separation matters because it keeps each instruction file small enough to reason about and easy enough to debug.

