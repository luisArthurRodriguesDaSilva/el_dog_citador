import tweepy
import os
import dotenv
dotenv.load_dotenv(dotenv.find_dotenv())

auth = tweepy.OAuthHandler(os.getenv('citchave1'),os.getenv('citchave2'))
auth.set_access_token(os.getenv('citchave3'),os.getenv('citchave4'))
api = tweepy.API(auth)
print((api.get_user(screen_name='noBugChapeu')._json['id_str']))


def postIt(filename):
    api.update_status_with_media(status='',filename=filename)
def notifyByDm(text):
  api.send_direct_message(1505211970643009544,text=text)

def imageToMyDm(image,text=' s '):
  media = api.media_upload(filename=image)

  api.send_direct_message(
    1505211970643009544,text=' s',
    attachment_type='media',
    attachment_media_id=media.media_id)

BRAZIL_WOE_ID = 23424768
