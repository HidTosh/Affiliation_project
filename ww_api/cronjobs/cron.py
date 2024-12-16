from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from datetime import datetime
import schedule
import threading
import time
from collections import defaultdict
from app.controllers.cashback_controller import get_cashback

def process_cashback():
    """Credit the cashback to the corresponding user"""
    print(f"Task start at {datetime.now()}")
    users_balance = get_cashback()
    #TODO: send cashback to user
    return True

def cron_job_get_purchase():
    """Start cron job"""
    schedule.every(1).seconds.do(process_cashback)
    while True:
        schedule.run_pending()
        time.sleep(1)

thread = threading.Thread(target=cron_job_get_purchase, daemon=True)
thread.start()