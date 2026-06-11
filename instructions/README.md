# Instructions

## What It Is

Instructions are markdown files that guide Copilot behavior persistently. They are the right place for coding conventions, architectural rules, and project-specific preferences.

## When To Use It

Use instructions when you want Copilot to consistently respect rules such as:

- routes stay thin
- services own business logic
- repositories own SQL
- Python code should use typing
- commands should run through `just` and `uv`

## How It Works

Instructions can apply broadly or to specific file patterns. They are added as context so Copilot can respond in a way that matches the repository conventions.

## Advantages

- Good for architectural rules and style guidance.
- Reusable across many sessions.
- Easy to inspect in prompt debugging.

## Disadvantages

- They guide behavior but do not enforce it.
- They can become too broad if written without clear scope.
- They do not replace actual validation tools.

## Project-Specific Example

This repository should use instructions to reinforce that:

- FastAPI route functions remain thin
- service classes own business logic
- repository classes own SQLite queries
- `ruff` and `pytest` are part of normal development flow

## Tips

- Keep instructions specific and testable.
- Prefer a few crisp rules over large generic advice blocks.
- Use request debugging to confirm the instruction file was included.
