# Assignments

## Assignment 1: Connect A Read-Only SQLite MCP

Goal: expose the shared application data safely.

Tasks:

1. Bootstrap the application database.
2. Configure a local MCP server that points at the same SQLite file.
3. Expose read-only tools such as `list-tables`, `describe-table`, and `query-readonly`.
4. Verify the tools appear in Copilot.

## Assignment 2: Prove The Guardrails

Goal: show that the MCP is useful but constrained.

Tasks:

1. Run a safe query against customers, orders, or support tickets.
2. Attempt a suspicious or destructive query pattern.
3. Verify that the MCP blocks it.
4. Document which guardrail stopped the request.

Expected observations:

- The same shared data becomes useful for exploration.
- Guardrails are part of the design, not an afterthought.
