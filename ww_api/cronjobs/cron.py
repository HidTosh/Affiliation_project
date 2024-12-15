from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from datetime import datetime
import requests
import schedule
import threading
import time
from collections import defaultdict

BASE_URL = "http://127.0.0.1:9000" # TODO: move into env file

def get_list_purchase():
    print(f"Task start at {datetime.now()}")
    try:
        response = requests.get(f"{BASE_URL}/list_purchase")
        if response.status_code == 200:
            process_cashback(response.json())
        else:
            print(f"Erreur : {response.status_code} - {response.text}")
    except Exception as e:
        print(f"error : {e}")


def cron_job_get_purchase():
    """Start cron job"""
    schedule.every(10).minutes.do(get_list_purchase)
    while True:
        schedule.run_pending()
        time.sleep(1)

thread = threading.Thread(target=cron_job_get_purchase, daemon=True)
thread.start()

def process_cashback(data_purchase: dict):
    """Credit the cashback to the corresponding user"""
    users_balance = __calculate_total_purchase(data_purchase)
    #TODO: send cashback to user
    return True


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