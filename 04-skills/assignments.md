# Assignments

## Assignment 1: Create An API-Focused Skill

Goal: design a skill that is clearly more useful than a plain instruction file.

Tasks:

1. Create or refine a skill aimed at adding or revising FastAPI routes, response models, and endpoint tests.
2. Keep the description narrow enough that it clearly targets API-facing work.
3. Trigger the skill while working in `python-app/app/api/orders.py`.
4. Ask Copilot for a realistic route-layer task.
5. Inspect whether the resulting guidance is richer than what a small instruction file alone would have provided.

Write down:

- what the skill appears to contribute
- whether the skill is specific enough to feel intentional
- whether the outcome justified the extra customization surface

Expected outcome:

- The skill should feel like reusable workflow packaging, not a verbose instruction file in disguise.

## Assignment 2: Prove The Activation Boundary

Goal: demonstrate that a good skill activates for the right work and stays out of the wrong work.

Tasks:

1. Make a similar request while editing `python-app/app/repositories/order_repository.py`.
2. Compare behavior with the API-layer request.
3. Use debugging to determine whether the skill activated, and if so why.
4. Adjust the skill wording if the boundary is too broad or too weak.

Write down:

- where activation was correct
- where activation was incorrect
- what wording changes improved the boundary

Expected insight:

- A skill is only well designed if its activation boundary is defensible.
