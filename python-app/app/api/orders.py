from fastapi import APIRouter, Depends, Query

from app.dependencies import get_order_service
from app.models.dto import RecentOrder
from app.services.order_service import OrderService

router = APIRouter(prefix="/orders", tags=["orders"])


@router.get("/recent", response_model=list[RecentOrder])
def list_recent_orders(
    limit: int = Query(default=5, ge=1, le=20),
    service: OrderService = Depends(get_order_service),
) -> list[RecentOrder]:
    return service.list_recent_orders(limit)
