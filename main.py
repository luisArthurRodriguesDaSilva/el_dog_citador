from bote import *
import time
import os

obj=bote()
#autor,trending,dm ou random?
while True:
  obj.rodar('dm')
  print('proximo')
  time.sleep(int(os.getenv('intervalo')))