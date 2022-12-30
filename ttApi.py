import tweepy
import os
import dotenv
dotenv.load_dotenv(dotenv.find_dotenv())

auth = tweepy.OAuthHandler(os.getenv('chave1'),os.getenv('chave2'))
auth.set_access_token(os.getenv('chave3'),os.getenv('chave4'))
api = tweepy.API(auth)
print((api.get_user(screen_name='noBugChapeu')._json['id_str']))
