from fastapi import FastAPI
from router import router
from threading import Thread
from cronjobs.cron import cron_job_get_purchase

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
async def start_cron():
    """Call cron job"""
    thread = Thread(target=cron_job_get_purchase)
    thread.start()