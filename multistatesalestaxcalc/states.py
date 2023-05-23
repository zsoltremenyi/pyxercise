from bs4 import BeautifulSoup as bs
import requests

URL = "https://taxfoundation.org/2021-sales-taxes/"

site =requests.get(URL)

soup = bs(site.content, features="html.parser")
# results = soup.find(id="Table")
# print(results.prettify())
table_rows = soup.find_all('tr')
states = [n.splitlines() for n in [i.text.strip() for i in table_rows]]
state_and_tax = {i[0].replace(u"\xa0", u" "):i[1].replace("%", "") for i in states[1:-1]}
print(state_and_tax)