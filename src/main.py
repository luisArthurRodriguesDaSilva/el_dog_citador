from imagesFuncs import crateIAimage, getEditedImage, putTextOnImage, saveImage
from ttApi import (
    getActualTrending,
    makeFriends,
    postIt,
    twetIt,
    imageToMyDm,
    notifyByDm,
)
import os
import time
from random import randrange
from quotersApi import getQuotes
from botWork import getSelectedQuoteInfo, play_image_mode


def isProduction():
    os.getenv("producao") == "true"


def need_images():
    os.getenv("withImages") == "true"


while 1:
    trendingGuys = getActualTrending()
    for guy in trendingGuys:
        try:
            makeFriends(guy)
            selectdPhase, selectedAuthor = getSelectedQuoteInfo(guy)
            formatted_text = f"{selectdPhase}\n__\n{selectedAuthor}"
            if len(formatted_text) > 280:
                raise "grande demais"
            if not need_images():
                twetIt(formatted_text)
            else:
                play_image_mode(selectdPhase, selectedAuthor)
        except Exception as e:
            print(e)
        print("proximo")
        time.sleep(int(os.getenv("intervalo")))
    notifyByDm("saiu da rodinha")
    time.sleep(4000)
