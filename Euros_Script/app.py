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
import pandas as pd 


url = 'https://en.wikipedia.org/wiki/UEFA_Euro_2024'

response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

tables = soup.find_all('table', class_='fevent')


matches_portugal = []
matches_england = []

# Iterate through each table of fixtures
for table in tables:
    home_team = table.find('th', class_='fhome').find('span', itemprop='name').text.strip()
    away_team = table.find('th', class_='faway').find('span', itemprop='name').text.strip()
    match_details = f"{home_team} v {away_team}"
    
    # Check if the match involves Portugal
    if 'Portugal' in match_details:
        matches_portugal.append({
            'Match': match_details
        })
    
    # Check if the match involves England
    if 'England' in match_details:
        matches_england.append({
            'Match': match_details
        })


df_portugal_matches = pd.DataFrame(matches_portugal)

df_england_matches = pd.DataFrame(matches_england)
