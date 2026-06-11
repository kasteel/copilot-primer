from pathlib import Path

from fastapi.testclient import TestClient

from app.db.bootstrap import bootstrap_database
from app.main import create_app


def build_client(tmp_path: Path) -> TestClient:
    db_path = tmp_path / "test.db"
    bootstrap_database(db_path)

    import os

    os.environ["COPILOT_PRIMER_DB_PATH"] = str(db_path)
    return TestClient(create_app())


def test_health(tmp_path: Path) -> None:
    client = build_client(tmp_path)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_list_customers(tmp_path: Path) -> None:
    client = build_client(tmp_path)

    response = client.get("/customers")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 5
    assert data[0]["name"] == "Blue Harbor Retail"


def test_customer_summary(tmp_path: Path) -> None:
    client = build_client(tmp_path)

    response = client.get("/customers/1/summary")

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Northwind Traders"
    assert data["total_orders"] == 2
    assert data["open_tickets"] >= 1


def test_recent_orders_limit(tmp_path: Path) -> None:
    client = build_client(tmp_path)

    response = client.get("/orders/recent", params={"limit": 3})

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3
    assert data[0]["id"] == 6


def test_top_products(tmp_path: Path) -> None:
    client = build_client(tmp_path)

    response = client.get("/products/top", params={"limit": 2})

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["units_sold"] >= data[1]["units_sold"]
