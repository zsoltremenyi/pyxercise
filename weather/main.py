from weather import something
from geocode import city_name
from datetime import datetime

try:
    temperature = something()["main"]["temp"]
    sunr = something()["sys"]["sunrise"]
    suns = something()["sys"]["sunset"]+something()["timezone"]
    weath_conditions = something()["weather"]["main"]
except (TypeError, KeyError):
    print(f"Input: {city_name}, not found.")
else:
    print(f"{city_name.title()} weather: {temperature} degrees Kelvin."
          f"\nSunrise is at {datetime.fromtimestamp(sunr).time()}."
          f"\nThe sun sets at {datetime.fromtimestamp(suns).time()}.")

    if weath_conditions == "Rain":
        print("It's raining, get your umbrella.")
    elif weath_conditions == "Clouds":
        print("It's cloudy.")
    elif weath_conditions == "Snow":
        print("It's snowing, better stay home. I hate winter sports anyway.")
    elif weath_conditions == "Extreme":
        print("If you go outside, you will probably not return.")
    else:
        print("The sky is clear.")




print(weather.something())