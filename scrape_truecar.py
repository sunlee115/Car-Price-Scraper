import requests
import lxml
import cchardet
from time import sleep,time
from random import randint
from bs4 import BeautifulSoup as bs

print("Welcome to Sun's Truecar scraper :)\n")
make = input("What make? ")
model = input("What model? ")
years = input("What years? (YYYY-YYYY or MIN-MAX) ")

truecar_url = 'https://www.truecar.com/used-cars-for-sale/listings/' + make.lower().strip() + '/' + model.lower().strip() + '/year-' + years.strip() +'/?searchRadius=5000&sort[]=price_asc'
requests_session = requests.Session()
response = requests_session.get(truecar_url)
soup = bs(response.content,'lxml')
num_cars_response = soup.find_all(attrs={"data-test": "bodyCopy"})[-1].text
num_cars_total = int(num_cars_response.split("TrueCar has ")[1].split(" used")[0].replace(",",""))
try:
    last_page = int(soup.find_all(attrs={"data-test": "paginationItem"})[-1].text)
except:
    last_page=1
if(last_page==1):
    print(f"\n{num_cars_total} {model}s found! That's only {last_page} page to scrape :D\n")
else:
    print(f"\n{num_cars_total} {model}s found! That's {last_page} pages to scrape .-.\n")
sum_price = 0
average_price=0
all_prices = []

start_time=time()
for page in range(1,last_page+1):
    print(f'Scraping page {page}...')
    new_url = truecar_url.split("?")[0] + '?page=' + str(page) + '&' + truecar_url.split("?")[1]
    response = requests_session.get(new_url)
    soup = bs(response.content,'lxml')
    prices_response=soup.find_all(attrs={"data-test": "vehicleCardPricingBlockPrice"})
    for x in prices_response:
        price_float = float(x.text.replace("$","").replace(",",""))
        all_prices.append(price_float)

all_prices.sort()
for x in all_prices:
    sum_price+=x
    print(f'${x:.2f}')
average_price = sum_price/len(all_prices)
if(num_cars_total!=len(all_prices)):
    print(f"\n{len(all_prices)} out of {num_cars_total} {model}s have prices available.")
print(f'\nAverage of {len(all_prices)} prices = ${average_price:.2f}.')
print(f"\nHere's your Truecar search result link: {truecar_url}")
print(f"\nHave a good day. Beep boop.\n")
print(f"\nElapsed time is {time()-start_time}")