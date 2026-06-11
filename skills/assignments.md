# Assignments

## Assignment 1: Create An API-Focused Skill

Goal: build a skill that helps with FastAPI endpoint work.

Tasks:

1. Create a skill aimed at adding or revising routes, response models, and endpoint tests.
2. Keep the description specific to API-facing work.
3. Test the skill while editing `python-app/app/api/orders.py`.

Expected observations:

- The skill should feel relevant when working on routes and request or response shape.

## Assignment 2: Prove The Boundary

Goal: show that the skill should not activate everywhere.

Tasks:

1. Make a similar request while editing `python-app/app/repositories/order_repository.py`.
2. Compare behavior with the API-layer request.
3. Use request debugging to explain why the skill did or did not activate.

## Assignment 3: Compare Skill Versus Instruction

Goal: understand the difference between workflow packaging and persistent guidance.

Tasks:

1. Write one rule as an instruction and one workflow as a skill.
2. Ask Copilot to do API work and repository work.
3. Record where the instruction helps and where the skill helps.
