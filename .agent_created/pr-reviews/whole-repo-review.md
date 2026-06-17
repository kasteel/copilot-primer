# Review: copilot-primer (whole repository)

**Date:** 2026-06-15
**Scope:** Full repo review (`/Users/fleur.petit/projects/copilot-primer`)
**Audience target:** developers who already have meaningful Copilot experience
**Lens:** clarity, factual correctness, generic security, **npm-worm aftermath**, **Alliander post-incident policy compliance**

---

## Verdict

❌ **Request changes** — primarily on **Alliander compliance** and **supply‑chain framing**. The didactic material itself is solid and largely accurate, but several artefacts will either be blocked from being pushed to GitHub under the current Alliander policy, or actively teach patterns (hooks/MCPs/skills) without the security warnings the post-incident context demands. Once those are addressed, this becomes a confident 🔶.

---

## Summary

- **Pedagogy:** Strong. Each chapter follows a consistent *What it's good for → Why senior devs should care → How to think about it → Failure modes* shape that suits experienced readers. Mental models like *Ask/Plan/Agent*, *instructions vs hooks (steer vs enforce)*, and *MCP usefulness grows with MCP restraint* are sharp.
- **Factual accuracy:** Mostly correct. Two real concerns: the **hook exit-code contract** described in chapter 5 is the Anthropic/Claude Code contract, not officially documented for GitHub Copilot's hook surface; and the **skills mechanism** is described in a way that blurs Copilot Code Review (GitHub-side, looks in `.github/skills/`) with the in-IDE skill loading path, leaving learners without a working filesystem location.
- **Missing artefacts:** Chapter 8 ships `mcp.json` and a README but no `server.py`. The MCP `mcp.json` references `python server.py` with no working directory — students get an immediate "where do I put this" wall.
- **Generic security:** The default `.vscode/settings.json` enables agent debug logging including file logging. Logs can contain prompts, file contents, and inadvertently secrets. Not flagged.
- **npm-worm / supply chain:** The course teaches *three* mechanisms that grant arbitrary local code execution from a repo (hooks, MCPs, skills) and *none* of the chapter READMEs warn against enabling them from untrusted repos. After Shai-Hulud, this is the single biggest gap.
- **Alliander compliance:** Multiple direct conflicts. The example hook configs and `.vscode/settings.json` are exactly the file classes Alliander now blocks from being pushed to GitHub. The course presupposes Copilot is available as an extension, which is currently disallowed on managed devices. There is no mention of Artifactory, `--frozen` lockfile installs, signed commits, or commit-hash-pinned actions.

---

## Findings

