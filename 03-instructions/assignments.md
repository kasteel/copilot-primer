# Assignments

## Assignment 1: Observe Scoped Instructions In Context

Goal: see how scoped instructions enter the request only when the active file matches their `applyTo` pattern.

Tasks:

1. Prompt Copilot for help with general Python application code in `python-app/app/`, such as revising a service or repository function.
2. Prompt Copilot for help with Python tests in `python-app/tests/`, such as adding or revising a test.
3. Compare the two requests in Chat Debug View.
4. Check which instruction files were included for the app-code prompt and which were included for the test prompt.
5. Note whether the scoped test instructions changed the answer in a way you could actually observe.

Write down:

- which instructions appeared only for the test prompt
- whether any instructions were broader than they needed to be
- whether the scoped file was specific enough to produce an observable difference

Expected outcome:

- You should see that scoped instructions are part of request context, not universal policy, and that `applyTo` determines when they show up.

## Assignment 2: Change An Instruction And Compare The Result

Goal: observe how even a small instruction edit can change a repeated prompt when the file scope matches.

Tasks:

1. Choose a prompt about Python tests in `python-app/tests/` and run it once with the current scoped instruction file.
2. Edit [examples/python.test.instructions.md](c:\Users\AL31909\wrepos\copilot-primer\03-instructions\examples\python.test.instructions.md) and add a deliberately noticeable rule such as: `Variable names should refer to animals as much as possible.`
3. Run the same prompt again against a matching test file.
4. Compare the two answers and inspect Chat Debug View to confirm that the changed instruction content was included.
5. Remove the funny rule when you are done so the example file returns to a sensible state.

Write down:

- what changed between the first and second answer
- whether the instruction change affected behavior, wording, or both
- how easy it was to verify that the difference came from the scoped instruction file

Expected insight:

- Instructions are inspectable inputs. If you change them and rerun the same prompt in a matching scope, you should be able to observe the effect.
