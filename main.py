from bote import *
import time
import os

obj=bote()
#autor,trending,dm ou random?
while True:
  obj.rodar('trending')
  time.sleep(int(os.getenv('intervalo')))