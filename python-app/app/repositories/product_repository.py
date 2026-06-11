from __future__ import annotations

from pathlib import Path

from app.db.connection import open_connection


class ProductRepository:
    def __init__(self, db_path: str | Path) -> None:
        self.db_path = db_path

    def list_top_products(self, limit: int) -> list[dict[str, object]]:
        query = """
        SELECT
            p.id,
            p.name,
            p.category,
            SUM(oi.quantity) AS units_sold,
            SUM(oi.quantity * oi.unit_price) AS revenue
        FROM order_items oi
        INNER JOIN products p ON p.id = oi.product_id
        GROUP BY p.id, p.name, p.category
        ORDER BY units_sold DESC, revenue DESC
        LIMIT ?
        """
        with open_connection(self.db_path) as connection:
            rows = connection.execute(query, (limit,)).fetchall()
        return [dict(row) for row in rows]
