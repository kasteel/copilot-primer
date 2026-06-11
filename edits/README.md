# Edits

## What It Is

Copilot Edits are useful when one change spans multiple files and layers.

## When To Use It

Use Edits when a change naturally touches:

- routes
- services
- repositories
- models
- tests

## How It Works

Edits coordinate changes across files so you can review them as one operation instead of a set of disconnected suggestions.

## Advantages

- Good for cross-layer refactors.
- Fits realistic application work.
- Encourages reviewing the whole change, not just one file.

## Disadvantages

- Multi-file changes can hide regressions if reviewed lazily.
- Over-wide edits are harder to reason about.
- Validation becomes more important, not less.

## Project-Specific Example

A good exercise in this repository is adding a new field to a response shape and carrying it through routes, services, repositories, DTOs, and tests.

## Tips

- Use Edits when the change is inherently coordinated.
- Keep the requested change narrow enough to review.
- Validate immediately after the edit sequence.
