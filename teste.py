import imagesFuncs as imgf
from ttApi import postIt, imageToMyDm , notifyByDm
import os
import time
from bs4 import BeautifulSoup
import requests
from random import randrange
import json

isProduction = lambda : True

def pesquisar(autor = 'frases'):
  if autor == 'frases':
      html = requests.get(f'https://www.pensador.com/{autor}', timeout=5).content 
  else:
      html = requests.get(f'https://www.pensador.com/busca.php?q={autor}', timeout=5).content    
  soup = BeautifulSoup(html, "html.parser")
  phrases = list(map(lambda x:x.text, soup.find_all('p',{'class':'frase'})))
  authors = list(map(lambda x:x.text, soup.find_all('span',{'class':'author-name'})))
  return phrases,authors



with open('nomes_da_dm.json', "r") as f:
  nomes_da_dm= json.load(f)
  for i in range(1):
    try:
      randomNumber = randrange(1,10)
      autor = nomes_da_dm[randomNumber]['autor']


      rawImagePath = imgf.crateIAimage(autor)
      phrases,authors = pesquisar(autor)
      selectdPhase,selectedAuthor = phrases[randomNumber],authors[randomNumber]
      editedImage = imgf.getEditedImage(rawImagePath)
      imgWithText = imgf.putTextOnImage(editedImage,selectdPhase,selectedAuthor)
      finalImagePath = imgf.saveImage(imgWithText,selectedAuthor)["newPath"]

      postIt(finalImagePath) if isProduction() else imageToMyDm(finalImagePath)
    except Exception as e:
       print(e)
    