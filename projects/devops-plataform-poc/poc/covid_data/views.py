from django.http import HttpResponse
from covid_data.models import Csv_data
from django.shortcuts import render
import pandas as pd

def display_table_all_data(request):
    csv_data = pd.DataFrame(list(Csv_data.objects.all().values()))
    html_table = csv_data.to_html(classes='table table-stripped')
    return HttpResponse(html_table)


def display_table_country_region(request, country_region):
    csv_data = pd.DataFrame(list(Csv_data.objects.all().values()))
    filtered_data = csv_data.query("coutry_region == '{country}'".format(country=country_region))
    html_table = filtered_data.to_html(classes='table table-stripped')
    return HttpResponse(html_table)
