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
matches = []
good_matches = []

matches_portugal = []
matches_england = []
good_teams = ["Italy", "Germany", "England", "Portugal", "Spain", "Netherlands", "France", "Croatia"]

# Iterate through each table of fixtures
for table in tables:
    home_team = table.find('th', class_='fhome').find('span', itemprop='name').text.strip()
    away_team = table.find('th', class_='faway').find('span', itemprop='name').text.strip()
    match_details = f"{home_team} v {away_team}"

    matches.append(match_details)
    
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
    if home_team in good_teams and away_team in good_teams:
        good_match_details = f"{home_team} v {away_team}"
        good_matches.append(good_match_details)


df_portugal_matches = pd.DataFrame(matches_portugal)

df_england_matches = pd.DataFrame(matches_england)

df_matches = pd.DataFrame(matches)

df_good_matches = pd.DataFrame(good_matches)

df_portugal_matches.to_csv("portugal_matches.csv",index=False)
df_england_matches.to_csv("england_matches.csv",index=False)
df_good_matches.to_csv("good_matches.csv",index=False)
df_matches.to_csv("all_matches.csv",index=False)
