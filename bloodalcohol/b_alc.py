import calculator
from country import Country
import pandas as pd




# different rules apply to proffessional drivers professional drivers

country_alcohol = {}

blood_alcohol_content = 0.08

try:
    country_of_interest = input("Country of interest? ")
    A = float(input("Total alcohol consumed, in oz: "))
    W = float(input("Bodyweight in pounds: "))
    r = input("Gender for alcohol distribution ratio ('m' male, 'f' female): ")
    H = float(input("Number of minutes since the last drink: "))


except ValueError:
    print("Please input valid value")


else:
    country = Country(country_of_interest.title(), calculator.b_alc_calc(A,W,r,H))
    print(country.get_dict_countries())
    print(country.get_bac())

# 12 floz beer = 8-9 floz malt liqour == 5floz red wine = 1.5 floz 80proof