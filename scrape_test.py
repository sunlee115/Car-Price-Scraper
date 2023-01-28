import requests
import time
from bs4 import BeautifulSoup as bs


url = 'https://www.newegg.com/dji-mini-3-pro-263174/p/N82E16815515034?Description=dji%20drone&cm_re=dji_drone-_-15-515-034-_-Product&quicklink=true'
page = requests.get(url)
soup = bs(page.content,'html.parser')

price_result = soup.find("li",class_="price-current")
price = float(price_result.text.split("$")[1])
#print (price)
print(f'{price:.2f}')

