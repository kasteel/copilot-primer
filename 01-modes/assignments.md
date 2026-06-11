# Assignments

## Assignment 1: Compare All Three Modes

Goal: experience how the same task behaves in `Ask`, `Agent`, and `Plan`.

Task:

1. Pick one concrete task in `python-app`, such as adding a new query parameter to `/orders/recent`.
2. Ask Copilot to help in `Plan` mode and review the proposed steps.
3. Ask the same task in `Ask` mode and compare the answer shape.
4. Run the task in `Agent` mode and review the implementation plan and edits.

Expected observations:

- `Plan` should focus on scope, sequence, and validation.
- `Ask` should focus on explanation or suggested code shape.
- `Agent` should move into actual file changes and validation.

## Assignment 2: Match Mode To Risk

Goal: choose the right mode for the right kind of work.

Tasks:

1. Use `Ask` to explain why SQL should stay in repositories in `python-app`.
2. Use `Plan` to outline a safe approach for adding a new summary endpoint.
3. Use `Agent` to make a small implementation change in one chapter or in the shared app.

Write down where each mode felt too weak or too strong for the task.
