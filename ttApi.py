import tweepy
import os
import dotenv
dotenv.load_dotenv(dotenv.find_dotenv())

auth = tweepy.OAuthHandler(os.getenv('citchave1'),os.getenv('citchave2'))
auth.set_access_token(os.getenv('citchave3'),os.getenv('citchave4'))
api = tweepy.API(auth)
print((api.get_user(screen_name='noBugChapeu')._json['id_str']))


BRAZIL_WOE_ID = 23424768
