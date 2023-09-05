import schedule
import time
import logging

def run_scheduler(params, task):
    logging.info("sync interval set to {interval}".format(interval = params["sync_interval"]))
    logging.info("scheduler starting...")
    
    schedule.every(params["sync_interval"]).seconds.do(task, params)
    while True:
        schedule.run_pending()
        time.sleep(1)