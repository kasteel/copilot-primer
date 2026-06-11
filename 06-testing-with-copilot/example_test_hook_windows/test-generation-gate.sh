#!/usr/bin/env sh
set -eu

state_root="${TMPDIR:-/tmp}/copilot-primer-test-gate"
mkdir -p "$state_root"

safe_session_id() {
  printf '%s' "$1" | tr -c '[:alnum:]_-' '_'
}

state_file_path() {
  printf '%s/%s.json' "$state_root" "$(safe_session_id "$1")"
}

save_state() {
  printf '{"decision":"%s"}\n' "$2" > "$(state_file_path "$1")"
}

clear_state() {
  state_file="$(state_file_path "$1")"
  if [ -f "$state_file" ]; then
    rm -f "$state_file"
  fi
}

read_state() {
  state_file="$(state_file_path "$1")"
  if [ -f "$state_file" ]; then
    cat "$state_file"
  fi
}

hook_input="$(cat)"
payload_json="$hook_input"

if command -v python >/dev/null 2>&1; then
  parsed_payload="$(HOOK_INPUT="$payload_json" python - <<'PY'
import json
import os

raw = os.environ.get("HOOK_INPUT", "")
try:
    payload = json.loads(raw)
except json.JSONDecodeError:
    print(json.dumps({"hookEventName": "", "sessionId": "default-session", "prompt": raw, "tool_name": "", "tool_input_strings": []}), end="")
else:
    tool_input_strings = []

    def walk(value):
        if value is None:
            return
        if isinstance(value, str):
            tool_input_strings.append(value)
            return
        if isinstance(value, dict):
            for nested in value.values():
                walk(nested)
            return
        if isinstance(value, (list, tuple)):
            for nested in value:
                walk(nested)
            return
        tool_input_strings.append(str(value))

    walk(payload.get("tool_input"))
    print(json.dumps({
        "hookEventName": payload.get("hookEventName", ""),
        "sessionId": payload.get("sessionId", "default-session"),
        "prompt": payload.get("prompt", raw),
        "tool_name": payload.get("tool_name", ""),
        "tool_input_strings": tool_input_strings,
    }), end="")
PY
)"
elif command -v python3 >/dev/null 2>&1; then
  parsed_payload="$(HOOK_INPUT="$payload_json" python3 - <<'PY'
import json
import os

raw = os.environ.get("HOOK_INPUT", "")
try:
    payload = json.loads(raw)
except json.JSONDecodeError:
    print(json.dumps({"hookEventName": "", "sessionId": "default-session", "prompt": raw, "tool_name": "", "tool_input_strings": []}), end="")
else:
    tool_input_strings = []

    def walk(value):
        if value is None:
            return
        if isinstance(value, str):
            tool_input_strings.append(value)
            return
        if isinstance(value, dict):
            for nested in value.values():
                walk(nested)
            return
        if isinstance(value, (list, tuple)):
            for nested in value:
                walk(nested)
            return
        tool_input_strings.append(str(value))

    walk(payload.get("tool_input"))
    print(json.dumps({
        "hookEventName": payload.get("hookEventName", ""),
        "sessionId": payload.get("sessionId", "default-session"),
        "prompt": payload.get("prompt", raw),
        "tool_name": payload.get("tool_name", ""),
        "tool_input_strings": tool_input_strings,
    }), end="")
PY
)"
else
  parsed_payload='{"hookEventName":"","sessionId":"default-session","prompt":"","tool_name":"","tool_input_strings":[]}'
fi

event_name="$(PARSED_PAYLOAD="$parsed_payload" python - <<'PY'
import json, os
payload = json.loads(os.environ["PARSED_PAYLOAD"])
print(payload.get("hookEventName", ""), end="")
PY
 2>/dev/null || python3 - <<'PY'
import json, os
payload = json.loads(os.environ["PARSED_PAYLOAD"])
print(payload.get("hookEventName", ""), end="")
PY
)"

session_id="$(PARSED_PAYLOAD="$parsed_payload" python - <<'PY'
import json, os
payload = json.loads(os.environ["PARSED_PAYLOAD"])
print(payload.get("sessionId", "default-session"), end="")
PY
 2>/dev/null || python3 - <<'PY'
import json, os
payload = json.loads(os.environ["PARSED_PAYLOAD"])
print(payload.get("sessionId", "default-session"), end="")
PY
)"

prompt_text="$(PARSED_PAYLOAD="$parsed_payload" python - <<'PY'
import json, os
payload = json.loads(os.environ["PARSED_PAYLOAD"])
print(payload.get("prompt", ""), end="")
PY
 2>/dev/null || python3 - <<'PY'
import json, os
payload = json.loads(os.environ["PARSED_PAYLOAD"])
print(payload.get("prompt", ""), end="")
PY
)"

tool_name="$(PARSED_PAYLOAD="$parsed_payload" python - <<'PY'
import json, os
payload = json.loads(os.environ["PARSED_PAYLOAD"])
print(payload.get("tool_name", ""), end="")
PY
 2>/dev/null || python3 - <<'PY'
import json, os
payload = json.loads(os.environ["PARSED_PAYLOAD"])
print(payload.get("tool_name", ""), end="")
PY
)"

tool_input_strings="$(PARSED_PAYLOAD="$parsed_payload" python - <<'PY'
import json, os
payload = json.loads(os.environ["PARSED_PAYLOAD"])
print("\n".join(payload.get("tool_input_strings", [])), end="")
PY
 2>/dev/null || python3 - <<'PY'
import json, os
payload = json.loads(os.environ["PARSED_PAYLOAD"])
print("\n".join(payload.get("tool_input_strings", [])), end="")
PY
)"

if [ "$event_name" = "UserPromptSubmit" ]; then
  case "$prompt_text" in
    *PROCEED*)
      save_state "$session_id" "PROCEED"
      ;;
    *MODIFY*|*SKIP*)
      save_state "$session_id" "HOLD"
      ;;
    *)
      clear_state "$session_id"
      ;;
  esac
  exit 0
fi

if [ "$event_name" != "PreToolUse" ]; then
  exit 0
fi

normalized_input="$(printf '%s\n%s' "$tool_name" "$tool_input_strings" | tr '[:upper:]' '[:lower:]')"

case "$(printf '%s' "$tool_name" | tr '[:upper:]' '[:lower:]')" in
  *edit*|*create*|*write*|*replace*)
    case "$normalized_input" in
      *python-app/tests/test_api.py*|*python-app/tests/*|*test_api.py*)
        state_json="$(read_state "$session_id")"
        case "$state_json" in
          *'"decision":"PROCEED"'*)
            clear_state "$session_id"
            exit 0
            ;;
          *)
            printf '%s\n' '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"Before editing tests, first summarize the planned test changes and wait for the user to reply with PROCEED, MODIFY, or SKIP.","additionalContext":"Test-file edits are gated. Summarize the intended test changes first. Only edit tests after the user replies with PROCEED in a follow-up prompt."}}'
            exit 0
            ;;
        esac
        ;;
      *)
        exit 0
        ;;
    esac
    ;;
  *)
    exit 0
    ;;
esac