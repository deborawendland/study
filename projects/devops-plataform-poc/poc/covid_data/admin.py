from django.contrib import admin
from .models import Csv_file, Csv_data, Covid_deaths

admin.site.register(Csv_file)
admin.site.register(Csv_data)
admin.site.register(Covid_deaths)
