from bote import *
import time
import os

obj=bote()
possibilidates = ['trending','dm','random']
while True:
  escolha = possibilidates[randint(0,2)]
  print(escolha)
  try:
    if (escolha == 'random') :
      obj.escolha_random()

    elif(escolha == 'autor') :
        obj.escolha_autor()

    elif (escolha == 'trending') :
        obj.escolha_trending()

    elif(escolha =='dm'):
        obj.escolha_dm()
  except Exception as e:
    print(e)
  print('proximo')
  time.sleep(int(os.getenv('intervalo')))