import tweepy,time,sys
from tweepy import OAuthHandler

consumer_key = 'SegAXbekM9euiEVdlsQw8ECvF'
consumer_secret = 'xjyGZoASkYIH4An8Az6I2TT76JfJRNZAaMVkhx1Eco8sHiA1Ft'
access_token = '961480922641006592-JZSZ0si0JMMobAQxwMpRlcY8lT3pHwh'
access_secret = 'HODbqAywyoMbsRruOy3AX7ztV0j1HT8WeIKY0bJShI2sC'

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
