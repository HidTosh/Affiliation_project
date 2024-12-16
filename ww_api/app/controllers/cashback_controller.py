from app.schemas.product import ProductCreate, ProductUpdate, ProductBase as Product
from app.schemas.product import ProductInResponse
from app.schemas.order_by import OrderByCase
from operator import attrgetter
from fastapi import HTTPException
import json
from json import JSONDecodeError
from collections import defaultdict
import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_cashback(user_id: int = None) -> dict:
    if user_id != None: 
        for cashbak in __calculate_total_purchase(get_purchase_list()):
            if cashbak["user_id"] == user_id:
                return cashbak
        return {}
    else:
        return __calculate_total_purchase(get_purchase_list())

def get_purchase_list():
    base_url = os.getenv("BASE_URL")
    try:
        response = requests.get(f"{base_url}/list_purchase")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Erreur : {response.status_code} - {response.text}")
    except Exception as e:
        print(f"error : {e}")

def __calculate_total_purchase(data) -> float:
    users_balance: list = []
    grouped_purchase = __group_purchase_by_user(data)
    for user_id in grouped_purchase:  
        pruchase_total_price: float = 0
        for el in grouped_purchase[user_id]: 
            pruchase_total_price += int(el["price"])
        users_balance.append({"user_id": user_id, "balance": pruchase_total_price * 0.10})

    return users_balance


def __group_purchase_by_user(all_purchase): 
    grouped_purchase_by_user = defaultdict(list)
    for purchase in all_purchase["items"]:
        grouped_purchase_by_user[purchase["user_id"]].append(purchase)

    return grouped_purchase_by_user