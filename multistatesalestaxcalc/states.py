from bs4 import BeautifulSoup as bs
import requests

URL = "https://taxfoundation.org/2021-sales-taxes/"

site =requests.get(URL)

soup = bs(site.content, features="html.parser")
table_rows = soup.find_all('tr')
print(table_rows)