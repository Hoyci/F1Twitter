import tweepy
from f1Class import F1
from twitter_handler import Twitter
from datetime import datetime
from auth import TWITTER_API_KEY, TWITTER_API_SECRET_KEY, TWITTER_API_SECRET_TOKEN, TWITTER_API_TOKEN
import emoji
import flag
import json

with open('emojis.json', 'r') as emojis:
    reactions = json.load(emojis)

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
auth.set_access_token(TWITTER_API_TOKEN, TWITTER_API_SECRET_TOKEN)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
bot = Twitter(auth, api)

f1 = F1()

if datetime.now().date() != f1.nextRace():
    faltamDias = f1.nextRace() - datetime.now().date()
    mensagem = f"{reactions['paises']['checkered']} {f1.gpName()} {flag.flag(f1.listaBandeiras())} \nFaltam {faltamDias.days} dias para a corrida em {f1.nextCircuit()}"
    emojis_tweet = emoji.emojize(mensagem, use_aliases=True)
    bot.enviarTweet(emojis_tweet)
else:
    mensagem = f"Hoje é dia de corrida em {f1.nextCountry()}"
    bot.enviarTweet(mensagem)



