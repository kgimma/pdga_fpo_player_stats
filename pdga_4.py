#!/usr/bin/env python3

"""
PDGA Scraper
"""

# ----------
# IMPORTS
# ----------

from bs4 import BeautifulSoup
import csv 
import requests 
import time

from . import util # NOTE: How to import our local util.py file.

# ----------
# CONSTANTS
# Set all of the variable constants that you will need.
# ----------

BASE_URL = 'https://www.pdga.com/players/stats'

# ----------
# EXTRACT
# These functions extract the data from their source
# ----------

def generate_params(year):
    return {
        'Year': str(year),
        'player_Class': '1',
        'Gender': 'Female',
        'Bracket': 'All',
        'continent': 'All',
        'Country': 'All',
        'StateProv': 'All',
        'order': 'Prize',
        'sort': 'desc',
    }

# NOTE: this function could probably be moved to the util file too, it will not change. Some others below might be movable as well.
def scrape_response(response):
    """Create a BeautifulSoup object from the HTML content of the response"""
    return BeautifulSoup(response.content, 'html.parser')

def fetch_url(url, params):
    """Fetches the URL with the given params and returns the response"""
    return requests.get(url, params=params)

def get_num_pages(soup):
    """Extract the total number of pages from the 'pagination' section of the page"""
    pagination = soup.find('ul', class_='pagination')
    if pagination:
        return int(pagination.find_all('li')[-2].text)
    else:
        return 1

# ----------
# TRANSFORM
# These functions transform the extracted data into something useful
# ----------

def get_table(soup):
    """Find the table element that contains the player statistics"""
    return soup.find('table')

def get_headers(table):
    """Extract the headers from the table"""
    return [th.text.strip() for th in table.find_all('th')]

def get_rows(table):
    """Extract the rows from the table"""
    rows = []
    for tr in table.find_all('tr'):
        row = [td.text for td in tr.find_all('td')]
        if row:
            rows.append(row)
    return rows

def format_rows(rows):
  """Removing new lines and white space from each element in string"""
  for sublist in rows:
      for i in range(len(sublist)):
          sublist[i] = sublist[i].strip()
  return rows

# ----------
# LOAD
# These functions load your extracted data into a useful format
# ----------

def to_csv(headers, rows):
    """Write headers and rows to CSV"""
    with open('pdga_4.csv', 'w') as file:
        rows.insert(0, headers)
        writer = csv.writer(file)
        writer.writerows(rows)

def __main__():
    """ Loop through each page and scrape the data """
    headers_list = []
    rows_list = [] 
    for year in range(1974, 2024):
        print("year:", year)
        for i in range(0, 100):
            print("page:", i)
            if(i % 2 == 0): time.sleep(1)
            url_params = generate_params(year)
            url_params['page'] = str(i)
            response = fetch_url(BASE_URL, params=url_params)
            scraped_response = scrape_response(response)
            table = get_table(scraped_response)
            if(table == None):
                break;
            headers = get_headers(table)
            if(len(headers_list) == 0):
                headers_list = headers
            unformatted_rows = get_rows(table)
            rows = format_rows(unformatted_rows)
            rows_list += rows
        
    to_csv(headers_list, rows_list)