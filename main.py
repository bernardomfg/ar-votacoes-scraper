from sqlite3 import DataError
from urllib.parse import urlparse, parse_qs
from urllib.request import urlretrieve
from model.File import File
from datetime import datetime
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup as bs
import dotenv
import os
import constants
import mongoengine as mongo


dotenv.load_dotenv()
mongo.connect(host=os.getenv('DB_MONGODB_CONNECTION_STRING'))

response = requests.get(constants.AR_ARCHIVE_BASE_URL)
soup = bs(response.content, "html.parser")

votings = soup.findAll("a", attrs={"title": re.compile("^Resultado")})

for voting in votings:
    filename = parse_qs(urlparse(voting['href']).query)['Fich'][0]
    filePath = os.getenv("FILESYSTEM_ROOT_PATH") + "/" + filename
    fileDoc = File(file_url=voting['href'], isParsed=False, filename=filename, localFilePath=filePath, created=datetime.now())
    try:
        fileDoc.save()
        urlretrieve(fileDoc.file_url, fileDoc.localFilePath)
    except mongo.errors.NotUniqueError:
        print("Already added on db")
        continue
