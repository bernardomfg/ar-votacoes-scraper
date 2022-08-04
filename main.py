import pandas as pd
import re
import requests
from bs4 import BeautifulSoup as bs
import dotenv
import os
import constants
from mongoengine import connect

dotenv.load_dotenv()

connect(os.getenv('DB_MONGODB_CONNECTION_STRING'))

response = requests.get(constants.AR_ARCHIVE_BASE_URL)
soup = bs(response.content, "html.parser")

divs = soup.findAll("a", attrs={"title": re.compile("^Resultado")})
print(divs[0])