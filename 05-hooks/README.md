# Hooks

**Builds on:** chapter 03 (instructions bias; hooks enforce).

> **Supply-chain warning.** A hook config is a JSON file in a repo that tells Copilot to execute commands on your machine. Always read every `.github/hooks/*.json` and every script it invokes before trusting a cloned repository. The official VS Code guidance is the same: see [Security considerations](https://code.visualstudio.com/docs/agent-customization/hooks#_security-considerations) in the Agent hooks docs.

Canonical reference for everything in this chapter: [Agent hooks in Visual Studio Code](https://code.visualstudio.com/docs/agent-customization/hooks). Hooks are currently marked **Preview**.

## Where Hook Files Must Live

VS Code discovers hook configurations from `.github/hooks/*.json` by default. There is no committed hook config in this repository — the snippet later in this chapter is what you paste into `.github/hooks/ruff.json` in your own workspace.

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

For this chapter's example, `PostToolUse` is the important one. The Ruff command runs after Copilot has successfully used a tool such as editing files. That makes it a good moment for linting or formatting checks, because the hook runs after the change exists but before you treat the result as done.

The practical pattern is:

- use `PreToolUse` when you want to block or approve something before it happens
- use `PostToolUse` when you want to validate or react to a completed action
- use `Stop` when you want to prevent the agent from finishing before some condition is met

## The Ruff Hook (Snippet)

There is no committed hook config in this repo. Paste the snippet below into `.github/hooks/ruff.json` in your workspace to install it:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "type": "command",
        "command": "cd python-app && uv run ruff check app tests scripts",
        "windows": "Set-Location python-app; uv run ruff check app tests scripts",
        "timeout": 20
      }
    ]
  }
}
```

VS Code resolves the `command` field per-OS: it uses `windows` on Windows and the top-level `command` on macOS/Linux. A non-zero exit from `ruff check` blocks the post-tool step (see *Exit codes* below).

## What Happens When A Hook Runs

VS Code gives a hook two ways to influence the workflow: an **exit code** and an **optional JSON response** on stdout. Both are documented in the [Hook input and output](https://code.visualstudio.com/docs/agent-customization/hooks#_hook-input-and-output) section of the official docs.

### Exit codes (the simple model)

The script's exit code drives the basic outcome:

- exit code `0`: success. VS Code parses stdout as JSON (if any).
- exit code `2`: **blocking** failure. The hook's stderr is shown to the model as context. No JSON output is needed.
- any other non-zero code: non-blocking warning surfaced to the user; processing continues.

A Ruff hook that simply calls `uv run ruff check ...` and propagates that exit code already gets the right behavior: ruff returns `0` on clean code and a non-zero on lint failures. To force the failure to be *blocking* (rather than a warning), wrap the command so that any non-zero exit becomes `exit 2`.

### JSON output (the fine-grained model)

When exit code is `0`, VS Code parses stdout as JSON and looks for fields like:

- `continue: false` plus `stopReason` — stops the entire agent session.
- `systemMessage` — warning shown to the user regardless of other decisions.
- `hookSpecificOutput` — hook-event-specific control. For `PreToolUse`, that means `permissionDecision: "allow" | "deny" | "ask"`, which decides exactly one upcoming tool call without stopping the session. Chapter 6's test-generation gate uses this form to deny edits to test files until the user confirms.

When multiple control signals collide, the most restrictive wins (for example, `continue: false` + `permissionDecision: "allow"` still stops the session).

### How the two models combine

- **Quick guardrails:** rely on exit code `2`. Cheap, no JSON parsing required. This is the right shape for the Ruff hook.
- **Per-tool approval / per-tool denial:** return exit code `0` and a JSON `hookSpecificOutput.permissionDecision` from a `PreToolUse` hook. This is the right shape for chapter 6.
- **Context injection without blocking:** return exit code `0` and a `hookSpecificOutput.additionalContext` string — useful from `SessionStart` or `PostToolUse`.

The Ruff hook in this chapter is intentionally on the simple side of that spectrum: a non-zero exit becomes a blocking failure that the agent sees as feedback. The chapter 6 test-generation gate is on the rich side: it returns structured JSON to deny exactly one tool call.

For `Stop` and `SubagentStop` hooks specifically, watch for the `stop_hook_active` flag in the hook input. If your hook keeps returning `decision: "block"` without checking that flag, the agent can be kept alive indefinitely — with real billing impact.

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

