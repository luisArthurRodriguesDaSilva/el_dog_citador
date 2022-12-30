from random import *


def existir(num,arayo):
      resposta=False
      for i in range(len(arayo)):
            if num==arayo[i]:
                  resposta= True
                  break
      return resposta

def numeros_aleatorios(quantidade,limite):
      numeros=[]
      for i in range(quantidade):
            while 1 and quantidade<=limite:
                  numero_novo=randrange(0,limite)
                  if existir(numero_novo,numeros)==False:
                        numeros.append(numero_novo)
                        break
      return numeros
