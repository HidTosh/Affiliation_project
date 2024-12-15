import requests
from fastapi import HTTPException
import json
from json import JSONDecodeError
import time

#BASE_URL = "http://127.0.0.1:8000"
BASE_URL = "http://ww_api:8000"
file_path = "list_purchase.json"

def create_purchase(product_id: int, user_id: int):
    for product in __get_all_products():
        if ((product["id"] == product_id) & (product["archived"] == False)) :
            list_purchase = __get_all_purchase()
            list_purchase.append(
                {
                    "product_id":product["id"], 
                    "name":product["id"],
                    "price": product["price"],
                    "user_id": user_id,
                    "ts": time.time()
                }
            )
            __create_purchase(list_purchase)       
            return {"message": "Created successfully", "purchase": product["id"]}

    return {"message": "purchase error"}


def get_list_purchase():
    return __get_all_purchase()

def __get_all_products():
    response = requests.get(f"{BASE_URL}/products")
    if response.status_code == 200:
        return response.json()
    else:
        return []
        print("Erreur :", response.status_code, response.text)

def __get_all_purchase():
    with open(file_path, "r") as purchase_list:    
        try:
            return json.load(purchase_list)
        except JSONDecodeError:
            return []
        
def __create_purchase(purchase_list):
    with open(file_path, "w") as file:
        json.dump(purchase_list, file, indent=4)