from imagesFuncs import crateIAimage, getEditedImage, putTextOnImage, saveImage
from ttApi import (
    postIt,
    imageToMyDm,
)
from random import randrange
from quotersApi import getQuotes
import os


def isProduction():
    os.getenv("producao") == "true"


def getSelectedQuoteInfo(autor):
    phrases, authors = getQuotes(autor)
    randomNumber = randrange(1, len(phrases) - 1)

    [selectdPhase, selectedAuthor] = [
        phrases[randomNumber],
        authors[randomNumber],
    ]
    return selectdPhase, selectedAuthor


def play_image_mode(selectdPhase, selectedAuthor):
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
