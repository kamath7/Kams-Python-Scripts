import requests
from bs4 import BeautifulSoup

# URL of the UEFA Euro 2024 Wikipedia page
url = 'https://en.wikipedia.org/wiki/UEFA_Euro_2024'

# Fetch the webpage content
response = requests.get(url)
html_content = response.text

# Parse HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all tables with class "fevent"
tables = soup.find_all('table', class_='fevent')

# Initialize an empty list to store match data
matches = []

# Iterate through each table to find all matches
for table in tables:
    # Find the home team name
    home_team = table.find('th', class_='fhome').find('span', itemprop='name').text.strip()
    
    # Find the away team name
    away_team = table.find('th', class_='faway').find('span', itemprop='name').text.strip()
    
    # Format match details (e.g., "Germany v Scotland")
    match_details = f"{home_team} v {away_team}"
    
    # Find the match timings if available
    timings_row = table.find_next_sibling('tr', class_='fgoals')
    if timings_row:
        timings_cell = timings_row.find('td')
        if timings_cell:
            match_timings = timings_cell.text.strip()
        else:
            match_timings = 'Timing not available'
    else:
        match_timings = 'Timing not available'
    
    # Store match details in a dictionary
    match = {
        'Match': match_details,
        'Timings': match_timings
    }
    
    # Append match data to the list
    matches.append(match)

# Print or further process the extracted matches
for match in matches:
    print(match)