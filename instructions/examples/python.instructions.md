---
applyTo: "python-app/**/*.py"
---

- Use explicit type annotations on public functions.
- Keep FastAPI route functions focused on HTTP concerns.
- Do not move database access into routes or services.
- When validation is needed, prefer the existing `pytest` and `ruff` workflow.
