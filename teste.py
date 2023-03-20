import imagesFuncs as imgf
from ttApi import postIt, imageToMyDm , notifyByDm
import os
import time
from bs4 import BeautifulSoup
import requests

isProduction = lambda : False

def pesquisar(autor = 'frases'):
  if autor == 'frases':
      html = requests.get(f'https://www.pensador.com/{autor}', timeout=5).content 
  else:
      html = requests.get(f'https://www.pensador.com/busca.php?q={autor}', timeout=5).content    
  soup = BeautifulSoup(html, "html.parser")
  phrases = list(map(lambda x:x.text, soup.find_all('p',{'class':'frase'})))
  authors = list(map(lambda x:x.text, soup.find_all('span',{'class':'author-name'})))
  return phrases,authors

autor = 'iron man'

rawImagePath = imgf.crateIAimage(autor)
phrases,authors = pesquisar(autor)
selectdPhase,selectedAuthor = phrases[2],authors[2]
editedImage = imgf.getEditedImage(rawImagePath)
imgWithText = imgf.putTextOnImage(editedImage,selectdPhase,selectedAuthor)
finalImagePath = imgf.saveImage(imgWithText,selectedAuthor)["newPath"]
      
postIt(finalImagePath) if isProduction() else imageToMyDm(finalImagePath)
    