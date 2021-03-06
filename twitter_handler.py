import tweepy.error

class Twitter():
    def __init__(self, auth, api):
        self.auth = auth
        self.api = api
        
        try:
            self.api.verify_credentials()
            print('Autenticado')
        except tweepy.error.TweepError as e:
            print('Erro na autenticação')
            raise e

    def enviarTweet(self, tweet):
        try:
            self.api.update_status(tweet)
            print(tweet)
            print('Postado com sucesso')
        except Exception as e:
            print(e)
            raise e
    
    def enviarTweetComImg(self, tweet, img):
        try:
            self.api.update_with_media(img, tweet)
            print('Imagem postada com sucesso')
        except Exception as e:
            print(e)
            raise e
