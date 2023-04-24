import requests
from bs4 import BeautifulSoup
import pprint

# use: .titleline instead of .storylink

URL = 'https://news.ycombinator.com/news'
next_page = '?p=2'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.select('.titleline')
subtext = soup.select('.subtext')


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

def create_cutom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.a['href']
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_cutom_hn(links, subtext))