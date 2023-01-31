import tweepy, keys
from bs4 import BeautifulSoup as bs
import scrape_truecar


price_rounded = round(scrape_truecar.average_price,2)
tweet_message = 'The average is $' + str(price_rounded) + '.'

def api():
    auth = tweepy.OAuth1UserHandler(
        keys.API_KEY, keys.API_SECRET,
        keys.ACCESS_TOKEN, keys.ACESS_TOKEN_SECRET
    )

    return tweepy.API(auth)

def tweet(api: tweepy.API, message:str, image_path=None):
    if image_path:
        api.media_upload(message, image_path)
    else:
        api.update_status(message)
    
    print('Tweeted successfully!')


if __name__ == '__main__':
    api=api()
    tweet(api, tweet_message)
    

"""
cargurus, cars.com, autotrader, trucar
what if the twitter bot everyday just tweeted the average price of a random car??
honda = [s2000, civic, odyssey]
bmw = [3-series, x5]
etc...

then everyday it could tweet:

'Today, the average cost of a HONDA S2000 in city,state is $1234.56
Gathered from truecar, cargurus, etc'

and the city and state could change everyday too for fun?
"""