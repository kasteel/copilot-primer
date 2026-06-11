from __future__ import annotations

import os
import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DEFAULT_DB_PATH = BASE_DIR / "data" / "app.db"
ENV_DB_PATH = "COPILOT_PRIMER_DB_PATH"


def resolve_db_path(db_path: str | Path | None = None) -> Path:
    if db_path is not None:
        return Path(db_path)

    env_value = os.getenv(ENV_DB_PATH)
    if env_value:
        return Path(env_value)

    return DEFAULT_DB_PATH


@contextmanager
def open_connection(db_path: str | Path | None = None) -> Iterator[sqlite3.Connection]:
    path = resolve_db_path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    try:
        yield connection
    finally:
        connection.close()
