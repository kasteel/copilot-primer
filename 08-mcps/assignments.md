# Assignments

## Assignment 1: Connect A Read-Only SQLite MCP

Goal: expose real application data through a deliberately narrow interface.

Tasks:

1. Bootstrap the application database.
2. Configure a local MCP server that points at the same SQLite file.
3. Expose only a small set of read-only tools, such as:
   - `list-tables`
   - `describe-table`
   - `query-readonly`
4. Verify that the tools appear in Copilot.
5. Explain why each exposed tool deserves to exist.

Write down:

- what use case each tool supports
- what capability you intentionally did not expose
- why the interface is safer than a general database shell

Expected outcome:

- You should end with an MCP design that is visibly constrained, not merely labeled read-only.

## Assignment 2: Prove The Guardrails

Goal: show that the MCP is useful precisely because its boundaries are real.

Tasks:

1. Run one safe query against customers, orders, or support tickets.
2. Attempt a suspicious or destructive query pattern.
3. Verify that the MCP blocks it.
4. Document which guardrail caused the block.
5. Explain whether the protection came from tool design, input validation, or both.

Expected insight:

- Guardrails are part of the product design, not cleanup after the fact.
