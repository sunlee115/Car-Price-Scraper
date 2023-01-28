import requests
import urllib.request
import time
from bs4 import BeautifulSoup as bs
import numpy as np
import pandas as pd
from urllib.request import urlopen

url = 'https://en.wikipedia.org/wiki/Epidemiology_of_depression'
html = urlopen(url) 
soup = bs(html, 'html.parser')


"""
for multiple pages, go to the bottom or whatever shows the last page #, 
and scrape that value. change url and loop through prices until it reaches 
that last value?
"""

