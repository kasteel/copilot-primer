from __future__ import annotations

from pathlib import Path

from app.db.connection import open_connection


class CustomerRepository:
    def __init__(self, db_path: str | Path) -> None:
        self.db_path = db_path

    def list_customers(self) -> list[dict[str, object]]:
        query = """
        SELECT id, name, segment, city, country
        FROM customers
        ORDER BY name
        """
        with open_connection(self.db_path) as connection:
            rows = connection.execute(query).fetchall()
        return [dict(row) for row in rows]

    def get_customer_summary(self, customer_id: int) -> dict[str, object] | None:
        query = """
        SELECT
            c.id,
            c.name,
            c.segment,
            c.city,
            c.country,
            COUNT(DISTINCT o.id) AS total_orders,
            COALESCE(SUM(o.total_amount), 0) AS total_revenue,
            SUM(CASE WHEN st.status = 'open' THEN 1 ELSE 0 END) AS open_tickets
        FROM customers c
        LEFT JOIN orders o ON o.customer_id = c.id
        LEFT JOIN support_tickets st ON st.customer_id = c.id
        WHERE c.id = ?
        GROUP BY c.id, c.name, c.segment, c.city, c.country
        """
        with open_connection(self.db_path) as connection:
            row = connection.execute(query, (customer_id,)).fetchone()
        return dict(row) if row else None
