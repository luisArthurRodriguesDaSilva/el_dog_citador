import imagesFuncs as imgf
from ttApi import postIt, imageToMyDm , notifyByDm
import os
import time
from random import randrange
import json
from quotersApi import getQuotes

isProduction = lambda : False

for image in os.listdir('finalImages'):
    postIt('finalImages/' + image)
    time.sleep(10)