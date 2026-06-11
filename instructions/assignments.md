# Assignments

## Assignment 1: Project-Wide Architecture Rules

Goal: create instructions that reinforce the shared FastAPI architecture.

Tasks:

1. Add a project-wide instruction file that says routes stay thin, services own business logic, and repositories own SQL.
2. Ask Copilot to add a new endpoint.
3. Review whether the response respects the boundaries.
4. Use request debugging to confirm the instruction was included.

## Assignment 2: Tooling Rules

Goal: encode team tooling conventions.

Tasks:

1. Add instructions that prefer `just` for common commands, `uv` under the hood, `ruff` for lint and format, and `pytest` for tests.
2. Ask Copilot how to validate a change in `python-app`.
3. Check whether the suggested workflow matches the repo conventions.

## Assignment 3: Scoped Python Instructions

Goal: scope instructions to the right files.

Tasks:

1. Create a Python-scoped instruction file.
2. Add rules about typing and small functions.
3. Compare behavior in a Python file and a markdown file.

Expected observations:

- Scoped instructions should matter only where they apply.
- Project-wide instructions should remain stable across the repo.
