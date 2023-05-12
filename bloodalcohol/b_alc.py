import calculator
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

site = requests.get(url="http://iardwebprod.azurewebsites.net/science-resources/detail/Blood-Alcohol-Concentration-(BAC)-Limits")
soup = bs(site.content, features="html.parser")
table_rows = soup.find_all("tr")
countries = [n.splitlines() for n in [i.text.strip() for i in table_rows]]
country_dict = {countries[something][0]:countries[something][1] for something in range(1, len(countries))}
print(country_dict)


# no official BAC is defined, but it is prohibited to drive under the inluence of alcohol.
# different rules apply to proffessional drivers professional drivers
country_alcohol = {}

blood_alcohol_content = 0.08

# try:
#     A = float(input("Total alcohol consumed, in oz: "))
#     W = float(input("Bodyweight in pounds: "))
#     r = input("Gender for alcohol distribution ratio ('m' male, 'f' female): ")
#     H = float(input("Number of minutes since the last drink: "))
#
#
# except ValueError:
#     print("Please input valid value")
#
#
# else:
#     print(calculator.b_alc_calc(A,W,r,H))

# 12 floz beer = 8-9 floz malt liqour == 5floz red wine = 1.5 floz 80proof