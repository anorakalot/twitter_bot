import tweepy,time,sys
from tweepy import OAuthHandler

consumer_key = 'INSERT YOUR OWN '
consumer_secret = 'INSERT YOUR OWN'
access_token = 'INSERT YOUR OWN'
access_secret = 'INSERT YOUR OWN'

argfile = str(sys.argv[1])

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth)

bot_file = open(argfile)
l = bot_file.readlines()
bot_file.close()

for tweet in l:
    api.update_status(status = tweet)
    time.sleep(900)
