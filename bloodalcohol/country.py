from bs4 import BeautifulSoup as bs
import requests



class Country:
    def __init__(self, country):
        self.country = country

    def get_dict_countries(self):
        site = requests.get(
            url="http://iardwebprod.azurewebsites.net/science-resources/detail/Blood-Alcohol-Concentration-(BAC)-Limits")
        soup = bs(site.content, features="html.parser")
        table_rows = soup.find_all("tr")
        countries = [n.splitlines() for n in [i.text.strip() for i in table_rows]]
        country_dict = {countries[something][0]: countries[something][1] for something in range(1, len(countries))}
        return country_dict

    def get_bac(self):
        for k, v in self.get_dict_countries().items():
            if k == self.country:
                try:
                    float(v)
                except:
                    return f"In {k} no official BAC is defined, but it is prohibited to drive under the inluence of alcohol."
                else:
                    return f"{k}:{v}"

something = Country("Burkina Faso")
print(something.get_bac())