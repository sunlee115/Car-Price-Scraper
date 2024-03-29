import requests
import time
from bs4 import BeautifulSoup as bs

"""
what if the twitter bot everyday just tweeted the average price of a random car??
honda = [s2000, civic, odyssey]
bmw = [3-series, x5]
etc...

then everyday it could tweet:

'Today, the average cost of a HONDA S2000 in city,state is $1234.56
Gathered from truecar, cargurus, etc'

and the city and state could change everyday too for fun?
"""

#url = 'https://www.truecar.com/used-cars-for-sale/listings/location-carrollton-tx/?searchRadius=25'
original_url = 'https://www.truecar.com/used-cars-for-sale/listings/honda/civic/location-carrollton-tx/?searchRadius=50&sort[]=price_asc'
#original_url = 'https://www.truecar.com/used-cars-for-sale/listings/honda/civic/location-carrollton-tx/?page=1&searchRadius=50&sort[]=price_asc'

response = requests.get(original_url)
soup = bs(response.content,'html.parser')

price_search_result=soup.find_all(attrs={"data-test": "vehicleCardPricingBlockPrice"})

list_of_prices = []
for x in price_search_result:
    #have to make sure it does smth when the price is 'no value' and subtract it from length when calculating average
    price_float = float(x.text.replace("$","").replace(",",""))
    list_of_prices.append(price_float)
list_of_prices.sort()
sum = 0
print('Prices of certain cars in area:')
for x in list_of_prices:
    sum+=x
    print(f'${x:.2f}')
average_price = sum/len(list_of_prices)
print(f'\nAverage of above prices is: ${average_price:.2f}.')

"""
sites to use:
cargurus, cars.com, autotrader, trucar

- only works for truecar, idk how to make the others work yet lols
for multiple pages, go to the bottom or whatever shows the last page #, 
and scrape that value. change url and loop through prices until it reaches 
that last value?
"""

