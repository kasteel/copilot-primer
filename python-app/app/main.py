from fastapi import FastAPI

from app.api.customers import router as customers_router
from app.api.orders import router as orders_router
from app.api.products import router as products_router
from app.db.connection import resolve_db_path


def create_app() -> FastAPI:
    app = FastAPI(title="Copilot Primer API", version="0.1.0")

    @app.get("/health", tags=["system"])
    def health() -> dict[str, str]:
        return {"status": "ok", "database": "configured" if resolve_db_path() else "missing"}

    app.include_router(customers_router)
    app.include_router(orders_router)
    app.include_router(products_router)
    return app


app = create_app()
