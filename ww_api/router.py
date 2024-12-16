from fastapi import APIRouter, HTTPException
from app.routes.products_routes import router as products_router
from app.routes.cashback_routes import router as cashback_router
router = APIRouter()

router.include_router(products_router)
router.include_router(cashback_router)