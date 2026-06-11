from __future__ import annotations

from app.models.dto import TopProduct
from app.repositories.product_repository import ProductRepository


class ProductService:
    def __init__(self, repository: ProductRepository) -> None:
        self.repository = repository

    def list_top_products(self, limit: int = 5) -> list[TopProduct]:
        safe_limit = max(1, min(limit, 20))
        return [TopProduct.model_validate(row) for row in self.repository.list_top_products(safe_limit)]
