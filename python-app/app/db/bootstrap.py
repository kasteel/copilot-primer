from __future__ import annotations

import sqlite3
from pathlib import Path

from app.db.connection import resolve_db_path

SCHEMA_SQL = """
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    segment TEXT NOT NULL,
    city TEXT NOT NULL,
    country TEXT NOT NULL,
    joined_at TEXT NOT NULL
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    active INTEGER NOT NULL
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    status TEXT NOT NULL,
    created_at TEXT NOT NULL,
    total_amount REAL NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers (id)
);

CREATE TABLE order_items (
    id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price REAL NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders (id),
    FOREIGN KEY (product_id) REFERENCES products (id)
);

CREATE TABLE support_tickets (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_id INTEGER,
    status TEXT NOT NULL,
    priority TEXT NOT NULL,
    subject TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers (id),
    FOREIGN KEY (order_id) REFERENCES orders (id)
);
"""

CUSTOMERS = [
    (1, "Northwind Traders", "enterprise", "Amsterdam", "Netherlands", "2023-01-11"),
    (2, "Blue Harbor Retail", "mid-market", "Rotterdam", "Netherlands", "2023-03-06"),
    (3, "Cedar & Stone", "small-business", "Utrecht", "Netherlands", "2023-06-18"),
    (4, "Granite Peak Outfitters", "enterprise", "Brussels", "Belgium", "2024-01-09"),
    (5, "Sunset Studio", "small-business", "Ghent", "Belgium", "2024-04-22"),
]

PRODUCTS = [
    (1, "Field Laptop", "hardware", 1499.0, 1),
    (2, "Warehouse Scanner", "hardware", 399.0, 1),
    (3, "Operations Dashboard", "software", 299.0, 1),
    (4, "Support Analytics", "software", 199.0, 1),
    (5, "Thermal Printer", "hardware", 249.0, 1),
    (6, "Inventory Beacon", "hardware", 129.0, 1),
]

ORDERS = [
    (1, 1, "fulfilled", "2025-01-10", 2197.0),
    (2, 2, "fulfilled", "2025-02-03", 997.0),
    (3, 1, "open", "2025-02-18", 598.0),
    (4, 3, "fulfilled", "2025-03-01", 1499.0),
    (5, 4, "open", "2025-03-22", 1188.0),
    (6, 5, "fulfilled", "2025-04-02", 528.0),
]

ORDER_ITEMS = [
    (1, 1, 1, 1, 1499.0),
    (2, 1, 3, 1, 299.0),
    (3, 1, 5, 1, 249.0),
    (4, 2, 2, 1, 399.0),
    (5, 2, 4, 3, 199.0),
    (6, 3, 3, 2, 299.0),
    (7, 4, 1, 1, 1499.0),
    (8, 5, 2, 2, 399.0),
    (9, 5, 6, 3, 129.0),
    (10, 6, 5, 1, 249.0),
    (11, 6, 6, 2, 129.0),
]

SUPPORT_TICKETS = [
    (1, 1, 1, "closed", "medium", "Printer setup question", "2025-01-15"),
    (2, 1, 3, "open", "high", "Dashboard sync delay", "2025-02-21"),
    (3, 2, 2, "closed", "low", "License clarification", "2025-02-10"),
    (4, 4, 5, "open", "high", "Scanner pairing issue", "2025-03-24"),
    (5, 5, 6, "open", "medium", "Beacon battery drain", "2025-04-05"),
    (6, 1, None, "open", "medium", "Quarterly renewal planning", "2025-04-11"),
]


def bootstrap_database(db_path: str | Path | None = None) -> Path:
    path = resolve_db_path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    if path.exists():
        path.unlink()

    connection = sqlite3.connect(path)
    try:
        connection.executescript(SCHEMA_SQL)
        connection.executemany(
            "INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?)", CUSTOMERS
        )
        connection.executemany(
            "INSERT INTO products VALUES (?, ?, ?, ?, ?)", PRODUCTS
        )
        connection.executemany(
            "INSERT INTO orders VALUES (?, ?, ?, ?, ?)", ORDERS
        )
        connection.executemany(
            "INSERT INTO order_items VALUES (?, ?, ?, ?, ?)", ORDER_ITEMS
        )
        connection.executemany(
            "INSERT INTO support_tickets VALUES (?, ?, ?, ?, ?, ?, ?)", SUPPORT_TICKETS
        )
        connection.commit()
    finally:
        connection.close()

    return path
