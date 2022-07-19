import pandas as pd
import re
import requests
from bs4 import BeautifulSoup as bs

baseurl = "https://www.parlamento.pt/ArquivoDocumentacao/Paginas/Arquivodevotacoes.aspx"

response = requests.get(baseurl)

soup = bs(response.content, "html.parser")

divs = soup.findAll("a", attrs={"title": re.compile("^Resultado")})
print(len(divs))
print(divs)