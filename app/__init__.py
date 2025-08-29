# app/__init__.py
from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI(title="Scholar Search API")

    # Импортируем маршруты
    from app.api.routes import router as api_router
    app.include_router(api_router, prefix="/api")

    return app
