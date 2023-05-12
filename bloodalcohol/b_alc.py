import calculator
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

site = requests.get(url="http://iardwebprod.azurewebsites.net/science-resources/detail/Blood-Alcohol-Concentration-(BAC)-Limits")
soup = bs(site.content, features="html.parser")
class_list = set()
tags = {tag.name for tag in soup.find_all() }
print(tags)
for tag in tags:

    for i in soup.find_all(tag):
        if i.has_attr("class"):
            if len(i['class']) != 0:
                class_list.add(" ". join(i['class']))
print(class_list)
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