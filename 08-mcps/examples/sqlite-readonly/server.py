#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["mcp>=1.2"]
# ///
"""Read-only SQLite MCP server for the Copilot primer.

The read-only guarantee is enforced by:
- opening the database with the `mode=ro` URI form (the OS-level handle cannot write)
- rejecting multi-statement SQL
- rejecting anything that does not start with SELECT or WITH
- capping the row count returned to the caller
"""

from __future__ import annotations

import os
import re
import sqlite3
from pathlib import Path

from mcp.server.fastmcp import FastMCP

DEFAULT_DB_PATH = (
    Path(__file__).resolve().parents[3] / "python-app" / "data" / "app.db"
)
MAX_ROWS_CEILING = 500

mcp = FastMCP("primer-sqlite-readonly")


def _db_path() -> Path:
    return Path(os.getenv("SQLITE_DB_PATH", str(DEFAULT_DB_PATH)))


def _row_cap() -> int:
    raw = os.getenv("SQLITE_MAX_ROWS", "100")
    try:
        value = int(raw)
    except ValueError:
        value = 100
    return max(1, min(value, MAX_ROWS_CEILING))


def _connect() -> sqlite3.Connection:
    path = _db_path()
    if not path.exists():
        raise FileNotFoundError(
            f"SQLite database not found at {path}. Run `just bootstrap` first."
        )
    uri = f"file:{path}?mode=ro"
    connection = sqlite3.connect(uri, uri=True)
    connection.row_factory = sqlite3.Row
    return connection


_IDENT_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def _validate_identifier(name: str) -> str:
    if not _IDENT_RE.match(name):
        raise ValueError(f"Invalid identifier: {name!r}")
    return name


def _validate_select(sql: str) -> str:
    stripped = sql.strip().rstrip(";").strip()
    if not stripped:
        raise ValueError("Empty query.")
    if ";" in stripped:
        raise ValueError("Multi-statement SQL is not allowed.")
    leading = stripped.split(None, 1)[0].upper()
    if leading not in {"SELECT", "WITH"}:
        raise ValueError("Only SELECT or WITH queries are allowed.")
    return stripped


@mcp.tool()
def list_tables() -> list[str]:
    """List user tables in the database."""
    with _connect() as connection:
        cursor = connection.execute(
            "SELECT name FROM sqlite_master "
            "WHERE type = 'table' AND name NOT LIKE 'sqlite_%' "
            "ORDER BY name"
        )
        return [row["name"] for row in cursor.fetchall()]


@mcp.tool()
def describe_table(table: str) -> list[dict]:
    """Return the column schema for one table."""
    name = _validate_identifier(table)
    with _connect() as connection:
        cursor = connection.execute(f"PRAGMA table_info({name})")
        return [dict(row) for row in cursor.fetchall()]


@mcp.tool()
def query_readonly(sql: str, limit: int | None = None) -> dict:
    """Run a single SELECT or WITH query and return rows.

    The query is capped at SQLITE_MAX_ROWS (or the supplied limit, whichever is
    smaller). Multi-statement SQL and non-SELECT statements are rejected.
    """
    validated = _validate_select(sql)
    cap = _row_cap()
    effective_limit = cap if limit is None else max(1, min(limit, cap))
    with _connect() as connection:
        cursor = connection.execute(validated)
        rows = cursor.fetchmany(effective_limit + 1)
        truncated = len(rows) > effective_limit
        kept = rows[:effective_limit]
        return {
            "rows": [dict(row) for row in kept],
            "row_count": len(kept),
            "truncated": truncated,
            "row_limit": effective_limit,
        }


if __name__ == "__main__":
    mcp.run()
