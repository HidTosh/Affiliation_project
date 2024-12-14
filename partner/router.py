from fastapi import APIRouter, HTTPException
from app.routes.purchase_routes import router as purchase_router
router = APIRouter()

router.include_router(purchase_router)