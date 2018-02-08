import tweepy,time,sys
from tweepy import OAuthHandler
import scraper

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''


auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth)

list_of_links = scraper.web_scrape_to_list()
print (list_of_links[0])
num = int(0)


for link in list_of_links:
    print link
    #api.update_status(status = link)
    #time.sleep(900)
