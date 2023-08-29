from django.conf import settings
from covid_data.commands.download_csv import Import
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.utils import timezone
from django_apscheduler.models import DjangoJobExecution
from covid_data.models import Csv_file
import sys

    
start_date = settings.START_DATE


def set_new_start_date(add_days):
    global start_date
    date = datetime.strptime(start_date, "%m-%d-%Y")
    modified_date = date + timedelta(days=add_days)
    start_date = datetime.strftime(modified_date, "%m-%d-%Y")


def get_start_date():
    global start_date
    last_csv_file = Csv_file.objects.last()
    if last_csv_file is not None:
        start_date = last_csv_file.pub_date.strftime("%m-%d-%Y")
        set_new_start_date(1)
    return start_date


def timed_download():
    print('importing csv datafile from date: {date}...'.format(date=start_date))
    Import.parse_csv_data(Import.import_csv(Import.get_url(get_start_date())),get_start_date())


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(timed_download, 'interval', seconds=10, name='timed download', jobstore='default')
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)
        
