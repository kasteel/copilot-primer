# Assignments

## Assignment 1: Add A Ruff Hook

Goal: enforce linting or formatting after Copilot edits Python code.

Tasks:

1. Configure a hook that runs `uv run ruff check .` or `uv run ruff format .` in `python-app`.
2. Ask Copilot to revise one of the API or service files.
3. Observe what the hook catches or changes.

## Assignment 2: Compare Instructions Versus Hooks

Goal: understand guidance versus enforcement.

Tasks:

1. Add an instruction about formatting and linting.
2. Make a change that could violate style.
3. Compare whether the instruction alone is enough.
4. Repeat with the hook enabled.

Expected observations:

- Instructions can steer behavior.
- Hooks can enforce it.
