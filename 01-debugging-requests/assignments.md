# Assignments

## Assignment 1: Draw The Request

Goal: build a concrete mental model of what a basic Copilot code request is made of.

Tasks:

1. Open one file in `python-app`, for example `python-app/app/api/orders.py`.
2. Ask Copilot for one small change.
3. Open the Chat Debug view.
4. On paper, draw the building blocks of the request as you observe them.

Your drawing should include stuff like:

- your typed request
- system prompt or orchestration instructions
- attached context
- tool availability
- conversation history if present
- response payload or tool response linkage

Expected outcome:

- You should end with a sketched architecture of a basic Copilot request, not just a list of labels.

## Assignment 2: Investigate Token Consumption

Goal: connect prompt shape to token cost, cache behavior, and latency.

Preflight: this assignment assumes Agent Debug Log capture and file logging are enabled in the current VS Code window. This repository ships those settings in `.vscode/settings.json`, but if the logs still show empty token or model-turn fields, start a fresh chat session after confirming the settings are active.

Tasks:

1. Open the Agent Debug Logs panel for an active session.
2. Send a small request, then repeat it with a small variation.
3. Send a broader request, then repeat it with a light alteration.
4. Inspect token usage, duration, and cache information for both pairs.
5. Use the Cache Explorer to compare consecutive model turns.

Use these concrete examples:

- Small request: `Explain what the /health endpoint returns in python-app/app/main.py and whether returning the database path is a good idea.`
- Small variation: `Briefly explain what the /health endpoint returns in python-app/app/main.py and whether returning the database path is a good idea.`
- Broader request: `Review python-app/app/main.py, python-app/app/api/orders.py, python-app/app/services/order_service.py, and python-app/app/repositories/order_repository.py and propose how to extend /orders/recent with one extra response field, including what would need to change in tests.`
- Lightly altered broader request: `Review python-app/app/main.py, python-app/app/api/orders.py, python-app/app/services/order_service.py, python-app/app/repositories/order_repository.py, and python-app/tests/test_api.py and propose how to extend /orders/recent with one extra response field, including what would need to change in tests.`

For the small pair, explicitly check whether prompt caching is reused.

For the broader pair, explicitly check whether cache reuse drops or breaks after the altered request.

Write down:

- did token usage increase with the bigger request? Why?
- whether cache reuse improved or degraded
- whether the broader request was actually worth the added cost

Expected observations:

- Small prompt variations often preserve more cache reuse than broader context changes.
- Cache misses and unnecessary context expansion have a real cost in both latency and tokens.
