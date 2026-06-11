# Assignments

## Assignment 1: Add A Ruff Hook

Goal: convert a repo preference into an actual post-edit guardrail.

Tasks:

1. Configure a hook that runs a Ruff command in `python-app` after relevant Copilot-driven Python changes.
2. Keep the command narrow enough to be practical for repeated use.
3. Ask Copilot to revise an API or service file.
4. Observe what the hook runs and what feedback it produces.
5. Record whether the feedback is actionable or merely noisy.

Write down:

- what the hook actually enforced
- whether the cost of the hook felt justified
- whether the command scope should be narrower or broader

Expected outcome:

- You should be able to explain why this hook is valuable in workflow terms, not just that it can run.

## Assignment 2: Compare Instructions Versus Hooks

Goal: separate guidance from enforcement using the same repository convention.

Tasks:

1. Add an instruction that prefers clean Ruff-compliant code.
2. Make or request a change that could violate style.
3. Observe what happens with instruction-only guidance.
4. Repeat the same style of change with the hook enabled.
5. Compare the outcomes.

Write down:

- what the instruction influenced
- what only the hook could guarantee
- whether both mechanisms together produced a better workflow than either one alone

Expected insight:

- Instructions bias behavior; hooks constrain behavior.
