# SQLite Read-Only MCP Example

A complete, runnable read-only MCP server pointed at the SQLite database produced by `python-app/scripts/bootstrap_db.py`.

## Files

- [server.py](server.py) — the MCP server. Self-contained `uv run --script` (PEP 723) module; no install step needed.
- [mcp.json](mcp.json) — server entry to paste into your workspace `.vscode/mcp.json`.

## Tool surface

- `list_tables`
- `describe_table`
- `query_readonly`

## Guardrails

- **OS-level read-only:** the database is opened with the `file:...?mode=ro` URI form, so the SQLite handle cannot mutate the file regardless of what SQL is submitted.
- **Single-statement only:** semicolons inside the submitted SQL are rejected.
- **SELECT or WITH only:** any other leading keyword (`INSERT`, `UPDATE`, `DELETE`, `PRAGMA`, `ATTACH`, …) is rejected.
- **Row cap:** `SQLITE_MAX_ROWS` (default `100`, hard ceiling `500`) limits the rows returned. The response includes a `truncated` flag so the caller knows when more rows exist.
- **Identifier validation:** `describe_table` only accepts SQL identifiers (letters, digits, underscore; first character non-numeric).

## Run it

1. Bootstrap the SQLite database: `just bootstrap`.
2. Copy the entry from [mcp.json](mcp.json) into your workspace `.vscode/mcp.json` (or create that file with the same content).
3. Reload the MCP server list in VS Code (Command Palette → `MCP: List Servers`).
4. Confirm that `list_tables`, `describe_table`, and `query_readonly` appear under `primer-sqlite-readonly`.

## Verify the guardrails

Try these against the server and confirm each is rejected with a clear error:

- `query_readonly("DELETE FROM customers")`
- `query_readonly("SELECT 1; SELECT 2;")`
- `query_readonly("PRAGMA writable_schema = 1")`
- `describe_table("customers; DROP TABLE orders")`
