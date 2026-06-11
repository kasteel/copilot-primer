# Assignments

## Assignment 1: Prove The Activation Boundary

Goal: demonstrate that a good skill activates for the right work and stays out of the wrong work.

Tasks:

1. Look at the example skill. Place it in a folder where Copilot can use it.
2. Make a skill-oriented request while editing `python-app/app/api/orders.py`.
3. Make a similar request while editing `python-app/app/repositories/order_repository.py`.
4. Compare the two interactions.
5. Use debugging to determine whether the skill activated, and if so why.
6. Adjust the skill wording if the boundary worked, to see when it breaks down. Adjust the wording as well when it didn't work, to make it work!

Write down:

- where activation was correct
- where activation was incorrect
- what wording changes improved the boundary

Expected insight:

- A skill is only well designed if its activation boundary is defensible.

## Assignment 2: Create A Skill That Runs A Script

Goal: build a small skill that does more than provide advice by bringing a script into the workflow.

Tasks:

1. Create a new example skill in a location where copilot finds it. Give it a narrow purpose such as generating a silly status report, printing a joke, or summarizing something trivial.
2. Inside that folder, add a `SKILL.md` file with a clear description of when the skill should be used.
3. Add a small script file that the skill can refer to. The script does not need to be meaningful. For example, it could print a fake deployment summary, list a few animal names, or emit a deliberately dramatic success message.
4. In the skill content, tell Copilot that when this kind of task appears, it should run the script as part of the workflow.
5. Keep the skill narrow. It should be obvious when it applies and obvious when it does not.
6. Trigger the skill with a prompt that matches its purpose.
7. Check whether Copilot actually uses the script-aware guidance rather than responding with generic advice.
8. If the skill does not activate or the script is ignored, debug skill description or other failures until it works.

Expected outcome:

- You should end with a small but memorable example of a skill that packages a workflow artifact, not just a rule.
