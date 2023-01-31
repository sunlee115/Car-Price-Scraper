import requests
from time import *
from random import randint
from bs4 import BeautifulSoup as bs

make = input("What make? ").lower().strip()
model = input("What model? ").lower().strip()

truecar_url = 'https://www.truecar.com/used-cars-for-sale/listings/' + make + '/' + model + '/location-carrollton-tx/?searchRadius=5000&sort[]=price_asc'

#truecar_url = 'https://www.truecar.com/used-cars-for-sale/listings/honda/s2000/location-carrollton-tx/?searchRadius=5000&sort[]=price_asc'

response = requests.get(truecar_url)
soup = bs(response.content,'html.parser')
last_page = int(soup.find_all(attrs={"data-test": "paginationItem"})[-1].text)
count_cars = 0
sum_price = 0
average_price=0
all_prices = []
print(f'\n{last_page} pages to scrape .-.\n')

for page in range(1,last_page+1):
    print(f'Scraping page {page}...')
    new_url = truecar_url.split("?")[0] + '?page=' + str(page) + '&' + truecar_url.split("?")[1]
    response = requests.get(new_url)
    soup = bs(response.content,'html.parser')
    prices_response=soup.find_all(attrs={"data-test": "vehicleCardPricingBlockPrice"})
    for x in prices_response:
        price_float = float(x.text.replace("$","").replace(",",""))
        all_prices.append(price_float)
           
    sleep(randint(1,5))
    print(f'Finished page {page}!\n')  
    sleep(1)

all_prices.sort()
print(f'Prices of {len(all_prices)} cars in area:')
for x in all_prices:
    sum_price+=x
    print(f'${x:.2f}')
average_price = sum_price/len(all_prices)
print(f'\nAverage of above prices is: ${average_price:.2f}.')