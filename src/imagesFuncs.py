import openai
import os
import requests
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from PIL.ImageFilter import BLUR
import textFuncs as tf
import Fa
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

startOfPrompts = "day realistic, focused, older and modern"

openai_key = os.getenv("openaiApiKey")
print(openai_key)


def crateIAimage(prompt):
    openai.api_key = openai_key
    response = openai.Image.create(prompt=startOfPrompts + prompt, n=1, size="512x512")
    image_url = response["data"][0]["url"]
    image = requests.get(image_url).content
    imageAdress = "image.jpg"
    with open(imageAdress, "wb") as f:
        f.write(image)
    return imageAdress


diviter = 15


def getEditedImage(imagePath):
    img = Image.open(imagePath)
    img = img.filter(BLUR).filter(BLUR).filter(BLUR)
    img = ImageEnhance.Brightness(img).enhance(0.4)
    return img


def getBlocksSizes(pilImage):
    [width, height] = pilImage.size
    [widthBlock, heightBlock] = map(lambda x: int(x / diviter),
                                    [width, height])
    return widthBlock, heightBlock


def putTextOnImage(pilImage, text, autor):
    img = pilImage
    completeText = tf.putAutor(text, autor=autor)
    imageDraw = ImageDraw.Draw(img)
    widthBlock, heightBlock = getBlocksSizes(img)
    freeSpace = heightBlock * (diviter - 1)
    adaptedText, numberOfLines = tf.divitedText(completeText, diviter)
    if numberOfLines > 15:
        raise "muitas linhas"
    divisor = Fa.biggest(numberOfLines + 5, diviter + 5)
    fontSize = freeSpace / divisor
    font = ImageFont.truetype("./font/arial.ttf", int(fontSize))
    imageDraw.text(
        (widthBlock, heightBlock),  # initial cordinates
        adaptedText,
        fill=(250, 250, 250),
        font=font,
    )
    return img


def saveImage(pilImage, autor):
    dirPath = "finalImages"
    exist = os.path.isdir(dirPath)
    if not exist:
        os.mkdir(dirPath)
    newPath = f"{dirPath}/{autor}.jpg"
    pilImage.save(newPath)
    return {"newPath": newPath}
