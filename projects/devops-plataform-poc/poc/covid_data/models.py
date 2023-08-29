from django.db import models

class Csv_file(models.Model):
    pub_date = models.DateField("date published")

class Csv_data(models.Model):
    province_state = models.CharField(max_length=200,null=True, blank=True)
    coutry_region = models.CharField(max_length=200)
    last_update = models.DateTimeField("last update")
    confirmed = models.IntegerField(null=True, blank=True)
    deaths = models.IntegerField(null=True, blank=True)
    recovered = models.IntegerField(null=True, blank=True)
    csv_file = models.ForeignKey(Csv_file, on_delete=models.CASCADE)

class Covid_deaths(models.Model):
    country = models.CharField(max_length=200)
    total_deaths = models.IntegerField(default=None)
    fetched_datetime = models.DateTimeField("datetime fetched")
    pub_date = models.ForeignKey(Csv_file, on_delete=models.CASCADE)