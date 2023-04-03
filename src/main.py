from ttApi import (
    getActualTrending,
    makeFriends,
    twetIt,
    notifyByDm,
)
import os
import time
from botWork import getSelectedQuoteInfo, play_image_mode


def isProduction():
    os.getenv("producao") == "true"


def need_images():
    os.getenv("withImages") == "true"


interval = int(os.getenv("intervalo"))

while 1:
    trendingGuys = getActualTrending()
    for guy in trendingGuys:
        try:
            makeFriends(q=guy)
            selectdPhase, selectedAuthor = getSelectedQuoteInfo(guy)
            formatted_text = f"{selectdPhase}\n__\n{selectedAuthor}"
            if len(formatted_text) > 280:
                raise "grande demais"
            if not need_images():
                twetIt(text=formatted_text)
            else:
                play_image_mode(selectdPhase, selectedAuthor)
        except Exception as e:
            print(e)
        print("proximo")
        time.sleep(interval)
    notifyByDm("saiu da rodinha")
    time.sleep(4000)
