from datetime import datetime
import boto3
import tweepy
from imgs import createImages
from f1Class import F1
from twitter_handler import Twitter


ssm_client = boto3.client("ssm")
api_key = ssm_client.get_parameter(Name="API-Key", WithDecryption=True)
api_secret_key = ssm_client.get_parameter(Name="API-Secret-Key", WithDecryption=True)
api_token = ssm_client.get_parameter(Name="Acess-Token", WithDecryption=True)
api_secret_token = ssm_client.get_parameter(Name="Acess-Secret-Token", WithDecryption=True)

API_KEY = api_key["Parameter"]["Value"]
API_SECRET_KEY = api_secret_key["Parameter"]["Value"]
API_TOKEN = api_token["Parameter"]["Value"]
API_SECRET_TOKEN = api_secret_token['Parameter']["Value"]

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(API_TOKEN, API_SECRET_TOKEN)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
bot = Twitter(auth, api)

f1 = F1()
img = createImages()
# post everyday
bot.enviarTweet(f1.message())

# post on saturday
day = f1.nextRace() - datetime.today().date()
if day.days == 1:
    img.createConstructorResultImg()
    imgPath = "constructorResult.jpg"
    bot.enviarTweetComImg(f1.message(), imgPath)
    
# post on sunday
if day.days == 0:
    img.createQualifyImg()
    imgPath = "qualifyImage.jpg"
    bot.enviarTweetComImg(f1.message(), imgPath)
