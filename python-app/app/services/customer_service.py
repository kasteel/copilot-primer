from __future__ import annotations

from app.models.dto import CustomerRead, CustomerSummary
from app.repositories.customer_repository import CustomerRepository


class CustomerService:
    def __init__(self, repository: CustomerRepository) -> None:
        self.repository = repository

    def list_customers(self) -> list[CustomerRead]:
        return [CustomerRead.model_validate(row) for row in self.repository.list_customers()]

    def get_customer_summary(self, customer_id: int) -> CustomerSummary | None:
        row = self.repository.get_customer_summary(customer_id)
        if row is None:
            return None
        return CustomerSummary.model_validate(row)
