# Assignments

> **Working in pairs.** Each assignment is designed for a pair. You do not need to write down every observation. Discuss with your partner and capture **2–3 take-aways** per assignment that you would share with the rest of the team.

## Assignment 1: Compare The Constructed Requests

Goal: inspect what actually changes between `Ask`, `Agent`, and `Plan` when the underlying task is held constant.

Tasks:

1. Pick one concrete change in `python-app`, such as extending `/orders/recent` with one additional response field.
2. Send the same core task once in `Ask`, once in `Plan`, and once in `Agent`.
3. Open Chat Debug View for each request.
4. Compare at least these aspects across the three requests:
	- message framing
	- whether the request is shaped toward explanation, decomposition, or execution
	- visible tool declarations or action expectations
	- any visible request options or metadata differences
	- the final response shape that comes back to the UI

Discuss with your pair and capture **2–3 take-aways**. Useful prompts:

- what is directly visible in the constructed request
- what changed in the resulting behavior even when the visible request looked similar
- which differences you can prove and which differences you can only infer

Expected outcome:

- You should end with a concrete comparison of three request shapes, not just a statement that the modes "feel different."

## Assignment 2: Test Whether Plan Helps Because Of Structure

Goal: decide whether `Plan` improves later execution because of hidden mode behavior or because it forces better decomposition before action.

Tasks:

1. Choose a change that touches route, service, repository, and tests.
2. First, ask for that change directly in `Agent` mode.
3. Then reset and repeat the experiment as `Plan` first, followed by `Agent`.
4. Compare the plan quality, implementation quality, and validation path.
5. Use Chat Debug View on the planning step and the execution step to see how the prompts differ.

Use this concrete prompt for both experiments:

`Extend /orders/recent so each item also returns an item_count field. Update the route, service, repository, and tests. Keep the existing architecture boundaries intact.`

Discuss with your pair and capture **2–3 take-aways**. Useful prompts:

- whether the planning step reduced ambiguity
- whether the later execution became narrower or safer
- whether the plan surfaced assumptions that the direct `Agent` path skipped
- whether the improvement came from better decomposition or from some other visible change

Expected outcome:

- You should be able to argue whether `Plan` helped because it changed the request shape, because it improved the human review loop, or both.
