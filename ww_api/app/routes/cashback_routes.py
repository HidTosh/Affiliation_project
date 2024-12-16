from fastapi import APIRouter
from app.schemas.order_by import OrderByCase
from app.controllers.cashback_controller import get_cashback

router = APIRouter()

@router.get("/cashback")
def get_cashback_process(user_id: int):
    
    return get_cashback(user_id)