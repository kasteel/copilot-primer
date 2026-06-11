# Copilot Instructions

- Treat `python-app` as a layered FastAPI service.
- Keep route handlers thin and move business decisions into services.
- Keep raw SQL inside repository classes only.
- Prefer `just` for common repo commands and `uv` under the hood for Python execution.
- Use `ruff` for linting and formatting and `pytest` for verification.
- Preserve typing and small, readable functions.
