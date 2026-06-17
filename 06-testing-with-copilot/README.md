# Testing With Copilot

**Builds on:** chapters 03 (scoped test instruction) and 05 (the test-generation gate uses a `UserPromptSubmit` + `PreToolUse` hook).

## What Copilot Is Good At In Testing

Copilot is often useful for:

- creating a first draft of test structure
- suggesting additional endpoint cases
- enumerating edge conditions
- expanding regression coverage after a known code change
- filling in repetitive scaffolding around `pytest` and `TestClient`

Those are real advantages. They reduce typing and help surface scenarios humans might initially forget.

## What Copilot Is Bad At In Testing

Copilot is often weak at:

- choosing the most important assertion
- identifying whether a test is actually meaningful
- distinguishing signal from superficial coverage
- understanding when the real invariant is architectural rather than just syntactic

The common failure mode is a test that technically runs but does not protect the real contract of the system.

## The Correct Testing Workflow

The workflow to teach is not "generate tests." It is:

1. define the behavior or regression that matters
2. ask Copilot for targeted test help
3. inspect every assertion for quality
4. run the tests
5. tighten or discard weak cases

This sequence matters because Copilot is strongest as a test assistant, not as a test authority.

## What Makes A Good Copilot-Generated Test

A good generated test should do at least one of these well:

- protect a real behavior contract
- catch a plausible regression
- make an edge case explicit
- increase confidence in a recent change

A bad generated test usually has one of these smells:

- it restates implementation details without testing behavior
- it asserts something trivial or already guaranteed elsewhere
- it duplicates another test with slightly different wording
- it is broad and noisy but not precise

That distinction is where senior judgment matters most.

## The Test-Generation Gate (Snippet)

The test-generation gate combines a scoped instruction with a hook. The instruction shapes the conversation; the hook enforces the editing contract.

### 1. The scoped instruction

The instruction file in [instructions/test-confirmation.instructions.md](instructions/test-confirmation.instructions.md) is a **template**. Copy it to `.github/instructions/test-confirmation.instructions.md` so Copilot picks it up.

### 2. The hook config

Paste this into `.github/hooks/test-generation-gate.json`:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "type": "command",
        "command": "python3 .github/hooks/test_generation_gate.py",
        "windows": "python .github/hooks/test_generation_gate.py",
        "timeout": 20
      }
    ],
    "PreToolUse": [
      {
        "type": "command",
        "command": "python3 .github/hooks/test_generation_gate.py",
        "windows": "python .github/hooks/test_generation_gate.py",
        "timeout": 20
      }
    ]
  }
}
```

### 3. The gate script (cross-platform Python, fail-closed)

Paste this into `.github/hooks/test_generation_gate.py`. The script is single-purpose: it tracks whether the current session has approved test edits, and denies `PreToolUse` for test-file edits until it has.

```python
#!/usr/bin/env python3
"""Cross-platform test-generation gate. Fail-closed by design."""
from __future__ import annotations

import json
import os
import re
import sys
import tempfile
from pathlib import Path

STATE_DIR = Path(tempfile.gettempdir()) / "copilot-primer-test-gate"
SAFE_ID = re.compile(r"[^A-Za-z0-9_-]")
TEST_PATH_MARKERS = ("python-app/tests/", "test_api.py")
EDIT_TOOL_MARKERS = ("edit", "create", "write", "replace")

DENY_RESPONSE = {
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": (
            "Before editing tests, first summarize the planned test changes "
            "and wait for the user to reply with PROCEED, MODIFY, or SKIP."
        ),
        "additionalContext": (
            "Test-file edits are gated. Summarize the intended test changes "
            "first. Only edit tests after the user replies with PROCEED."
        ),
    }
}


def _state_file(session_id: str) -> Path:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    safe = SAFE_ID.sub("_", session_id)
    return STATE_DIR / f"{safe}.json"


def _write_state(session_id: str, decision: str) -> None:
    _state_file(session_id).write_text(json.dumps({"decision": decision}))


def _read_state(session_id: str) -> str | None:
    path = _state_file(session_id)
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text()).get("decision")
    except (json.JSONDecodeError, OSError):
        return None


def _clear_state(session_id: str) -> None:
    path = _state_file(session_id)
    if path.exists():
        path.unlink()


def _collect_strings(value: object) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        out: list[str] = []
        for v in value.values():
            out.extend(_collect_strings(v))
        return out
    if isinstance(value, (list, tuple)):
        out = []
        for v in value:
            out.extend(_collect_strings(v))
        return out
    return [str(value)]


def _targets_tests(tool_name: str, tool_input: object) -> bool:
    name = (tool_name or "").lower()
    if not any(marker in name for marker in EDIT_TOOL_MARKERS):
        return False
    haystack = "\n".join(_collect_strings(tool_input)).lower()
    return any(marker in haystack for marker in TEST_PATH_MARKERS)


def main() -> int:
    raw = sys.stdin.read()
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        # Fail closed: if we cannot parse the payload, do not approve anything.
        print(json.dumps(DENY_RESPONSE))
        return 0

    event = payload.get("hook_event_name") or payload.get("hookEventName") or ""
    session_id = payload.get("session_id") or payload.get("sessionId") or ""

    if not session_id:
        # Fail closed on missing session id; do not fall back to a shared bucket.
        if event == "PreToolUse" and _targets_tests(
            payload.get("tool_name", ""), payload.get("tool_input")
        ):
            print(json.dumps(DENY_RESPONSE))
        return 0

    if event == "UserPromptSubmit":
        prompt = payload.get("prompt", "") or ""
        if "PROCEED" in prompt:
            _write_state(session_id, "PROCEED")
        elif "MODIFY" in prompt or "SKIP" in prompt:
            _write_state(session_id, "HOLD")
        else:
            _clear_state(session_id)
        return 0

    if event != "PreToolUse":
        return 0

    if not _targets_tests(payload.get("tool_name", ""), payload.get("tool_input")):
        return 0

    if _read_state(session_id) == "PROCEED":
        _clear_state(session_id)
        return 0

    print(json.dumps(DENY_RESPONSE))
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

Three properties of this version that matter:

- **Fail-closed on parse failure:** a malformed payload triggers a deny rather than an empty pass-through.
- **Fail-closed on missing `session_id`:** the script never falls back to a shared `default-session` bucket, so one session's `PROCEED` cannot unlock another session's test edits.
- **No shell-heredoc Python dance:** one file, runs on Windows and POSIX.

