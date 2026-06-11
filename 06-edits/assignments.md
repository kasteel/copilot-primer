# Assignments

## Assignment 1: Cross-Layer Rename

Goal: use Edits for a coordinated rename that must remain consistent across architectural boundaries.

Tasks:

1. Pick a domain term in `python-app`, such as a response model or DTO name.
2. Ask Copilot to rename it across the relevant route, service, and test files.
3. Review the resulting change as one contract-level refactor rather than a pile of line edits.
4. Validate the result using the repository workflow.

Write down:

- which files had to move together
- whether any layer was missed on the first pass
- what made the rename safe or unsafe to review

Expected outcome:

- You should end with a concrete sense of when Edits preserve consistency better than isolated edits.

## Assignment 2: Add A Response Field Across Layers

Goal: evaluate whether Copilot can carry one contract change cleanly through the application stack.

Tasks:

1. Add one new response field to a customer summary or recent order response.
2. Require updates to the repository query, service mapping, DTO, route output, and tests.
3. Review the edits as one coherent operation.
4. Run a focused validation step immediately afterward.

Write down:

- whether the end-to-end contract stayed coherent
- which layer was easiest to miss
- whether the edit request was narrow enough

Expected insight:

- Edits are strongest when the intended contract change is precise and the validation path is obvious.
