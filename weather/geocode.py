import requests
import json

city_name = input("Where are you? ")
api_key = "b4a21ba89e12eafcde8d348978a3ad13"


def long_lat(request_geo=requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={api_key}")):
    try:
        longitude = json.loads(request_geo.text)[0]["lon"]
        latitude = json.loads(request_geo.text)[0]["lat"]
    except IndexError:
        return False
    else:
        return longitude, latitude