from fastapi import APIRouter
from app.schemas.order_by import OrderByCase
from typing import List
from app.schemas.product import (
    ProductBase as Product, 
    ProductCreate, 
    ProductUpdate
    )
from app.controllers.product_controller import (
    get_all_products,
    create_product,
    update_product,
    delete_product,
    archive_product
    )

router = APIRouter()

@router.get("/products", response_model=List[Product])
@router.get("/", response_model=List[Product])
def list_products(order_by: OrderByCase = "name", reverse_order: bool = False):
    """list all available products in a particular order and change the display order"""
    return get_all_products(order_by, reverse_order)

@router.post("/product", response_model=str)
def add_product(product: ProductCreate):
    """Add new product"""
    return create_product(product)

#
@router.put("/product/{product_id}", response_model=str)
def edit_product(product_id: int, product_update: ProductUpdate):
    """Update existing product"""
    return update_product(product_id, product_update)

#
@router.delete("/product/{product_id}")
def delete(product_id: int):
    """Delete product"""
    return delete_product(product_id)

#
@router.put("/product/archive/{product_id}", response_model=str)
def disable_product(product_id: int):
    """Update status of archive product"""
    return archive_product(product_id)