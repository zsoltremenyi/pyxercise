import json
import requests
import re

URL = "https://us-states.p.rapidapi.com/basic"


headers = {
	"X-RapidAPI-Key": "b0e7075c29mshec40ece92f0b021p181835jsn7cb811e9ccfe",
	"X-RapidAPI-Host": "us-states.p.rapidapi.com"
}


response = requests.get(URL, headers=headers)
data = response.json()


class State:
	state_name_abbr = {i['name']: i['postal'] for i in data}


	def __init__(self, abbr):
		self.abbr = abbr


	def full_name(self):
		for key, value in self.state_name_abbr.items():
			if value == self.abbr:
				return key

state = State("CA")
print(state.full_name())