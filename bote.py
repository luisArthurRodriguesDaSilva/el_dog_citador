from random import Random
import threading
import time
import enderecos
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import tweepy
import chaves
import enderecos
from random import randrange, uniform

auth = tweepy.OAuthHandler(chaves.chave1, chaves.chave2)
auth.set_access_token(chaves.chave3, chaves.chave4)
BRAZIL_WOE_ID = 23424768

class bote:
    def __init__(self):
          self.arq =enderecos.arq
          self.arq_tr=enderecos.arq_tr
          self.api = tweepy.API(auth)
          self.brazil_trends = self.api.get_place_trends(BRAZIL_WOE_ID)
          self.alarme1=False

    def escar(self):
          pyautogui.press('esc')
          print('escou1')

    def contar(self):
          self.alarme1=False
          inicial=time.time()
          for i in range(6):
            final=time.time()
            time.sleep(1)
            if self.alarme1 :
                print("alarmou1")
                break
            elif final-inicial>5:
                self.escar()
                break

    def comeca_contagem(self):
          print("entrei1")
          time.sleep(1)
          threading.Thread(target=self.contar).start()

    def trending_atual(self):
          caras=[]
          for i in range(int(len(self.brazil_trends[0]['trends'])/10)):
              caras.append(str(self.brazil_trends[0]['trends'][i]['name'].replace('#','')))
          return caras

    def existir_em_salvas(self,postado):
        with open(self.arq, "r") as f:
            salvos = json.load(f)
        resposta = False
        for i in range (len(salvos)):
            #print(f"(em existir) {salvos[i]['twet']}\n(tamanho) {len(salvos)}  i:{i}")
            if salvos[i]['twet']==postado:
                resposta=True
                break
        return resposta

    def salvar_twet(self,twete):
        with open(self.arq, "r") as f:
            salvos = json.load(f)
    
        salvos.append({"twet": twete})
    
        with open(self.arq, 'w') as f:
            json.dump(salvos, f,indent=4)

    def postar(self,twets,tamanho):
    
        postado = twets[randrange(0, tamanho)]
        print(f"em postar")
        if self.existir_em_salvas(postado)==False and len(postado)< 279 and postado!="\n~":
            print(f"--------{self.existir_em_salvas(postado)}")
            try:
                self.api.update_status(postado)
            except Exception as e:
                print("-----------------")
                print(f"{e} : {postado}")
                self.postar(twets, tamanho)
                print("-----------------")
            self.salvar_twet(postado)
        else:
            print(f"repetiu{postado}")
            self.postar(twets,tamanho)

    def inicializacao_classica(self):
        self.comeca_contagem()
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.pensador.com/citacoes/")
        self.alarme1 = True
        self.driver.maximize_window()
        #------------------------------------------------------------------------------------------
    def rodar(self):
        print("autor,trending ou random?")
        escolha=input()
        
        if (escolha == 'random') :
            self.inicializacao_classica()
            try:
                frases = self.driver.find_elements(By.TAG_NAME, 'p')
                autores = self.driver.find_elements(By.CLASS_NAME, "autor")
                twets = []
                for c in range(len(autores) - 1):
                    twets.append(f"""“{frases[c].text.replace('"', '')}”
__
~{autores[c].text}""")
                    tamanho = c
                self.postar(twets, tamanho)
            except Exception as e:
                print(e)
            
        elif( escolha == 'autor') :
            print("quem?")
            autor=input()
            self.inicializacao_classica()
            self.comeca_contagem()
            self.driver.find_element(By.NAME, 'q').click()
            self.driver.find_element(By.NAME, 'q').send_keys(autor)
            self.driver.find_element(By.NAME, 'q').send_keys(Keys.ENTER)
            self.alarme1 = True
            try:
                frases = self.driver.find_elements(By.TAG_NAME, 'p')
                autores = self.driver.find_elements(By.CLASS_NAME, "autor")
                twets = []
                for c in range(len(autores) - 1):
                    twets.append(f"""“{frases[c].text.replace('"', '')}”
__
~{autores[c].text}""")
                    tamanho = c
                self.postar(twets, tamanho)
            except Exception as e:
                print(e)


        
        elif (escolha == 'trending') :
            self.inicializacao_classica()
            for cara in self.trending_atual():
                print(self.trending_atual())
                self.comeca_contagem()
                self.driver.find_element(By.NAME, 'q').click()
                self.driver.find_element(By.NAME,'q').send_keys(cara)
                self.driver.find_element(By.NAME,'q').send_keys(Keys.ENTER)
                self.alarme1=True
                try:
                    frases=self.driver.find_elements(By.TAG_NAME,'p')
                    autores=self.driver.find_elements(By.CLASS_NAME,"autor")
                    twets=[]

                    for c in range (len(autores)-1):
                        print("cheguei no for")
                        twets.append(f"""“{frases[c].text.replace('"','')}”
__              
~{autores[c].text}""")
                        tamanho=c
                    self.postar(twets,tamanho)

                except Exception as e:
                    print(e)
        

      