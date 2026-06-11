# Hooks

## What It Is

Hooks let you run deterministic automation around Copilot actions. They are useful when guidance is not enough and you want an actual command to run.

## When To Use It

Use hooks when:

- a lint or format step should always run
- dangerous commands should be blocked
- you want repeatable validation around Copilot edits

## How It Works

Hooks run at specific lifecycle points. In this course, the key exercise is a Ruff-based hook that runs after Copilot-driven Python changes.

## Cool

- Hooks enforce behavior instead of only suggesting it.
- They work well with team tooling.
- They make the feedback loop visible.

## Not Cool

- They need careful setup.
- They can be noisy if they run too broadly.
- They should stay simple and predictable.

## Project-Specific Example

This repository uses hooks to demonstrate where `ruff` enforcement helps more than instructions alone.

## Tips

- Keep hook scope clear.
- Prefer small commands with obvious outcomes.
- Compare hook behavior with instruction behavior on the same edit.
