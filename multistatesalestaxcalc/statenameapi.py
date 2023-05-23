import json
import requests
import re

url = "https://us-states.p.rapidapi.com/basic"

headers = {
	"X-RapidAPI-Key": "b0e7075c29mshec40ece92f0b021p181835jsn7cb811e9ccfe",
	"X-RapidAPI-Host": "us-states.p.rapidapi.com"
}


response = requests.get(url, headers=headers)
data = response.json()

state_name_abbr = {state_name_abbr[i['name']]:i['postal'] for i in data}



print(clean_name)