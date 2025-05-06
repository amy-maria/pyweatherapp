from django.urls import path
from weatherapp.weather.views import home

urlpatterns = [
    path("", home, name="home"),
]
