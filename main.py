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