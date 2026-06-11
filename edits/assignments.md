# Assignments

## Assignment 1: Cross-Layer Rename

Goal: use Copilot Edits for a multi-file refactor.

Tasks:

1. Pick a domain term in `python-app`, such as `RecentOrder` or `TopProduct`.
2. Rename it through the relevant DTO, route, service, and tests.
3. Review the coordinated diff.
4. Validate the result with the repo test flow.

## Assignment 2: Add A Response Field

Goal: update more than one architectural layer in one pass.

Tasks:

1. Add a new response field to a customer summary or order response.
2. Update the repository query, service mapping, DTO, route output, and tests.
3. Review the edits as one unit.

Expected observations:

- The change is easier to reason about when the full chain is visible.
- Validation matters more when the edit spans layers.
