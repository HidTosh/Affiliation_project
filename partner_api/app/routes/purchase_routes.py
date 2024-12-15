from fastapi import APIRouter, Query
from app.controllers.purchase_controller import (
    create_purchase,
    get_list_purchase
    )
from app.schemas.PaginationResponse import PaginatedResponse

router = APIRouter()

@router.get("/purchase", status_code=201)
def purchase(product_id: int, user_id: int):
    return create_purchase(product_id, user_id)

@router.get("/list_purchase", response_model=PaginatedResponse)
def list_purchase(page: int = Query(1, ge=1), size: int = Query(10, ge=1, le=100)):
    list_purchase = get_list_purchase()
    print(len(list_purchase))
    start = (page - 1) * size
    end = start + size
    paginated_list_purchase = list_purchase[start:end]
    return {
        "total": len(list_purchase),
        "page": page,
        "size": size,
        "items": paginated_list_purchase,
    }
