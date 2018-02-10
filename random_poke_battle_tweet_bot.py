import tweepy
import time
from tweepy import OAuthHandler
import pandas as pd
import random

consumer_key = 'SegAXbekM9euiEVdlsQw8ECvF'
consumer_secret = 'xjyGZoASkYIH4An8Az6I2TT76JfJRNZAaMVkhx1Eco8sHiA1Ft'
access_token = '961480922641006592-JZSZ0si0JMMobAQxwMpRlcY8lT3pHwh'
access_secret = 'HODbqAywyoMbsRruOy3AX7ztV0j1HT8WeIKY0bJShI2sC'


auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth)


data = pd.read_csv('/home/anorak/Documents/twitter_bots/pokemonGO.csv')
poke_names = data['Name']

poke_moves = []

not_a_move = ['0','1','2','3','4','=']

with open('pokemon_moves') as f:
    for line in f:
        valid_move = [move for move in line.split() if move[0] not in not_a_move]
        move = " ".join(valid_move)
        poke_moves.append(move)



verbs_last_index = len(poke_moves) - 1


print(poke_names[150])

while True:
    random_poke_name = random.randrange(0,151)
    random_poke_move = random.randrange(1,verbs_last_index)
    random_poke_name_enemy = random.randrange(0,151)
    random_poke_damage = random.randint(0,100)
    text_1 = poke_names[random_poke_name] + " " + "used" + " " + poke_moves[random_poke_move] + "!"
    text_2 = "\n" + "Wild " + poke_names[random_poke_name_enemy] + " lost " + str(random_poke_damage) +" hp!"
    #print(text_1)
    #print(text_2)
    text = text_1 + text_2
    #print(text)
    api.update_status(text)

    time.sleep(900)
