from fastapi import APIRouter, Depends, Query

from app.dependencies import get_product_service
from app.models.dto import TopProduct
from app.services.product_service import ProductService

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/top", response_model=list[TopProduct])
def list_top_products(
    limit: int = Query(default=5, ge=1, le=20),
    service: ProductService = Depends(get_product_service),
) -> list[TopProduct]:
    return service.list_top_products(limit)
