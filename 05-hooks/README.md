# Hooks

## What Hooks Are Good For

Hooks are appropriate when you need the system to deterministically run something, not merely remember something.

Good hook use cases include:

- running lint or format checks after edits
- enforcing a validation step before accepting changes
- blocking obviously dangerous operations
- making a repeatable guardrail visible to the team

This is the key conceptual difference from instructions and skills:

- instructions shape general behavior
- skills package specific workflows
- hooks execute deterministic automation

## Why Senior Developers Should Care

Hooks are not just a convenience feature. They are a way to close the gap between AI-generated code and the repository's actual quality contract.

If your team says "all Python edits should pass Ruff" and nothing actually runs Ruff, that rule is aspirational.

Once a hook runs the check, the workflow becomes operational rather than rhetorical.

## How To Think About Hook Design

Good hooks are:

- narrow in scope
- obvious in effect
- cheap enough to run regularly
- tied to a clear quality or safety outcome

Bad hooks are:

- too broad
- too slow
- too surprising
- too complicated to debug

The fastest way to make a hook unpopular is to let it fire constantly for marginal value.

## Hook Moments

Hooks connect to specific lifecycle events in the GitHub Copilot agent loop.

The main hook moments are:

- `SessionStart`: fires when a new chat or agent session begins
- `UserPromptSubmit`: fires when the user sends a prompt
- `PreToolUse`: fires just before Copilot runs a tool
- `PostToolUse`: fires right after a tool completes successfully
- `PreCompact`: fires before the conversation is compacted to save context space
- `SubagentStart`: fires when Copilot starts a subagent
- `SubagentStop`: fires when a subagent finishes
- `Stop`: fires when the agent is about to end its work

For this chapter's example, `PostToolUse` is the important one. In [examples/ruff-hook.json](examples/ruff-hook.json), the Ruff command runs after Copilot has successfully used a tool such as editing files. That makes it a good moment for linting or formatting checks, because the hook runs after the change exists but before you treat the result as done.

The practical pattern is:

- use `PreToolUse` when you want to block or approve something before it happens
- use `PostToolUse` when you want to validate or react to a completed action
- use `Stop` when you want to prevent the agent from finishing before some condition is met

## What Happens When A Hook Runs

When a hook fires, Copilot runs the configured command or script and then inspects how it finished.

The simplest mental model is:

- if the hook succeeds, Copilot continues normally
- if the hook returns a blocking failure, Copilot treats that as a real guardrail
- if the hook returns a non-blocking problem, Copilot can surface the warning and continue

In practice, the result is usually driven by the script's exit code.

- exit code `0`: success. The hook ran and did not block anything.
- exit code `2`: blocking failure. Copilot treats this as a hard stop for that hook outcome.
- other non-zero exit codes: warning or non-blocking failure. The problem is surfaced, but processing can continue.

That is why the example bash script in [examples/ruff-hook.sh](examples/ruff-hook.sh) ends with `exit 2` when Ruff finds issues. The script is saying: this is not just informational feedback, this should block progress until the lint problem is addressed.

So for the Ruff example:

- if Ruff passes, the hook succeeds and Copilot continues
- if Ruff fails and the script exits with `2`, the hook blocks and the failure becomes part of the workflow

What this means in practice:

- the user does get feedback: hook warnings and failures are surfaced in the Copilot workflow, and detailed output can be inspected in the GitHub Copilot Chat Hooks output channel
- a blocking hook failure is also shown back to the agent as context, so the agent can often respond by trying to fix the problem rather than blindly continuing
- that does not mean "automatic retry forever"; it means the failure becomes part of the next decision the agent makes

So if Ruff fails after an edit, the typical outcome is:

1. Copilot makes a change.
2. The `PostToolUse` hook runs Ruff.
3. Ruff fails and the script exits with `2`.
4. The hook blocks further progress for that step and the failure is fed back into the interaction.
5. The agent may then try to repair the lint issue and continue from there.

The main loop risk is with hooks like `Stop` or `SubagentStop`, because those hooks can explicitly tell the agent not to finish yet. If they keep blocking without a real exit condition, you can create a repeated loop. That is why those hook types expose a `stop_hook_active` flag in the hook input, so the hook can notice that it has already blocked once and avoid keeping the agent alive forever.

For normal validation hooks like this chapter's Ruff example, the failure mode is usually not an endless loop. The more common problem is repeated fix-and-check cycles if the agent keeps making changes that still fail validation. That is a workflow concern, but it is not the same as an unbounded hook loop.

More advanced hooks can also return JSON to add warnings or extra context, but the key idea is this: hooks do not just run scripts, they turn script outcomes into visible workflow behavior for both the user and the agent.

## Instructions Versus Hooks

This is a distinction worth teaching explicitly.

If the desired behavior is "please prefer Ruff," that is instruction-shaped.

If the desired behavior is "run Ruff after relevant edits," that is hook-shaped.

One steers. The other enforces.

Teams often need both:

- instructions to bias the model toward good behavior
- hooks to catch the cases where guidance was ignored or insufficient

## Failure Modes

Common hook failure modes include:

- triggering too often
- running an expensive command for a tiny change
- producing noisy output with little actionability
- making the workflow feel hostile rather than informative

The teaching point is not "hooks are powerful." The teaching point is "hooks are a tradeoff between enforcement value and workflow friction."

