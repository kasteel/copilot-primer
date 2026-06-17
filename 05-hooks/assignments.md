# Assignments

> **Working in pairs.** Each assignment is designed for a pair. You do not need to write down every observation. Discuss with your partner and capture **2–3 take-aways** per assignment that you would share with the rest of the team.

## Assignment 1: Add A Ruff Hook

Goal: convert a repo preference into an actual post-edit guardrail.

Tasks:

1. Paste the Ruff hook snippet from the [chapter README](README.md#the-ruff-hook-snippet) into `.github/hooks/ruff.json` in your workspace. Confirm it loads via the GitHub Copilot Chat Hooks output channel.
2. Keep the command narrow enough to be practical for repeated use.
3. Ask Copilot to revise an API or service file.
4. Observe what the hook runs and what feedback it produces.
5. Note whether the feedback is actionable or merely noisy.

Discuss with your pair and capture **2–3 take-aways**. Useful prompts:

- what the hook actually enforced
- whether the cost of the hook felt justified
- whether the command scope should be narrower or broader

Expected outcome:

- You should be able to explain why this hook is valuable in workflow terms, not just that it can run.

## Assignment 2: Compare Instructions Versus Hooks

Goal: separate guidance from enforcement using the same repository convention.

Tasks:

1. Add an instruction that prefers clean Ruff-compliant code.
2. Make or request a change that could violate style, make sure there is no ruff hook present (delete or rename `.github/hooks/ruff.json`).
3. Observe what happens with instruction-only guidance.
4. Repeat the same style of change with the hook enabled.
5. Compare the outcomes.

Discuss with your pair and capture **2–3 take-aways**. Useful prompts:

- what the instruction influenced
- what only the hook could guarantee
- whether both mechanisms together produced a better workflow than either one alone

Expected insight:

- Instructions bias behavior; hooks constrain behavior.
