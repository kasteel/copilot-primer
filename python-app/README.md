# Shared FastAPI App

This application is the common codebase for the Copilot primer. Every chapter uses this app so that instructions, skills, hooks, edits, tests, and MCP exercises all work against the same architecture.

## Architecture

- `app/api/` contains FastAPI routes.
- `app/services/` contains business logic.
- `app/repositories/` owns SQLite access.
- `app/db/` contains connection and bootstrap logic.
- `tests/` contains `pytest` coverage for the shared workflows.

## Domain

The app models a small order-management system with customers, products, orders, order items, and support tickets.

## Planned Commands

- `just setup`
- `just bootstrap`
- `just run`
- `just lint`
- `just format`
- `just test`

The `Justfile` wraps the underlying `uv`, `ruff`, and `pytest` commands. `just` is not installed on this machine right now, so those recipes are authored but not validated locally in this session.
