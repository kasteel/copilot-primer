# Skills

## What It Is

Skills package reusable workflows so Copilot can activate them when the request matches the right context.

## When To Use It

Use a skill when you want more than a static rule. A skill is useful when Copilot should follow a repeatable task pattern, such as shaping FastAPI endpoints and related tests.

## How It Works

A skill typically includes a `SKILL.md` description and may include examples or helper resources. The description should be specific enough that the skill activates in the intended context.

## Advantages

- Better for reusable workflows than plain instructions.
- Can include examples and supporting material.
- Useful when only certain kinds of work should trigger extra guidance.

## Disadvantages

- Activation depends on good scoping and descriptions.
- Overly broad skills can show up in the wrong places.
- They still need validation and debugging.

## Project-Specific Example

In this repository, the main skill exercise is intentionally narrow: it should activate when working on FastAPI API files, but not when editing repositories or database code.

## Tips

- Write the skill description around the target work, not around the whole project.
- Compare activation in route files and repository files.
- Use request debugging to confirm your hypothesis.
