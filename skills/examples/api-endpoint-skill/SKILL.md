---
name: api-endpoint-skill
description: Help with FastAPI endpoint changes in python-app/api, including response shapes, dependency wiring, and endpoint tests. Not intended for repository or raw SQL changes.
---

Use this skill when the work is primarily about FastAPI routes, request or response models, dependency injection, and endpoint-oriented pytest coverage.

Do not use this skill when the change is primarily about SQLite queries, repository internals, or database bootstrap logic.

Suggested workflow:

1. Inspect the target route file under `python-app/app/api/`.
2. Identify the related service and DTOs.
3. Update endpoint behavior without moving SQL into the route.
4. Extend endpoint tests in `python-app/tests/test_api.py`.
5. Validate through the repo command workflow.
