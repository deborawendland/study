from django.apps import AppConfig

# import sched, time

class CovidDataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'covid_data'

    def ready(self):
            from covid_data.scheduler import scheduler
            scheduler.start()
            