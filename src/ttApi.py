import tweepy
import os
import dotenv
import json
dotenv.load_dotenv(dotenv.find_dotenv())

BRAZIL_WOE_ID = 23424768

auth = tweepy.OAuthHandler(os.getenv('citchave1'),os.getenv('citchave2'))
auth.set_access_token(os.getenv('citchave3'),os.getenv('citchave4'))
api = tweepy.API(auth)


def postIt(filename,text=""):
    api.update_status_with_media(status=text,filename=filename)
def notifyByDm(text):
  api.send_direct_message(1505211970643009544,text=text)

def imageToMyDm(image,text=' s '):
  media = api.media_upload(filename=image)

  api.send_direct_message(
    1505211970643009544,text=' s',
    attachment_type='media',
    attachment_media_id=media.media_id)

def getActualTrending(WOE_ID=BRAZIL_WOE_ID):
  brazil_trends = api.get_place_trends(WOE_ID)  
  caras=list(map(lambda x: x['name'].replace('#',''),brazil_trends[0]['trends']))
  return caras

def getDMautors():
  autors = []
  messages = api.get_direct_messages(count=40)
  print(len(messages))
  for message in messages:
    #print(json.dumps(message._json, indent=4))
    messageText=message._json['message_create']['message_data']['text']
    if(messageText[0:6]=="autor:" or messageText[0:6]== "Autor:"):
        autor=messageText[6:len(messageText)]
        autors.append(autor)
  return autors