| Sev | File / Area | Issue | Suggestion |
|---|---|---|---|
| ❌ | [05-hooks/examples/ruff-hook.json](05-hooks/examples/ruff-hook.json), [05-hooks/examples/ruff-hook.sh](05-hooks/examples/ruff-hook.sh), [06-testing-with-copilot/example_test_hook_windows/test-generation-gate.json](06-testing-with-copilot/example_test_hook_windows/test-generation-gate.json), [06-testing-with-copilot/example_test_hook_windows/test-generation-gate.sh](06-testing-with-copilot/example_test_hook_windows/test-generation-gate.sh), [06-testing-with-copilot/example_test_hook_windows/test-generation-gate.ps1](06-testing-with-copilot/example_test_hook_windows/test-generation-gate.ps1) | Per Alliander post-incident FAQ, **AI-tool hook configs are blocked from being pushed to GitHub**. As shipped, this repo will fail those filters or — worse — the filters will be silently routed around because the files have neutral names. | Either (a) move hook material to a documentation-only form (`.md` snippets the reader copy-pastes locally), or (b) call out the policy explicitly and explain how to keep hooks out of the remote. |
| ❌ | Implicit `.vscode/settings.json` referenced in [README.md](README.md) | Alliander policy lists "VS Code settings files" as blocked from being pushed. Shipping a committed `.vscode/settings.json` (especially one that enables agent debug logging) directly conflicts. | Move settings to a `docs/recommended-settings.md` snippet, or gitignore `.vscode/` and instruct the reader to apply the settings locally. |
| ❌ | All chapters | The course assumes Copilot is installed and active in VS Code. On Alliander-managed devices today, VS Code is only allowed **without extensions** (fase 1, 10 jun 2026). The primer never acknowledges this gating. | Add a "Prerequisites & policy context" section to the top-level [README.md](README.md) that names the policy state assumed (fase 2+ with extension allow-listing) and warns participants who are on managed devices today. |
| ❌ | [05-hooks/README.md](05-hooks/README.md), [08-mcps/README.md](08-mcps/README.md), [04-skills/README.md](04-skills/README.md) | Hooks, MCP servers and skills all give a repository the ability to execute or steer code on the developer's machine the moment Copilot is active. After the npm worm, this is the same supply-chain shape that infected the company. No chapter warns the reader: "never enable a hook / MCP / skill that you did not write or audit." | Add a one-paragraph "Supply chain warning" to each of those three READMEs. Explicitly say: clone-and-trust is the threat model; treat repo-provided hook configs and MCP configs as untrusted by default. |
| ❌ | [python-app/pyproject.toml](python-app/pyproject.toml), [Justfile](Justfile) | `just setup` runs `uv sync --group dev` without `--frozen` and there is no `uv.lock` committed. Combined with no Artifactory configuration, this is exactly the install pattern Alliander now discourages: open PyPI, no lockfile pin, fresh version resolution on every run. | Commit `uv.lock`, change `just setup` to `uv sync --frozen --group dev`, and add a `docs/registry.md` showing the JFrog Artifactory `[[tool.uv.index]]` configuration. Document that participants on managed devices must use Artifactory. |
| 🔶 | [05-hooks/README.md](05-hooks/README.md) (the "exit code 0/2/other" section) | The exit-code contract (`0` = success, `2` = blocking, others = warning) is the **Claude Code** hook contract. GitHub Copilot's hook semantics are documented separately and have differed in places (e.g., JSON output with `permissionDecision: "deny"` for PreToolUse, which chapter 6 actually uses). Mixing the two without naming them will confuse experienced readers who try to reconcile this with the docs. | Either cite the Copilot hooks doc URL explicitly, or split into "the script-exit-code model" and "the JSON-output model" and note which Copilot version supports which. |
| 🔶 | [04-skills/README.md](04-skills/README.md), [04-skills/assignments.md](04-skills/assignments.md) | The skill loading mechanism is left implicit. The README mentions `.github/skills/` only in the context of Copilot **Code Review** on github.com, but Assignment 1 step 1 says "Place it in a folder where Copilot can use it" with no concrete path. Experienced devs will spend their first 20 minutes hunting for the right directory. | State the exact directories Copilot honors in-IDE for skills (and version, if relevant). If the in-IDE skills mechanism is still preview / unstable, say so. |
| 🔶 | [03-instructions/examples/python.test.instructions.md](03-instructions/examples/python.test.instructions.md) | The file sits in `03-instructions/examples/` rather than `.github/instructions/` or `.vscode/`. As shipped it is **not** actually scoped to `python-app/tests/**/*.py` for the running primer — it is a sample. The chapter does not say "copy this to `.github/instructions/`". A senior dev will assume it is live and be confused that nothing happens. | Add a one-liner in the chapter README clarifying that example files in `examples/` are templates the reader copies into the active discovery location. Name the active location. |
| 🔶 | [08-mcps/examples/sqlite-readonly/mcp.json](08-mcps/examples/sqlite-readonly/mcp.json), [08-mcps/examples/sqlite-readonly/README.md](08-mcps/examples/sqlite-readonly/README.md) | The MCP server `server.py` referenced in `mcp.json` is not shipped. The command is `python server.py` with no `cwd`, so VS Code will resolve it against the workspace root and the file won't be found. Also: `"command": "python"` not `python3` — on macOS without pyenv this often fails. The example silently expects the participant to write the server themselves, but doesn't say so. | Either ship a minimal `server.py` that demonstrates the read-only enforcement, or rename it `server-template.md` and make the "you write this" framing explicit. Use `python3`. Add `"cwd": "${workspaceFolder}/08-mcps/examples/sqlite-readonly"`. |
| 🔶 | [08-mcps/examples/sqlite-readonly/README.md](08-mcps/examples/sqlite-readonly/README.md) | Read-only enforcement is delegated to an env var (`SQLITE_READ_ONLY=true`) interpreted by user code that does not exist in the repo. The chapter teaches "the read-only story should not be based on trust" but the only artefact shipped *is* based on trust. | Show the SQLite read-only URI form (`file:...?mode=ro`) or `sqlite3.connect(..., uri=True, ...)` so participants see real enforcement, not a string they could ignore. |
| 🔶 | [06-testing-with-copilot/example_test_hook_windows/test-generation-gate.sh](06-testing-with-copilot/example_test_hook_windows/test-generation-gate.sh) | Falls back to `default-session` when `sessionId` is missing or JSON parsing fails (e.g., Python isn't on PATH). All parallel sessions would then **share approval state** — one `PROCEED` unlocks edits in a different session. Also: the `python` and `python3` fallback branches in the script silently emit empty payloads on parse failure, so a malformed input opens the gate. | Fail closed: if `sessionId` is empty or parsing failed, treat as "no decision" and deny. Don't fall back to a shared bucket. |
| 🔶 | [01-debugging-requests/README.md](01-debugging-requests/README.md) | External screenshots are referenced via `code.visualstudio.com/assets/docs/agents/chat-debug-view/...`. Link rot is likely on a 12+ month workshop horizon, and the Alliander web proxy may strip or block these. | Bundle a local `images/` folder per chapter; reference the local paths. |
| 🔶 | Repo-wide | No mention of **signed commits** (Alliander mandatory) and no contributor guidance on commit signing or GitHub Actions commit-SHA pinning. The repo has no `.github/workflows/`, so the action-pinning is currently a non-issue — but workshop participants commonly add one. | Add a short `CONTRIBUTING.md` covering signed commits and SHA-pinned actions, and reference the Alliander policy doc. |
| 🔶 | [Justfile](Justfile) (`just run` recipe) | `uvicorn --reload` exposes a dev server. There is no warning about binding only to localhost; default uvicorn binds to `127.0.0.1` so this is okay, but `app/main.py` enables `/health` returning the **absolute database path** (`resolve_db_path()`). That leaks host filesystem layout. | Either redact the path (`"database": "ok"`) or document that this endpoint is dev-only. |
| ℹ️ | [README.md](README.md) Course Order | Lists chapters but doesn't surface dependencies (e.g., chapter 5 hooks builds on chapter 3 instructions; chapter 6 needs chapter 3 and 5). | Add a one-line "depends on" tag per chapter for non-linear learners. |
| ℹ️ | [04-skills/assignments.md](04-skills/assignments.md) Assignment 2 | Asks the participant to "Create a new example skill ... that prints a joke / lists animals" and add a script. Combined with chapter 5 hooks, this gives a participant a frictionless path to a workflow that auto-executes a script in their session. Harmless for a joke; not harmless as a teaching reflex. | Add a one-liner: scripts triggered by Copilot are arbitrary code execution; only run scripts you authored. |
| ℹ️ | [03-instructions/assignments.md](03-instructions/assignments.md) | The "Variable names should refer to animals as much as possible" exercise is memorable but, as an instruction someone forgets to delete, can corrupt a real codebase. | Add an explicit "remove this before pushing" callout *with a git command to detect leftover instructions*. |
| ℹ️ | [python-app/app/main.py](python-app/app/main.py), [python-app/app/db/connection.py](python-app/app/db/connection.py) (inferred), repo-wide | Course makes no mention of secrets handling, DB-path injection from env, or auth. For a primer this is acceptable, but for the npm-worm context an "Out of scope" note would protect against participants assuming "Copilot-generated FastAPI" implies production-shaped guarantees. | One-line "Out of scope" footnote in [README.md](README.md) covering auth, secrets, transport security. |
| ℹ️ | [README.md](README.md) | Says the Justfile is Linux-shell only. macOS is implicit; Windows is "use WSL". After the cyber-incident, WSL re-install steps are non-trivial on managed devices. | Briefly link the Alliander WSL guidance or mark Windows as second-class. |

---

## 1. Clarity for experienced Copilot developers

**Where it works well**

- The consistent chapter shape (*What it's good for → Why senior devs should care → How to think about it → Failure modes*) is well-pitched. It treats the reader as someone who already knows how to chat with Copilot and need not be re-taught the basics.
- The conceptual contrasts are crisp: *Ask = read-only / Plan = propose / Agent = act*; *instructions bias, hooks constrain*; *MCP value lives in the boundary, not the surface*. These are the right framings for experienced readers.
- The 01-debugging chapter rightly leads with the debug view — anyone who has used Copilot at depth knows that's the difference between "it works" and "I can explain why it works."
- Assignment design is grown-up: prompts that ask you to compare, to record where activation broke, to compare instruction-only vs hook-enforced outcomes. That is the right register.

**Where it will frustrate experienced readers**

- **Concrete activation paths are missing.** Chapter 3's example sits in `03-instructions/examples/`, chapter 4 says "put it where Copilot can find it", chapter 5 ships a hook config without a target path, chapter 8 references a `server.py` that isn't there. A senior dev's first question on each chapter is "where exactly does this file live?" and the answer is too often "figure it out." See findings 🔶 for [03](03-instructions/examples/python.test.instructions.md), [04](04-skills/assignments.md), [08](08-mcps/examples/sqlite-readonly/mcp.json).
- **Tool-version reality is left implicit.** Skills in particular have different loading semantics depending on whether you are talking about in-IDE Copilot, Copilot Code Review on github.com, or third-party tools like Claude Code. The chapter conflates them.
- **No environment-validation step.** A senior dev wants `just doctor` or equivalent to confirm uv, just, Python, Copilot version, hook support, and MCP support are all present *before* the first assignment.
- **The Windows test-gate hook is 200+ lines of shell + Python shelling out to Python.** Anyone debugging it will reach for a rewrite within five minutes. A short Python-only script would be more honest and more useful as teaching material.

---

## 2. Factual correctness

**Things to verify or correct**

1. **Hook exit-code semantics** ([05-hooks/README.md](05-hooks/README.md)) — the "0 success / 2 blocking / other warning" trio is the Anthropic/Claude Code contract. GitHub Copilot's hook surface uses JSON output with `hookSpecificOutput.permissionDecision` (which chapter 6 already uses). Verify against the current Copilot docs and pick one canonical model per chapter.
2. **`agentDebugLog.fileLogging.enabled`** — chapter 1 implies enabling this turns on the debug *view*; in current builds the view setting and the file-logging setting are separate. The chapter mentions both in the intro, but the step list reads as if file logging is what opens the panel. Tighten.
3. **Skills loading directory** — chapter 4 says `.github/skills/` is honored by Copilot **code review**, then assignment 1 asks you to put a skill "where Copilot can find it" in the *in-IDE* flow. These are not the same surface; do not let the reader assume they are.
4. **MCP `mcp.json` shape** — `"type": "stdio"` and `"command"/"args"/"env"` are correct for VS Code's MCP configuration. ✅
5. **The Justfile `set shell := ["sh", "-cu"]`** is fine on macOS/Linux, but the README's claim that Windows needs WSL is correct only if the participant is also running `uv` and `python` via WSL — a mixed-host setup will silently break. Worth a sentence.
6. **`requires-python = ">=3.11"`** — fine, but the example MCP config invokes `python` not `python3`. On Apple Silicon stock macOS, `python` is often Python 3.9 or absent. Use `python3`.

No outright lies, but several of the above will cost a senior reader 15–30 minutes of "wait, that's not how this actually works."

---

## 3. Generic security risks

- **Debug logging captures prompts and file contents.** The `.vscode/settings.json` enables agent file logging by default. In a workshop repo this is fine; in a participant's day-job repo it could log secrets, customer data, or proprietary code into a JSONL on disk that they forget about. Warn explicitly.
- **`/health` leaks the absolute DB path.** Small, but unnecessary — recommend reducing to `{"status":"ok"}` and moving the path into a debug-only endpoint.
- **No input validation** is discussed for any of the example endpoints in `python-app/app/api/*`. Chapter 7 (recovery) demonstrates a service that removes `safe_limit = max(1, min(limit, 20))`. That's a great teaching moment about clamping; consider also calling out that *removing* such a clamp is the same class of bug that turns into DoS in production.
- **Hooks and MCPs are unsandboxed.** Both are arbitrary code execution from repo configuration. Treat as a security-relevant capability, not a productivity feature.
- **The test-generation-gate hook fails open** under JSON-parse failure and falls back to a shared `default-session` bucket. A gate that fails open is worse than no gate at all, because it implies safety that isn't there.

---

## 4. npm-worm-specific risks

The Shai-Hulud-style worm propagated through *three* surfaces: npm packages, infected repositories, and IDE marketplace extensions. The primer's three flagship capabilities — hooks, MCPs, skills — sit on exactly the second and third surfaces:

1. **Hooks (chapter 5)** — a hook config is a piece of YAML/JSON in a repo that tells Copilot to execute a local script. Clone a malicious repo, open in VS Code with Copilot active, do anything that triggers `SessionStart` or `PostToolUse`, and arbitrary code runs. The chapter does not say "review any repo's hook config before opening it." It should.
2. **MCP servers (chapter 8)** — an MCP config tells VS Code to spawn a long-lived local process. Even more direct code execution. The chapter does not warn against installing MCP servers from untrusted sources. It should.
3. **Skills (chapter 4)** — a SKILL.md can drag a script into Copilot's context with the intent that Copilot run it. Assignment 2 explicitly asks the student to build that pattern. Harmless content (jokes, animal names) is used, but the *muscle memory* it builds is "give Copilot a script and tell it to run it." That muscle memory is dangerous now.

In addition:

- The course never recommends `uv sync --frozen` and never mentions a committed `uv.lock`. Each `just setup` re-resolves dependencies against public PyPI. After Shai-Hulud, that is precisely the lifecycle moment Alliander wants pinned and routed through Artifactory.
- The course also never mentions `pip install --require-hashes`, `pnpm` cooldowns, or any other supply-chain mitigation. For a primer aimed at developers who are this week recovering from a real worm, that omission is loud.

**Highest-leverage fix:** add a single, prominent `docs/supply-chain.md` referenced from the top-level README that says, in order:
- never enable hooks, MCPs, or skills from a repo you did not write or audit
- pin and freeze your Python deps; use Artifactory; do not allow PyPI fallback
- if you see a `.vscode/`, `.github/hooks/`, `.github/skills/`, or `mcp.json` in a cloned repo, read it before letting Copilot touch the workspace

---

## 5. Compliance with Alliander guidelines

Mapping the two attached docs (recovery steps + GitHub FAQ for developers) against this repo:

| Alliander rule | Status in copilot-primer |
|---|---|
| VS Code allowed only without extensions (fase 1) | ❌ Entire primer assumes Copilot is active. Needs a "Prerequisites" disclaimer that this is fase 2+ material. |
| Forks of VS Code (Cursor, Kira) forbidden | ✅ No references to forks. |
| Other AI IDEs (Cursor, Neovim AI plugins) forbidden | ✅ Not promoted. |
| All packages via JFrog Artifactory | ❌ No mention. `uv sync` will hit public PyPI. |
| Prefer pnpm over npm; install --frozen-lockfile | N/A for npm (Python repo). Equivalent for uv is `uv sync --frozen`; not used. ❌ |
| Pin versions, no `latest` | 🔶 Version ranges in `pyproject.toml` use ceilings (`<1.0`) which is reasonable but no lockfile is committed. |
| Hash verification on installs | ❌ Not used. |
| Signed commits mandatory (SSH/GPG) | ❌ Not documented. |
| Commit-hash pinning for GitHub Actions | N/A (no workflows). 🔶 — preempt by saying so in the contributing guide. |
| Classic PATs blocked, fine-grained PATs need approval | N/A (no PATs in repo). ✅ |
| Self-hosted runners only | N/A (no workflows). |
| AI-tool hook configs blocked from being pushed to GitHub | ❌ [05-hooks/examples/ruff-hook.json](05-hooks/examples/ruff-hook.json) and [06-testing-with-copilot/example_test_hook_windows/test-generation-gate.json](06-testing-with-copilot/example_test_hook_windows/test-generation-gate.json) will hit that filter. |
| VS Code settings files blocked from being pushed | ❌ The repo's README documents shipping `.vscode/settings.json`. |
| Treat IDE extensions as supply-chain risk equal to packages | ❌ Not addressed. The premise of the primer is "install and configure Copilot, then add hooks/MCPs/skills" — none of those layers are framed as supply-chain risks. |

**Net:** the primer cannot be published or shared as a managed-Alliander-device-ready resource until the hook configs and VS Code settings are restructured to live outside the repo *or* the policy is explicitly relaxed.

---

## Per-file notes

- [README.md](README.md) — Good high-level overview. Add: prerequisites / policy context section; supply-chain warning; "Out of scope" note for security topics.
- [Justfile](Justfile) — Add `--frozen` to `uv sync`. Add a `just doctor` recipe that verifies versions. Document why `set shell := ["sh", "-cu"]` excludes native Windows.
- [01-debugging-requests/README.md](01-debugging-requests/README.md) — Tighten the wording around which setting opens the panel vs which writes the log file. Bundle screenshots locally.
- [01-debugging-requests/assignments.md](01-debugging-requests/assignments.md) — Good prompts. Consider adding one that asks the reader to *redact* a debug log and explain what they redacted, given the secret-leakage risk.
- [02-ask-agent-plan/README.md](02-ask-agent-plan/README.md) — Solid. Could add one line on Plan mode's *editable* nature being its main reviewability win.
- [02-ask-agent-plan/assignments.md](02-ask-agent-plan/assignments.md) — Good comparative design. ✅
- [03-instructions/README.md](03-instructions/README.md) — Solid on `applyTo`. Add explicit "where instruction files must live for in-IDE activation" callout.
- [03-instructions/examples/copilot-instructions.md](03-instructions/examples/copilot-instructions.md) — Concise. ✅
- [03-instructions/examples/python.test.instructions.md](03-instructions/examples/python.test.instructions.md) — Correct format, wrong location to be active. Call this out as template-only.
- [03-instructions/assignments.md](03-instructions/assignments.md) — The "animal variable names" exercise is fun but add a "remove before push" step with a concrete check.
- [04-skills/README.md](04-skills/README.md) — Good prose, weak on the load-path. Split Copilot Code Review behavior from in-IDE skill loading. Add supply-chain warning.
- [04-skills/assignments.md](04-skills/assignments.md) — Replace "place it in a folder where Copilot can use it" with the concrete path. In assignment 2 add the "only run scripts you authored" warning.
- [04-skills/examples/api-endpoint-skill/SKILL.md](04-skills/examples/api-endpoint-skill/SKILL.md) — Frontmatter and scope are correct and well-narrowed. ✅
- [05-hooks/README.md](05-hooks/README.md) — Clearly written; correct the exit-code contract attribution; add supply-chain warning.
- [05-hooks/assignments.md](05-hooks/assignments.md) — Good. ✅
- [05-hooks/examples/ruff-hook.json](05-hooks/examples/ruff-hook.json) — Works. Document the target path (`.vscode/hooks.json` vs `.github/hooks/`) and note the Alliander push restriction.
- [05-hooks/examples/ruff-hook.sh](05-hooks/examples/ruff-hook.sh) — Safe and minimal. ✅
- [06-testing-with-copilot/README.md](06-testing-with-copilot/README.md) — Clear judgment on Copilot's testing strengths/weaknesses. ✅
- [06-testing-with-copilot/assignments.md](06-testing-with-copilot/assignments.md) — Excellent experimental design (A: customization comparison; B: human gate).
- [06-testing-with-copilot/instructions/test-confirmation.instructions.md](06-testing-with-copilot/instructions/test-confirmation.instructions.md) — Clear and tight. ✅
- [06-testing-with-copilot/example_test_hook_windows/test-generation-gate.json](06-testing-with-copilot/example_test_hook_windows/test-generation-gate.json) — Fine shape. Same Alliander-push concern.
- [06-testing-with-copilot/example_test_hook_windows/test-generation-gate.sh](06-testing-with-copilot/example_test_hook_windows/test-generation-gate.sh) — Fail-open on parse failure and `default-session` fallback are real bugs; close them.
- [06-testing-with-copilot/example_test_hook_windows/test-generation-gate.ps1](06-testing-with-copilot/example_test_hook_windows/test-generation-gate.ps1) — Same fail-open concern (`default-session`).
- [07-error-recovery/README.md](07-error-recovery/README.md) — Lucid taxonomy of recovery failures. ✅
- [07-error-recovery/assignments.md](07-error-recovery/assignments.md) — Embedded patches are a nice didactic device. ✅
- [08-mcps/README.md](08-mcps/README.md) — Strong on philosophy. Weak on the missing artefact and supply-chain framing.
- [08-mcps/assignments.md](08-mcps/assignments.md) — Good challenge structure. Add "and verify the server source you connect to" as part of Assignment 1.
- [08-mcps/examples/sqlite-readonly/mcp.json](08-mcps/examples/sqlite-readonly/mcp.json) — Missing `cwd`, uses `python` not `python3`, references absent `server.py`.
- [08-mcps/examples/sqlite-readonly/README.md](08-mcps/examples/sqlite-readonly/README.md) — Lists the right guardrails; ships none of them. Either ship the server or relabel the file as a spec.

---

## Positive observations

- The course's central distinction — **bias vs constrain** (instructions vs hooks), **steer vs enforce** — is exactly the framing experienced devs need.
- Chapter 02's *Ask / Plan / Agent* mental model is a clean way to talk about risk profile per interaction.
- Chapter 06's two-mechanism approach (instruction + hook) for the test gate is a genuinely good worked example of "neither alone is enough."
- Chapter 07's insistence on "rerun the **same** validation after the repair" is the single most useful piece of advice in the whole primer for senior engineers leading less-experienced devs through Copilot.
- The `python-app` is small enough to be readable in one sitting and structured cleanly (api → service → repository) so the layering-violation assignments have teeth.

---

## Recommendations

**Must fix (before this can be shared as Alliander-compliant material)**

1. Remove or relocate the hook configs (`05-hooks/examples/*.json`, `06-testing-with-copilot/example_test_hook_windows/*.json/*.sh/*.ps1`) and any committed `.vscode/settings.json`. Either keep them as fenced code snippets inside Markdown that the reader pastes locally, or document the push-policy exception process.
2. Add a top-level "Supply-chain warnings" section referenced from chapters 4, 5, and 8. Be blunt: hooks/MCPs/skills are arbitrary code execution from repo state.
3. Add a "Prerequisites & Alliander policy state" section to [README.md](README.md) clarifying that the primer assumes a fase where extensions (Copilot specifically) are allow-listed.
4. Commit a `uv.lock`, change `just setup` to use `--frozen`, and add `docs/registry.md` showing the Artifactory config.

**Should fix**

5. Ship a working `08-mcps/examples/sqlite-readonly/server.py` that enforces read-only via the SQLite URI (`mode=ro`), not via an env-var-driven check. Set `cwd` in `mcp.json`.
6. Close the fail-open paths in `test-generation-gate.sh`/`.ps1`: deny when `sessionId` is empty or JSON parsing fails; never fall back to a shared bucket.
7. Reconcile the hook exit-code description in chapter 5 with the JSON-output model chapter 6 uses; cite the Copilot hook docs explicitly.
8. State the concrete in-IDE skill-loading directory in chapter 4, or mark the in-IDE skill mechanism as preview.
9. Bundle chapter 1's screenshots locally to survive link rot and proxy filters.

**Consider later**

10. Add a `just doctor` recipe that verifies `uv`, `just`, `python3`, and prints the Copilot extension version if installed.
11. Add a `CONTRIBUTING.md` covering signed commits and SHA-pinned actions.
12. Tighten `/health` so it does not leak the absolute DB path.
13. Add a one-liner "depends on" tag per chapter README to clarify the order for non-linear readers.

---

## Suggested PR title

`docs(security): align primer with post-incident supply-chain and Alliander policy`
