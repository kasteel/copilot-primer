# Assignments

> **Working in pairs.** Each assignment is designed for a pair. You do not need to write down every observation. Discuss with your partner and capture **2–3 take-aways** per assignment that you would share with the rest of the team.

## Assignment 1: Connect A Read-Only SQLite MCP

Goal: expose real application data through a deliberately narrow interface.

Tasks:

1. Bootstrap the application database with `just bootstrap`.
2. Install the example server: copy the `servers` entry from [examples/sqlite-readonly/mcp.json](examples/sqlite-readonly/mcp.json) into your workspace `.vscode/mcp.json`. The server script lives at [examples/sqlite-readonly/server.py](examples/sqlite-readonly/server.py) and runs via `uv run --script` (no install step).
3. Reload the MCP server list in VS Code and verify that `list_tables`, `describe_table`, and `query_readonly` appear in Copilot.
4. Read [examples/sqlite-readonly/server.py](examples/sqlite-readonly/server.py) end-to-end before trusting it. **Treat every MCP server as untrusted until you've read it.**
5. Explain why each exposed tool deserves to exist.

Discuss with your pair and capture **2–3 take-aways**. Useful prompts:

- what use case each tool supports
- what capability you intentionally did not expose
- why the interface is safer than a general database shell

Expected outcome:

- You should end with an MCP design that is visibly constrained, not merely labeled read-only.

## Assignment 2: Prove The Guardrails

Goal: show that the MCP is useful precisely because its boundaries are real.

Tasks:

1. Run one safe query against customers, orders, or support tickets.
2. Attempt suspicious or destructive query patterns. Try at least:
   - `query_readonly("DELETE FROM customers")`
   - `query_readonly("SELECT 1; SELECT 2;")`
   - `query_readonly("PRAGMA writable_schema = 1")`
   - `describe_table("customers; DROP TABLE orders")`
3. Verify that the MCP blocks each one.
4. Document which guardrail caused the block (OS-level `mode=ro`, single-statement check, SELECT/WITH check, or identifier validation).
5. Explain whether the protection came from tool design, input validation, or both.

Expected insight:

- Guardrails are part of the product design, not cleanup after the fact.
