# Testing With Copilot

## What It Is

Copilot can help generate, extend, and repair tests, but it should not replace test judgment.

## When To Use It

Use Copilot in testing when you want help with:

- pytest structure
- FastAPI `TestClient` cases
- edge-case discovery
- missing assertions

## How It Works

The best workflow is not “generate tests and trust them.” It is “generate tests, inspect the assertions, run them, and tighten them.”

## Cool

- Fast starting point for endpoint coverage.
- Useful for enumerating edge cases.
- Good fit for regression work after edits.

## Not Cool

- Generated tests can be shallow.
- Copilot may assert the wrong thing confidently.
- Coverage does not guarantee quality.

## Project-Specific Example

The shared FastAPI app already includes `pytest` tests. This chapter uses those tests as the baseline for adding new endpoints or expanding existing cases.

## Tips

- Ask Copilot for specific assertions, not generic coverage.
- Prefer concrete edge cases over vague “more tests.”
- Run tests after every meaningful change.
