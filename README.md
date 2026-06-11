# Copilot Primer

This repository is a workshop-heavy, self-paced primer for GitHub Copilot features that are useful in day-to-day development. The material is built around one shared FastAPI application so each chapter works against the same codebase instead of isolated snippets.

## Audience

This course is aimed at developers who already use FastAPI regularly and want to work more effectively with GitHub Copilot in VS Code.

## Shared Toolchain

- `just` is the primary command surface for the repository.
- `uv` is used under `just` for Python environment and command execution.
- `ruff` is used for linting and formatting.
- `pytest` is used for verification.

## Course Order

1. `modes`
2. `debugging-requests`
3. `instructions`
4. `skills`
5. `hooks`
6. `edits`
7. `testing-with-copilot`
8. `error-recovery`
9. `mcps`

## Ask, Agent, and Plan

| Mode | Best for | Tradeoff |
| --- | --- | --- |
| Ask | Focused questions, quick comparisons, small code explanations | Lowest autonomy, most manual follow-up |
| Agent | End-to-end implementation, edits, validation, and repo-wide tasks | Highest autonomy, needs stronger review |
| Plan | Scoping work, comparing approaches, agreeing on execution before coding | Does not move the code by itself |

## Customizations At A Glance

| Mechanism | Primary use |
| --- | --- |
| Instructions | Guide Copilot behavior with persistent markdown guidance |
| Skills | Package reusable workflows that should activate in the right context |
| Hooks | Enforce deterministic checks or automation around Copilot actions |
| MCPs | Connect Copilot to external tools or data sources through a controlled interface |

## Shared App

The shared application lives in `python-app/`. It is a simple FastAPI service backed by SQLite and structured with an API layer, service layer, repository layer, and tests. The dataset is intentionally rich enough to support meaningful MCP exercises.

## Common Commands

The repository will expose common tasks through `just`. The recipes will wrap the underlying Python toolchain.

Planned commands:

- `just setup`
- `just bootstrap`
- `just run`
- `just lint`
- `just format`
- `just test`

The `Justfile` is written for Linux shell execution. If you are working on Windows, run it through WSL after installing `just` in that environment.

## Running The App

Use the shared application in `python-app/` as the target for the course exercises.

Suggested flow:

1. Run `just setup` to install dependencies.
2. Run `just bootstrap` to create and seed the SQLite database.
3. Run `just run` to start the FastAPI server.

The running server is useful mainly as an API target. If you open the bare localhost URL in a browser, you should not expect a full user interface.

Use these endpoints instead:

- `/docs` for the Swagger UI
- `/openapi.json` for the generated OpenAPI schema
- `/health` for a quick health check

## Chapter Structure

Each chapter should contain:

- `README.md` for the concept explanation
- `assignments.md` for exercises tied to the shared application

## Implementation Notes

- The shared FastAPI app uses repository and service layers so later chapters can reinforce architectural boundaries.
- Error recovery exercises use embedded patches rather than a separate broken branch.
- The MCP chapter uses the same SQLite database as the application, but only through read-only guardrails.
