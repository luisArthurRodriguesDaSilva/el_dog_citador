import src.imagesFuncs as imgf
from src.ttApi import postIt, imageToMyDm , notifyByDm
import os
import time
from random import randrange
import json
from quotersApi import getQuotes

isProduction = lambda : False

with open('nomes_da_dm.json', "r") as f:
  nomes_da_dm= json.load(f)
  for i in range(10):
    try:
      randomNumber = randrange(1,10)
      autor = nomes_da_dm[randomNumber]['autor']


      phrases,authors = getQuotes(autor)
      selectdPhase,selectedAuthor = phrases[randomNumber],authors[randomNumber]
      if len(selectdPhase)>200:
         raise 'grande demais'

      rawImagePath = 'image.jpg'#imgf.crateIAimage(selectdPhase)
      editedImage = imgf.getEditedImage(rawImagePath)
      imgWithText = imgf.putTextOnImage(editedImage,selectdPhase,selectedAuthor)
      finalImagePath = imgf.saveImage(imgWithText,selectedAuthor)["newPath"]

      postIt(finalImagePath) if isProduction() else imageToMyDm(finalImagePath)
    except Exception as e:
       print(e)
    