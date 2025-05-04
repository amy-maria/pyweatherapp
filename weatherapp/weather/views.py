from django.shortcuts import render
from django.conf import settings
import requests
from datetime import datetime


# Create your views here.
def home(request):
    context = {}
    if request.method == "POST":
        city = request.POST.get("city")
        api_key = settings.API_KEY
        api_url = settings.API_URL
        forecast_api_url = settings.FORECAST_URL

        url = f"{api_url}?query={city}&key={api_key}&units=imperial"
        weather = requests.get(url)

        forecast_url = f"{forecast_api_url}?query={city}&key={api_key}&units=imperial"

        forecast = requests.get(forecast_url)

        if weather.status_code == 200:
            try:
                city_weather = weather.json()  # current temp
                # print(city_weather)

                context["city_name"] = city_weather["city"]
                context["temp_current"] = round(city_weather["temperature"]["current"])
                context["current_condition"] = city_weather["condition"][
                    "description"
                ].title()
                context["current_icon_url"] = city_weather["condition"]["icon_url"]
                context["current_icon"] = city_weather["condition"]["icon"]

            except KeyError:
                context["error"] = "Invalid city name. Please try again."

        # forecast weather

        if forecast.status_code == 200:
            try:
                city_forecast = forecast.json()  # forecast weather
                forecast_list = []
                # print(city_forecast)

                # forecast for tomorrow + 4 days
                for i, day in enumerate(city_forecast["daily"][1:6]):
                    timestamp = day["time"]  # get timestamp by date
                    forecast_dt = datetime.fromtimestamp(timestamp)

                    format_date = forecast_dt.date()  # convert timestamp to date
                    forecast_date = forecast_dt.strftime("%a")  # day of week
                    temperature_future = day["temperature"]["day"]
                    # forecasted temp for given day of week
                    temperature_min = round(day["temperature"]["minimum"])
                    temperature_max = round(day["temperature"]["maximum"])
                    daily_conditions = day["condition"]["description"]
                    icon_url = day["condition"]["icon_url"]
                    icon = day["condition"]["icon"]

                    if forecast_dt.date():
                        forecast_list.append(
                            {
                                "forecast_day": forecast_date,
                                "temp": temperature_future,
                                "max": temperature_max,
                                "min": temperature_min,
                                "condition": daily_conditions,
                                "icon_url": icon_url,
                                "icon": icon,
                            }
                        )
                        # for timestamp in city_forecast:
                        context["forecast_list"] = forecast_list
                        print(forecast_list)
            except KeyError:
                context["forecast_error"] = "Could not parse content."
        else:
            context["error"] = "Failed to retrieve data."
    return render(request, "weather/home.html", context)
