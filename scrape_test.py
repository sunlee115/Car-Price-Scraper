import requests
import urllib.request
import time
from bs4 import BeautifulSoup as bs
import numpy as np
import pandas as pd
from urllib.request import urlopen

url = 'https://en.wikipedia.org/wiki/Epidemiology_of_depression'
page = requests.get(url)
soup = bs(page.content,'html.parser')
headlines = soup.find(id="bodyContent").find_all("h2")
for head in headlines:
    print (head.text)