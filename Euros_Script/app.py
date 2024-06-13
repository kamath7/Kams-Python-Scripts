'''
Use Wiki to scrape through Euros 

Get the interesting fixtures only
Get Portgual matches
Get English matches
Add timing also


'''

import requests
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/UEFA_Euro_2024"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


print(soup)

