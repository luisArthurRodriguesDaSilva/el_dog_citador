from random import Random
import threading
import time

import fs
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

global salvos
global arq
global alarme1
arq = (r'C:\Users\luarp\PycharmProjects\testecit\salvas')



def escar():
    pyautogui.press('esc')
    print('escou1')
def contar():
    global alarme1
    alarme1=False
    inicial=time.time()
    for i in range(6):
        final=time.time()
        time.sleep(1)
        if alarme1 :
            print("alarmou1")
            break
        elif final-inicial>5:
            escar()
            break
def comeca_contagem():
    print("entrei1")
    time.sleep(1)
    threading.Thread(target=contar).start()

print("autor,trending ou random?")
escolha=input()

if escolha =='trending':
    comeca_contagem()
    driver = webdriver.Chrome()
    driver.get("https://www.pensador.com/citacoes/")
    alarme1 = True
    driver.maximize_window()
    #driver.find_element(By.XPATH,'/html/body/div[5]/img')
    for cara in fs.trending_atual():
        #print(fs.trending_atual())
        comeca_contagem()
        driver.find_element(By.NAME, 'q').click()
        driver.find_element(By.NAME,'q').send_keys(cara)
        driver.find_element(By.NAME,'q').send_keys(Keys.ENTER)
        alarme1=True
        try:
            frases=driver.find_elements(By.TAG_NAME,'p')
            autores=driver.find_elements(By.CLASS_NAME,"autor")
            twets=[]

            for c in range (len(autores)-1):
                twets.append(f"""“{frases[c].text.replace('"','')}”
__      
~{autores[c].text}""")
                tamanho=c
            fs.postar(twets,tamanho)

        except Exception as e:
            print(e)
elif escolha =='random':
    comeca_contagem()
    driver = webdriver.Chrome()
    driver.get("https://www.pensador.com/citacoes/")
    alarme1 = True
    driver.maximize_window()
    try:
        frases = driver.find_elements(By.TAG_NAME, 'p')
        autores = driver.find_elements(By.CLASS_NAME, "autor")
        twets = []
        for c in range(len(autores) - 1):
            twets.append(f"""“{frases[c].text.replace('"', '')}”
__
~{autores[c].text}""")
            tamanho = c
        fs.postar(twets, tamanho)
    except Exception as e:
        print(e)
elif escolha == 'autor':
    print("quem?")
    autor=input()

    comeca_contagem()
    driver = webdriver.Chrome()
    driver.get("https://www.pensador.com/citacoes/")
    alarme1 = True
    driver.maximize_window()

    comeca_contagem()
    driver.find_element(By.NAME, 'q').click()
    driver.find_element(By.NAME, 'q').send_keys(autor)
    driver.find_element(By.NAME, 'q').send_keys(Keys.ENTER)
    alarme1 = True
    try:
        frases = driver.find_elements(By.TAG_NAME, 'p')
        autores = driver.find_elements(By.CLASS_NAME, "autor")
        twets = []
        for c in range(len(autores) - 1):
            twets.append(f"""“{frases[c].text.replace('"', '')}”
__
~{autores[c].text}""")
            tamanho = c
        fs.postar(twets, tamanho)
    except Exception as e:
        print(e)

