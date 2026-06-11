from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import get_customer_service
from app.models.dto import CustomerRead, CustomerSummary
from app.services.customer_service import CustomerService

router = APIRouter(prefix="/customers", tags=["customers"])


@router.get("", response_model=list[CustomerRead])
def list_customers(service: CustomerService = Depends(get_customer_service)) -> list[CustomerRead]:
    return service.list_customers()


@router.get("/{customer_id}/summary", response_model=CustomerSummary)
def get_customer_summary(
    customer_id: int,
    service: CustomerService = Depends(get_customer_service),
) -> CustomerSummary:
    summary = service.get_customer_summary(customer_id)
    if summary is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return summary
