# SQLite Read-Only MCP Example

This example is intentionally small. It is meant to point a local MCP server at the SQLite database produced by `python-app/scripts/bootstrap_db.py`.

Recommended tool surface:

- `list-tables`
- `describe-table`
- `query-readonly`

Guardrails to keep:

- open the database in read-only mode
- reject non-SELECT queries
- reject multi-statement SQL
- limit rows returned
- sanitize errors before returning them
