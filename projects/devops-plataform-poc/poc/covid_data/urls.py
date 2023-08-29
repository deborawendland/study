from django.urls import path

from . import views

urlpatterns = [
    path("all/", views.display_table_all_data, name="display table all data"),
    path("<str:country_region>", views.display_table_country_region, name="display table by country or region"),
]