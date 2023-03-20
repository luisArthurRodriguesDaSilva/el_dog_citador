import numpy as np

def getSpaces(text):
    spaces = []
    for i in range(len(text)):
        if text[i] == ' ':
            spaces.append(i)
    return spaces


def getBiggestSmallest(arraio,n) :
  for index,curr  in enumerate(arraio):
    if curr > n:
      return arraio[index-1]
  return 9000

def divitedText(text, SizeLine):
  spaces = np.array(getSpaces(text))
  volta = 0
  while 1:
    volta+=1
    local = getBiggestSmallest(spaces,(SizeLine*volta)-2)
    if local == 9000:
      break
    text = text[:local] + '\n' + text[local+1:]
  return text , volta

def putAutor(quote,autor):
  return f'{quote}\n____\n\n~{autor}'