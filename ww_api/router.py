from fastapi import APIRouter, HTTPException
from app.routes.products_routes import router as products_router
router = APIRouter()

router.include_router(products_router)