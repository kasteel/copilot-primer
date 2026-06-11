from __future__ import annotations

from pathlib import Path

from app.db.connection import open_connection


class OrderRepository:
    def __init__(self, db_path: str | Path) -> None:
        self.db_path = db_path

    def list_recent_orders(self, limit: int) -> list[dict[str, object]]:
        query = """
        SELECT
            o.id,
            c.name AS customer_name,
            o.status,
            o.created_at,
            o.total_amount
        FROM orders o
        INNER JOIN customers c ON c.id = o.customer_id
        ORDER BY o.created_at DESC
        LIMIT ?
        """
        with open_connection(self.db_path) as connection:
            rows = connection.execute(query, (limit,)).fetchall()
        return [dict(row) for row in rows]
