import bs4
import requests

URL = "https://navalnuclearlab.energy.gov/"

web_page = requests.get(URL)

soup = bs4.BeautifulSoup(web_page.text, 'lxml')

all_links = []
for link in soup.findAll('a'):
    href = link.get('href')
    link_text = link.text
    if href.startswith('http'):
        all_links.append((link_text, href))

for text, ref in all_links:
    print(text, ref)
