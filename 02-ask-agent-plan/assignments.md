# Assignments

## Assignment 1: Compare The Constructed Requests

Goal: investigate what actually changes between `Ask`, `Agent`, and `Plan` for the same task.

Task:

1. Pick one concrete task in `python-app`, such as adding a new query parameter to `/orders/recent`.
2. Send the same task once in `Ask`, once in `Plan`, and once in `Agent`.
3. Open the debug view for each request.
4. Compare at least these aspects:
	- message framing
	- tool visibility or tool use expectations
	- request options or metadata when visible
	- whether the prompt is shaped toward analysis, decomposition, or execution

Expected observations:

- `Plan` should show stronger structuring pressure than `Ask`.
- `Agent` should look more execution-oriented than the other two.
- Some behavior differences may be visible in the prompt, while others may only be inferable from the orchestration behavior.

## Assignment 2: Test The Context Hypothesis

Goal: decide whether `Plan` helps because of mode behavior or because it gives better structure before implementation.

Tasks:

1. Pick a larger change, such as extending a response shape across route, service, repository, DTO, and tests.
2. Ask for the work directly in `Agent` mode.
3. Then repeat the experiment as `Plan` first, followed by `Agent`.
4. Compare the resulting request traces, implementation quality, and validation story.

Write down:

- whether the plan reduced ambiguity
- whether the implementation became narrower or safer
- whether the later `Agent` run looked better scaffolded

## Assignment 3: Match Mode To Failure Pattern

Goal: choose modes based on failure risk rather than habit.

Tasks:

1. Use `Ask` to critique whether a proposed change violates the repository/service boundary.
2. Use `Plan` to decompose a change that touches API, service, and tests.
3. Use `Agent` to execute one reviewed change.
4. For each mode, record what kind of mistake it is most likely to prevent and what kind of mistake it is most likely to introduce.

## Assignment 4: Form And Test A Theory

Goal: treat mode choice as a falsifiable engineering hypothesis.

Tasks:

1. Write one theory about how `Plan` is enforced under the hood.
2. Write one theory about how `Agent` differs from `Ask` at prompt or orchestration level.
3. Use the debug tooling to gather evidence for or against both theories.
4. Mark which parts are directly observed and which parts remain informed inference.

This assignment is complete only when you separate evidence from speculation.
