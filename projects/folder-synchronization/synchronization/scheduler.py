import schedule
import time

def run_scheduler(interval, task):
    print ("scheduler starting...")
    
    schedule.every(interval).seconds.do(task)
    while True:
        schedule.run_pending()
        time.sleep(1)