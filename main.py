import pandas as pd
import re
import requests
from bs4 import BeautifulSoup as bs
import dotenv
import os
import constants
from mongoengine import connect
import urllib.request

dotenv.load_dotenv()

# connect(os.getenv('DB_MONGODB_CONNECTION_STRING'))

response = requests.get(constants.AR_ARCHIVE_BASE_URL)
soup = bs(response.content, "html.parser")

divs = soup.findAll("a", attrs={"title": re.compile("^Resultado")})

pdf_url = divs[0]['href']
print(divs[0]['href'])
urllib.request.urlretrieve(pdf_url, os.getenv("FILESYSTEM_ROOT_PATH") + "/filename.pdf")
