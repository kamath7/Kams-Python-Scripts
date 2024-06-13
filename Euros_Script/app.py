'''
Use Wiki to scrape through Euros 

Get the interesting fixtures only
Get Portgual matches
Get English matches
Add timing also


'''

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz


url = 'https://en.wikipedia.org/wiki/UEFA_Euro_2024'

response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

tables = soup.find_all('table', class_='fevent')

matches = []

for table in tables:
    home_team = table.find('th', class_='fhome').find('span', itemprop='name').text.strip()
    away_team = table.find('th', class_='faway').find('span', itemprop='name').text.strip()
    matches.append(f"{home_team} v {away_team}")

for match in matches:
    print(match)