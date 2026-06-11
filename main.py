import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from rich import print

load_dotenv()


# Weather App in Python
# Ask for city name for weather
print("[purple bold]Weather Forecast[/purple bold]")
city = input("\nEnter a search city: ")
city = city.strip()

# error checking if no city name is entered
if city:
    city
else:
    print("Please enter a valid city name.")


def daily_weather(city):
    # Get weather from API
    api_key = os.getenv("API_KEY")
    api_url = os.getenv("API_URL")
    url = f"{api_url}?query={city}&key={api_key}&units=imperial"
    weather = requests.get(url)

    if weather.status_code == 200:
        city_weather = weather.json()  # current temp
        try:
            city_name = city_weather["city"]
            temp = round(city_weather["temperature"]["current"])
            # display current temp
            print(f"\nThe current temperature for {city_name} is {temp}°F.\n")

        except KeyError:
            print("Invalid city name. Please try again.")
    else:
        print("Failed to retrieve data.")


def forecast_weather(city):
    api_key = os.getenv("API_KEY")
    api_url = os.getenv("API_URL")
    forecast_url = os.getenv("FORECAST_URL")

    forecast_city = f"{forecast_url}?query={city}&key={api_key}&units=imperial"

    forecast = requests.get(forecast_city)

    city_forecast = forecast.json()  # forecast weather

    for day in city_forecast["daily"]:
        timestamp = day["time"]  # get timestamp by date
        forecast_dt = datetime.fromtimestamp(timestamp)  # convert timestamp to date
        format_date = forecast_dt.date()  # convert timestamp to date
        forecast_date = format_date.strftime("%a")  # timestamp to day of week

        temperature_future = day["temperature"]["day"]
        # forecasted temp for x days

        if forecast_dt.date() != datetime.today().date():
            # for timestamp in city_forecast:
            print(f"[blue]{forecast_date}[/blue]: {round(temperature_future)}°F")


def credit():
    print("\n[green]Created by Amy Rowell[/green]")


daily_weather(city)
forecast_weather(city)
credit()
