# Assignments

> **Working in pairs.** Each assignment is designed for a pair. You do not need to write down every observation. Discuss with your partner and capture **2–3 take-aways** per assignment that you would share with the rest of the team.

## Assignment 1: Prove The Activation Boundary

Goal: demonstrate that a good skill activates for the right work and stays out of the wrong work.

Tasks:

1. Look at the example skill in [examples/api-endpoint-skill/](examples/api-endpoint-skill). Copy the whole directory to `.github/skills/api-endpoint-skill/` so Copilot can discover it (directory name must match the `name` field in `SKILL.md`).
2. Make a skill-oriented request while editing `python-app/app/api/orders.py`.
3. Make a similar request while editing `python-app/app/repositories/order_repository.py`.
4. Compare the two interactions.
5. Use debugging to determine whether the skill activated, and if so why.
6. Adjust the skill wording if the boundary worked, to see when it breaks down. Adjust the wording as well when it didn't work, to make it work!

Discuss with your pair and capture **2–3 take-aways**. Useful prompts:

- where activation was correct
- where activation was incorrect
- what wording changes improved the boundary

Expected insight:

- A skill is only well designed if its activation boundary is defensible.

## Assignment 2: Create A Skill That Runs A Script

Goal: build a small skill that does more than provide advice by bringing a script into the workflow.

Tasks:

1. Create a new skill directory at `.github/skills/<your-skill-name>/` (the directory name must match the `name` field in the SKILL.md you are about to write). Give it a narrow purpose such as generating a silly status report, printing a joke, or summarizing something trivial.
2. Inside that folder, add a `SKILL.md` file with a clear description of when the skill should be used.
3. Add a small script file that the skill can refer to. Keep the script trivial — print a fake deployment summary, list a few animal names, emit a deliberately dramatic success message. **Only ever ship scripts you wrote yourself**; the same mechanism that runs your harmless joke would happily run anything else.
4. In the skill content, tell Copilot that when this kind of task appears, it should run the script as part of the workflow.
5. Keep the skill narrow. It should be obvious when it applies and obvious when it does not.
6. Trigger the skill with a prompt that matches its purpose.
7. Check whether Copilot actually uses the script-aware guidance rather than responding with generic advice.
8. If the skill does not activate or the script is ignored, debug skill description or other failures until it works.

Expected outcome:

- You should end with a small but memorable example of a skill that packages a workflow artifact, not just a rule.
