import pandas as pd
import numpy as np
from django.conf import settings
from covid_data.models import Csv_data, Csv_file
import datetime

class Import():
    def get_url(start_date):
        url = '{url}/{date}.csv'.format(url=settings.IMPORT_URL, date=start_date)
        print (url)
        return url


    def import_csv(url):
        data = pd.read_csv(url)
        # print (data)
        return data
    
    def create_object_csv_file(start_date):
        csv_file = Csv_file(
            pub_date = start_date
        )
        csv_file.save()
        # print('id = {id}'.format(id=csv_file.id))
        return csv_file
    
    def check_columns(data):
        if 'Province/State' not in data.columns:
            data.rename(columns={'Province_State': 'Province/State'}, inplace=True)
        if 'Country/Region' not in data.columns:
            data.rename(columns={'Country_Region': 'Country/Region'}, inplace=True)
        if 'Last Update' not in data.columns:
            data.rename(columns={'Last_Update': 'Last Update'}, inplace=True)
        return data
    
    def fix_datetime_last_update(last_update):
        try:
            return datetime.datetime.strptime(last_update, "%m/%d/%Y %H:%M").strftime("%Y-%m-%d %H:%M")
        except(ValueError): 
            try:
                return datetime.datetime.strptime(last_update, "%m/%d/%y %H:%M").strftime("%Y-%m-%d %H:%M")
            except (ValueError):
                try:
                    return datetime.datetime.strptime(last_update, "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d %H:%M")
                except (ValueError):
                    return datetime.datetime.strptime(last_update, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M")
    
    def create_object_csv_data(data, csv_file):
        data = data.replace(np.nan, None)
        data = Import.check_columns(data)
        #print(data)

        for index, row in data.iterrows():
            Csv_data.objects.create(
                province_state = row['Province/State'],
                coutry_region = row['Country/Region'],
                last_update = Import.fix_datetime_last_update(row['Last Update']),
                confirmed = row['Confirmed'],
                deaths = row['Deaths'],
                recovered = row['Recovered'],
                csv_file = csv_file
            )
            
            
    def parse_csv_data(data, start_date):  
        new_date_format = datetime.datetime.strptime(start_date, "%m-%d-%Y").strftime("%Y-%m-%d")
     
        csv_file = Import.create_object_csv_file(new_date_format)
        Import.create_object_csv_data(data, csv_file)
        