import requests
import urllib.request
import time
from bs4 import BeautifulSoup as bs
import numpy as np
import pandas as pd
from urllib.request import urlopen

url = 'https://en.wikipedia.org/wiki/Twice'
page = requests.get(url)
soup = bs(page.content,'html.parser')
#find_all looks for tags (e.g. title, h2, p)
headlines = soup.find(id="bodyContent").find_all("h2")
for x in headlines:
    headline = x.text.split("[edit]")[0]
    print(headline)

