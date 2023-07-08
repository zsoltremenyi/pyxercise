import requests
from geocode import long_lat, api_key, city_name
import json


def something(func=long_lat()):
    if not func:
        return "Invalid input"
    else:
        request_weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat="
                                       f"{long_lat()[0]}&lon={long_lat()[1]}&appid={api_key}")
        weather_data = json.loads(request_weather.text)
        return weather_data
