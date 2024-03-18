# modules/web_scraping.py
import logging
import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

def scrape_webpage(base_url):
    print("entered scrape")
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup.find_all("a", attrs={"title": re.compile("^Resultado")})

def extract_filename_from_url(url):
    return parse_qs(urlparse(url).query)['Fich'][0]