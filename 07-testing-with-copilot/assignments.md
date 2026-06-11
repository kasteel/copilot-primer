# Assignments

## Assignment 1: Add Endpoint Tests

Goal: use Copilot to build tests around a new or changed endpoint.

Tasks:

1. Add a small API change in `python-app/app/api/`.
2. Ask Copilot to extend `python-app/tests/test_api.py`.
3. Inspect the assertions for quality, not just quantity.
4. Run the test suite through the repo workflow.

## Assignment 2: Add Edge Cases

Goal: find missing scenarios.

Tasks:

1. Pick one endpoint.
2. Ask Copilot for edge cases around invalid IDs, limits, or missing data.
3. Keep the cases that improve confidence and delete the weak ones.

Expected observations:

- Copilot is useful for test ideas.
- You still need to filter and tighten the output.
