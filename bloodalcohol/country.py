from bs4 import BeautifulSoup as bs
import requests


class Country:
    def __init__(self, country, bac):
        self.country = country
        self.bac = bac

    def get_dict_countries(self):
        site = requests.get(
            url="http://iardwebprod.azurewebsites.net/science-resources/detail/Blood-Alcohol-Concentration-(BAC)-Limits")
        soup = bs(site.content, features="html.parser")
        table_rows = soup.find_all("tr")
        countries = [n.splitlines() for n in [i.text.strip() for i in table_rows]]
        country_dict = {countries[data][0]: countries[data][1] for data in range(1, len(countries))}
        return country_dict

    def get_bac(self):
        for k, v in self.get_dict_countries().items():
            #if k == self.country:
            if self.country in k:
                try:
                    float(v)
                except:
                    return f"In {k} no official BAC is defined, but it is prohibited to drive under the inluence of alcohol."
                else:
                    self.bac = round(self.bac, 2)
                    if self.bac <= float(v):
                        return f"You are allowed to drive in {k} - the limit of 'bac' is {v}, your level is {self.bac} - " \
                               f",but strongly recommended not to. The above stated only apply to non-professional drivers."

                    else:
                        return f"You are not allowed to drive. The limit is {v}, your 'BAC' is {self.bac}"


