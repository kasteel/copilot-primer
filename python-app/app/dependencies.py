from app.db.connection import resolve_db_path
from app.repositories.customer_repository import CustomerRepository
from app.repositories.order_repository import OrderRepository
from app.repositories.product_repository import ProductRepository
from app.services.customer_service import CustomerService
from app.services.order_service import OrderService
from app.services.product_service import ProductService


def get_customer_service() -> CustomerService:
    return CustomerService(CustomerRepository(resolve_db_path()))


def get_order_service() -> OrderService:
    return OrderService(OrderRepository(resolve_db_path()))


def get_product_service() -> ProductService:
    return ProductService(ProductRepository(resolve_db_path()))
