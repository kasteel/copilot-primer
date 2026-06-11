from __future__ import annotations

from app.models.dto import RecentOrder
from app.repositories.order_repository import OrderRepository


class OrderService:
    def __init__(self, repository: OrderRepository) -> None:
        self.repository = repository

    def list_recent_orders(self, limit: int = 5) -> list[RecentOrder]:
        safe_limit = max(1, min(limit, 20))
        return [RecentOrder.model_validate(row) for row in self.repository.list_recent_orders(safe_limit)]
