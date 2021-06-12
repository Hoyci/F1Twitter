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

teste = F1()

if datetime.now().date() != teste.nextRace():
    faltamDias = teste.nextRace() - datetime.now().date()
    mensagem = f"{reactions['paises']['checkered']} {teste.gpName()} {flag.flag(teste.listaBandeiras())} \nFaltam {faltamDias.days} dias para a corrida em {teste.nextCircuit()}"
    emojis_tweet = emoji.emojize(mensagem, use_aliases=True)
    bot.enviarTweet(emojis_tweet)
else:
    mensagem = f"Hoje é dia de corrida em {teste.nextCountry()}"
    bot.enviarTweet(mensagem)



