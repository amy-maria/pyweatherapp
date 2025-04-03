import requests
import os
from dotenv import load_dotenv

load_dotenv()


# Weather App in Python
# Ask for city name for weather
city = input("Enter a search city: ")
city = city.strip()
# print(city)
# Get weather from API
api_key = os.getenv("api_key")
api_url = os.getenv("api_url")
url = f"{api_url}?query={city}&key={api_key}&units=imperial"

response = requests.get(url)
# print(response)

weather_data = response.json()
print(weather_data)


# if city, call api, error please enter city
# Get forecast for city for next 5 days
# ? Temp graph for weather in next 5 days
