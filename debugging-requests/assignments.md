# Assignments

## Assignment 1: Inspect Instruction Presence

Goal: verify whether your project instructions are really part of the prompt.

Tasks:

1. Open a Python file under `python-app/app/api/`.
2. Ask Copilot to add or revise an endpoint.
3. Open the debug view and inspect whether the relevant instruction files were included.
4. Repeat from a different part of the project and compare the request.

Expected observations:

- Different files can lead to different instruction matches.
- You should be able to confirm instruction inclusion directly in the debug data.

## Assignment 2: Diagnose Skill Activation

Goal: understand why a skill activates for API work but not for repository work.

Tasks:

1. Make one request while focused on `python-app/app/api/customers.py`.
2. Make a similar request while focused on `python-app/app/repositories/customer_repository.py`.
3. Inspect the debug data for both.
4. Record which context differences explain the activation behavior.

## Assignment 3: Compare Prompt Construction

Goal: observe how context changes the request.

Tasks:

1. Open only one route file and ask for a change.
2. Open the route, service, and repository files together and ask the same thing.
3. Compare the resulting requests.

Expected observations:

- The visible context changes the request composition.
- Broader context can help, but it can also widen the problem too early.
