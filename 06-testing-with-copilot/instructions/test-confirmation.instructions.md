---
description: "Use when writing tests, updating or reviewing python-app/tests/test_api.py, generating endpoint tests, refactoring test files, or deciding whether a code change deserves a new test. Require a short summary step with PROCEED, MODIFY, or SKIP before editing tests."
applyTo: "python-app/tests/**"
---

# Test Confirmation Workflow

- For requests about writing, reviewing, removing, refactoring, updating, or extending tests, do not edit tests in the first response.
- First give a short paragraph that summarizes what test changes you are considering and what behavior, regression, or cleanup goal they would cover.
- End that first response by asking the user to reply with exactly one of these keywords: `PROCEED`, `MODIFY`, or `SKIP`.
- If the user replies with `PROCEED`, implement the test change.
- If the user replies with `MODIFY`, revise the proposed test focus, explain the revision briefly, and wait for `PROCEED` before editing tests.
- If the user replies with `SKIP`, do not edit tests. Explain briefly whether the change is large enough to justify a new or updated test.
- Prefer behavior assertions over shallow implementation-shaped assertions.