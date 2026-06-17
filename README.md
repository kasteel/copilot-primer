# Copilot Primer

This repository is a workshop-heavy, self-paced primer for GitHub Copilot features that are useful in day-to-day development. The material is built around one shared FastAPI application so each chapter works against the same codebase instead of isolated snippets.

## Audience

This course is aimed at developers who already use FastAPI regularly and want to work more effectively with GitHub Copilot in VS Code.

> **Read [PARTICIPANTS.md](PARTICIPANTS.md) before starting chapter 01.** It explains which files must stay local (and why a remote ruleset blocks them), and how the pair-work format is expected to run.

## Shared Toolchain

- `just` is the primary command surface for the repository.
- `uv` is used under `just` for Python environment and command execution.
- `ruff` is used for linting and formatting.
- `pytest` is used for verification.

## Copilot Debug Logging

The workshop includes exercises that rely on Agent Debug Logs and cached-turn inspection. This repo does **not** ship a committed `.vscode/settings.json`. Enable the two debug settings locally before starting chapter 01 by adding the snippet below to your workspace `.vscode/settings.json`:

```json
{
  "github.copilot.chat.agentDebugLog.enabled": true,
  "github.copilot.chat.agentDebugLog.fileLogging.enabled": true
}
```

If token, cache, or model-turn fields stay empty during the debugging chapter, start a fresh chat session after confirming those settings are active in the current window.

Note that the file log can contain prompts, attached file contents, and tool I/O. Treat it as you would any other developer log: do not check it in, and clear it before sharing diagnostic output.

## Working In Pairs

The assignments throughout this primer are designed for **pair work**. The expectation is not a written report for every observation; it is a short conversation with your colleague at the end of each assignment, summarized as **2–3 take-aways** that you would share with the rest of the team.

## Course Order

1. `01-debugging-requests` — foundation; later chapters reuse the debug views.
2. `02-ask-agent-plan` — builds on 01 (uses the debug view to compare modes).
3. `03-instructions` — builds on 01 (verifies instruction inclusion in the debug view).
4. `04-skills` — builds on 03 (skills vs instructions).
5. `05-hooks` — builds on 03 (instructions bias, hooks enforce).
6. `06-testing-with-copilot` — builds on 03 and 05 (instruction + hook gate).
7. `07-error-recovery` — builds on 02 and 03 (recovery patterns + boundary instructions).
8. `08-mcps` — independent of earlier chapters, but most useful after 05 and 07.

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

## Supply-Chain Warning

Hooks, MCP servers, and skills all give a repository the ability to **execute or steer code on your machine** the moment Copilot is active. Treat them as untrusted by default:

- Never enable a hook config, MCP server, or skill from a repo you did not write or audit.
- Read any `.github/hooks/`, `.github/skills/`, `.vscode/mcp.json`, `.claude/settings.json`, or `.agents/` content in a freshly cloned repo before letting Copilot touch the workspace.
- For dependency installs, use the internal package mirror. All `uv` installs are routed through Alliander JFrog Artifactory by default (configured in `python-app/pyproject.toml`); authenticate first as described in [docs/registry.md](docs/registry.md). Always install with `uv sync --frozen`; never with `--upgrade` on a managed device.

## Shared App

The shared application lives in `python-app/`. It is a simple FastAPI service backed by SQLite and structured with an API layer, service layer, repository layer, and tests. The dataset is intentionally rich enough to support meaningful MCP exercises.

## Common Commands

The repository exposes common tasks through `just`. The recipes wrap the underlying Python toolchain.

Commands:

- `just doctor` — verify `uv`, `just`, `python3`, and the VS Code CLI are present
- `just setup` — `uv sync --frozen --group dev` (lockfile-pinned)
- `just bootstrap` — create and seed the SQLite database
- `just run` — start the FastAPI server
- `just lint` / `just format`
- `just test`
- `just check`

The `Justfile` is written for Linux shell execution. If you are working on Windows, run it through WSL after installing `just` in that environment.

## Running The App

Use the shared application in `python-app/` as the target for the course exercises.

Suggested flow:

1. Authenticate to Artifactory (see [docs/registry.md](docs/registry.md)) — all dependencies install through the internal mirror, not public PyPI.
2. Run `just setup` to install dependencies.
3. Run `just bootstrap` to create and seed the SQLite database.
4. Run `just run` to start the FastAPI server.

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
