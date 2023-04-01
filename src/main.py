from imagesFuncs import crateIAimage, getEditedImage, putTextOnImage, saveImage
from ttApi import postIt, imageToMyDm, getActualTrending, notifyByDm
import os
import time
from random import randrange
from quotersApi import getQuotes


def isProduction():
    os.getenv("producao") == "true"


while 1:
    trendingGuys = getActualTrending()
    notifyByDm(f"trending len{len(trendingGuys)}")
    for guy in trendingGuys:
        try:
            # makeFriends(guy)
            autor = guy

            phrases, authors = getQuotes(autor)
            randomNumber = randrange(1, len(phrases) - 1)

            [selectdPhase, selectedAuthor] = [
                phrases[randomNumber],
                authors[randomNumber],
            ]

            if len(selectdPhase) > 200 or selectdPhase.count("\n") > 2:
                raise "grande demais"
            rawImagePath = crateIAimage(selectdPhase)
            editedImage = getEditedImage(rawImagePath)
            imgWithText = putTextOnImage(editedImage, selectdPhase, selectedAuthor)
            finalImagePath = saveImage(imgWithText, selectedAuthor)["newPath"]
            print(finalImagePath)
            postIt(
                finalImagePath, text=selectedAuthor
            ) if isProduction() else imageToMyDm(finalImagePath)
        except Exception as e:
            print(e)
        print("proximo")
        time.sleep(int(os.getenv("intervalo")))
    notifyByDm("saiu da rodinha")
    time.sleep(4000)
