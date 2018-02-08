import tweepy,time,sys
from tweepy import OAuthHandler
import scraper

consumer_key = 'SegAXbekM9euiEVdlsQw8ECvF'
consumer_secret = 'xjyGZoASkYIH4An8Az6I2TT76JfJRNZAaMVkhx1Eco8sHiA1Ft'
access_token = '961480922641006592-JZSZ0si0JMMobAQxwMpRlcY8lT3pHwh'
access_secret = 'HODbqAywyoMbsRruOy3AX7ztV0j1HT8WeIKY0bJShI2sC'


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
