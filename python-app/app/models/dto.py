from pydantic import BaseModel


class CustomerRead(BaseModel):
    id: int
    name: str
    segment: str
    city: str
    country: str


class CustomerSummary(BaseModel):
    id: int
    name: str
    segment: str
    city: str
    country: str
    total_orders: int
    total_revenue: float
    open_tickets: int


class RecentOrder(BaseModel):
    id: int
    customer_name: str
    status: str
    created_at: str
    total_amount: float


class TopProduct(BaseModel):
    id: int
    name: str
    category: str
    units_sold: int
    revenue: float
