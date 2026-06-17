# Assignments

> **Working in pairs.** Each assignment is designed for a pair. You do not need to write down every observation. Discuss with your partner and capture **2–3 take-aways** per assignment that you would share with the rest of the team.

## Assignment 1: Extend Endpoint Tests After A Real Change

Goal: use Copilot to expand tests in a way that protects an actual contract change rather than just increasing line count.

Tasks:

1. Make a small API change in `python-app/app/api/` or one of the supporting layers.
2. Ask Copilot to extend `python-app/tests/test_api.py`.
3. Review every proposed assertion for relevance.
4. Remove or tighten anything that looks superficial.
5. Run the tests through the repository workflow.

Then extend the exercise with these additional experiments:

### Experiment A: Add Instructions Or A Skill

Repeat the same test-generation task after changing the surrounding Copilot context.

Try one or both of these:

- add a small instruction that says tests should prefer behavior assertions over implementation-shaped assertions
- add or reuse a skill that is specifically about endpoint and test updates

Use a concrete prompt such as:

`I changed the /orders/recent response. Update python-app/tests/test_api.py so the tests verify the new behavior clearly and avoid shallow assertions.`

Discuss with your pair and capture **2–3 take-aways**. Useful prompts:

- whether the test suggestions became more behavior-focused
- whether the instruction or skill changed the assertions meaningfully
- whether the added customization improved quality enough to justify itself

### Experiment B: Add A Human Gate Before Test Generation

The full gate — instruction file, hook config, and cross-platform Python gate script — is documented as paste-ready snippets in the [chapter README](README.md#the-test-generation-gate-snippet). It is a single Python file that runs on both POSIX and Windows; there is no platform-specific shell version.

The important mechanism is:

- the instruction changes the first test-related response so Copilot must summarize the planned test change and ask for `PROCEED`, `MODIFY`, or `SKIP`
- the `UserPromptSubmit` hook records that decision for the active session
- the `PreToolUse` hook inspects upcoming tool calls and blocks test-file edits until the session has an approved `PROCEED` state
- the hook does not just print text; it returns structured JSON that tells Copilot to deny the test edit and explain why

This works because the instruction shapes the conversation, while the hook enforces the gate at the tool boundary. Either one alone would be weaker:

- the instruction alone can be ignored or bypassed
- the hook alone can block edits, but it does not explain the intended workflow nearly as well

Your task is to install the gate and decide whether it feels smooth in practice.

Suggested scope:

1. Paste the snippets into `.github/instructions/test-confirmation.instructions.md`, `.github/hooks/test-generation-gate.json`, and `.github/hooks/test_generation_gate.py`.
2. Try the full flow on a test-generation request against `python-app/tests/test_api.py`.
3. Try a bypass: ask Copilot to write a test without first saying `PROCEED`. Confirm the gate denies the edit.
4. Decide whether the gate improves the workflow or adds too much friction.

Use prompts like these to test the flow:

- `Update python-app/tests/test_api.py for the new /orders/recent behavior.`
- `MODIFY Focus on one high-value behavior assertion and skip shallow status-code-only checks.`
- `PROCEED`
- `SKIP`

This is a useful exercise because it shows the real boundary between instructions and hooks. The instruction defines the conversation contract. The hook enforces the editing contract.

Discuss with your pair and capture **2–3 take-aways**. Useful prompts:

- which assertion best protects the change you made
- which proposed assertions were weak or redundant
- whether Copilot improved your test design or only your speed
- whether instructions or skills improved the generated tests
- whether the hook gate improved your decision-making or only added friction

Expected outcome:

- You should end with tests that clearly defend a behavior change, not just tests that happen to pass.
