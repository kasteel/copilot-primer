# Assignments

## Assignment 1: Write Project-Wide Architecture Instructions

Goal: create instruction content that is specific enough to shape behavior and small enough to remain debuggable.

Tasks:

1. Add or revise a project-wide instruction file for the shared FastAPI app.
2. Include only high-value repository rules such as:
	- routes stay thin
	- services own business logic
	- repositories own SQL
	- validation should run through repo-standard commands
3. Ask Copilot to add or revise one endpoint in `python-app/app/api/`.
4. Review whether the result respects the architectural boundaries.
5. Use Chat Debug View to confirm the instruction content was included.

Write down:

- which rules changed the answer meaningfully
- which rules were too vague to observe in practice
- whether the instruction file stayed compact enough to justify its cost

Expected outcome:

- You should end with a small, testable instruction set rather than a long repository manifesto.

## Assignment 2: Encode Tooling And Validation Conventions

Goal: teach Copilot the repository workflow without turning the instruction file into generic process documentation.

Tasks:

1. Add instruction language that makes the preferred command surface explicit:
	- common tasks should go through `just`
	- Python execution should run through `uv`
	- linting and formatting use `ruff`
	- verification uses `pytest`
2. Ask Copilot how to validate a change to the FastAPI app.
3. Compare the answer before and after the tooling instructions are present.
4. Check whether the instruction changes actual command recommendations instead of merely tone.

Write down:

- which workflow suggestions improved
- whether the instruction introduced any ambiguity
- whether the answer became more repository-specific

Expected insight:

- Good instructions move Copilot away from generic workflow advice and toward the actual repo contract.
