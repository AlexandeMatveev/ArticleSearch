# app/api/__init__.py
from fastapi import APIRouter

router = APIRouter()

# Подключаем все роуты
from app.api.routes import router as routes_router
router.include_router(routes_router)