from app.schemas.product import ProductCreate, ProductUpdate, ProductBase as Product
from app.schemas.product import ProductInResponse
from app.schemas.order_by import OrderByCase
from operator import attrgetter
from fastapi import HTTPException
import json
from json import JSONDecodeError

file_path = "data.json"

def get_all_products(order_by: str, reverse_order: bool) -> list[Product]:
    if order_by not in ["name", "description", "price"]:
        raise HTTPException(status_code=400, detail="Please indicate correct sort order")
    
    return sorted(__get_all_data(), key=lambda x: x[order_by], reverse=reverse_order)


def create_product(product: ProductCreate) -> str:
    list_products: list[Product | None] = __get_all_data()
    if len(list_products) > 0: product.id = max(list_products, key=lambda x:x["id"])["id"] + 1
    else: product.id = 1
    list_products.append(product.dict())
    __update_file(list_products)
    
    return "success"

def update_product(product_id: int, product_update: ProductUpdate) -> str:
    list_products: list[Product | None] = __get_all_data()
    for product in list_products:
        if product["id"] == product_id:
            product["name"] = product_update.name
            product["description"] = product_update.description
            product["thumbnail_url"] = product_update.thumbnail_url
            product["base_url"] = product_update.base_url
            product["price"] = product_update.price
    __update_file(list_products)

    return "success"

def delete_product(product_id: int) -> str:
    list_products: list[Product | None] = __get_all_data()
    for idx in range(len(list_products)):
        if list_products[idx]["id"] == product_id:
            list_products.pop(idx)
            __update_file(list_products)
            
            return "success"
    return "error"   

def archive_product(product_id: int) -> str:
    list_products: list[Product] = __get_all_data()
    for product in list_products:
        if product["id"] == product_id:
            product["archived"] = True
            __update_file(list_products)

            return "success"
    return "error"

def __get_all_data():
    with open(file_path, "r") as products_data_file:    
        try:
            return json.load(products_data_file)
        except JSONDecodeError:
            return []
        
def __update_file(list_products):
    with open(file_path, "w") as file:
        json.dump(list_products, file, indent=4)
    