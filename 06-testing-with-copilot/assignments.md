# Assignments

## Assignment 1: Extend Endpoint Tests After A Real Change

Goal: use Copilot to expand tests in a way that protects an actual contract change rather than just increasing line count.

Tasks:

1. Make a small API change in `python-app/app/api/` or one of the supporting layers.
2. Ask Copilot to extend `python-app/tests/test_api.py`.
3. Review every proposed assertion for relevance.
4. Remove or tighten anything that looks superficial.
5. Run the tests through the repository workflow.

Write down:

- which assertion best protects the change you made
- which proposed assertions were weak or redundant
- whether Copilot improved your test design or only your speed

Expected outcome:

- You should end with tests that clearly defend a behavior change, not just tests that happen to pass.

## Assignment 2: Ask For Edge Cases And Filter Aggressively

Goal: use Copilot for scenario discovery without accepting low-signal cases.

Tasks:

1. Pick one endpoint.
2. Ask Copilot for edge cases around invalid IDs, limits, empty data, or missing records.
3. Separate the suggestions into:
   - high-value cases
   - weak or duplicate cases
4. Keep only the cases that materially improve confidence.
5. Explain why the discarded cases were not worth keeping.

Expected insight:

- Copilot is often useful at generating candidate tests, but filtering is where the real engineering happens.
