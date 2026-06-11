# Modes

## What It Is

GitHub Copilot in VS Code can work in different collaboration modes. For this course, the important distinction is between `Ask`, `Agent`, and `Plan`.

## When To Use It

- Use `Ask` when you want focused answers, explanations, or a small suggestion without handing over execution.
- Use `Agent` when you want Copilot to inspect the repository, make edits, and validate changes.
- Use `Plan` when you want to agree on the approach before changes are made.

## How It Works

- `Ask` optimizes for direct answers and local guidance.
- `Agent` optimizes for autonomy across multiple files and validation steps.
- `Plan` optimizes for scoping, sequencing, and tradeoff discussion.

## Advantages

- `Ask` is quick and easy to control.
- `Agent` can carry multi-step implementation work end to end.
- `Plan` reduces ambiguity before work starts.

## Disadvantages

- `Ask` does not carry the work forward for you.
- `Agent` requires more review because it can move faster and wider.
- `Plan` does not change the codebase by itself.

## Project-Specific Example

In this repository:

- Use `Ask` to compare whether a rule belongs in `instructions` or `hooks`.
- Use `Agent` to add a new FastAPI endpoint across routes, services, repositories, and tests.
- Use `Plan` to decide how the MCP chapter should expose read-only SQLite access.

## Tips

- If the task is ambiguous, start with `Plan`.
- If the task touches multiple files and requires validation, prefer `Agent`.
- If you mainly need understanding, prefer `Ask`.
