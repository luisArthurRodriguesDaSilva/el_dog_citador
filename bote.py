from random import Random
import threading
import time

from numpy import integer
from Fa import *
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
        self.arq_dm=enderecos.arq_dm
        self.api = tweepy.API(auth)
        self.brazil_trends = self.api.get_place_trends(BRAZIL_WOE_ID)
        self.alarme1=False
        #self.existir_em_salvas   = self.existir_em(arquivo=self.arq,coisa="twet",txt="")
        #self.existir_em_dm       = self.existir_em(arquivo=self.arq_dm,coisa="autor",txt="")
        
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
    
    def existir_em(self,txt,arquivo,coisa):
        print("passei por aqui")
        with open(arquivo, "r") as f:
            salvos = json.load(f)
        resposta = False
        for i in range (len(salvos)):
            if salvos[i][f"{coisa}"]==txt:
                resposta=True
                break
        return resposta

    def salvar_twet(self,twete):
        with open(self.arq, "r") as f:
            salvos = json.load(f)
    
        salvos.append({"twet": twete})
    
        with open(self.arq, 'w') as f:
            json.dump(salvos, f,indent=4)

    def salvar_autor(self,autor):
        with open(self.arq_dm, "r") as f:
            #print(self.arq_dm)
            salvos = json.load(f)
    
        salvos.append({"autor": autor})
    
        with open(self.arq_dm, 'w') as f:
            json.dump(salvos, f,indent=4)

    def postar(self,twets,tamanho):
    
        postado = twets[randrange(0, tamanho)]
        print(f"em postar")
        try:
            existir_em_salvas   = self.existir_em(arquivo=self.arq,coisa="twet",txt="")
            if existir_em_salvas==False and len(postado)< 279 and postado!="\n~":
                print(f"--------{existir_em_salvas}")
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
        except Exception as e:
            print(f"é isso {e}")

    def postar_dm(self):
        print("cheguei em postar dm")
        with open(self.arq_dm, "r") as f:
            nomes_da_dm= json.load(f)
            for i in numeros_aleatorios(quantidade=5,limite=len(nomes_da_dm)):
                try:
                    self.pesquisar(nomes_da_dm[i]['autor'])
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

    def inicializacao_classica(self):
        self.comeca_contagem()
        self.driver = webdriver.Chrome()#executable_path='/home/luis/Downloads/cromedriver/chromedriver')
        self.driver.get("https://www.pensador.com/citacoes/")
        self.alarme1 = True
        self.driver.maximize_window()

    def pesquisar(self,a):
        self.comeca_contagem()
        self.driver.find_element(By.NAME, 'q').click()
        self.driver.find_element(By.NAME, 'q').send_keys(a)
        self.driver.find_element(By.NAME, 'q').send_keys(Keys.ENTER)
        self.alarme1 = True
        #------------------------------------------------------------------------------------------    
    def ler_dm(self):
        for pessoa in self.api.get_direct_messages():
            mensagem=pessoa._json['message_create']['message_data']['text']
            if(mensagem[0:6]=="autor:" or mensagem[0:6]== "Autor:"):
                autor=mensagem[6:len(mensagem)]
                existir_em_dm       = self.existir_em(arquivo=self.arq_dm,coisa="autor",txt=f"{autor}")
        
                print(f"em ler dm --{existir_em_dm}--autor:{autor}")
                if(existir_em_dm==False):
                    self.salvar_autor(autor)
                    print(f"adicionado {autor} á lista")
                
    def escolha_random(self):
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
    def escolha_autor(self):
        print("quem?")
        autor=input()
        self.inicializacao_classica()
        self.comeca_contagem()
        self.pesquisar(autor)
        self.alarme1 = True
        try:
            print("entrei no try")
            frases = self.driver.find_elements(By.TAG_NAME, 'p')
            print("passeido frases")
            autores = self.driver.find_elements(By.CLASS_NAME, "autor")
            print(f"passei pelos autores{autores}")
            twets = []
            for c in range(len(autores) - 1):
                twets.append(f"""“{frases[c].text.replace('"', '')}”
__
~{autores[c].text}""")
                print(twets)
                tamanho = c
            self.postar(twets, tamanho)
        except Exception as e:
            print(e)

    def escolha_trending(self):
        self.inicializacao_classica()
        for cara in self.trending_atual():
            print(self.trending_atual())
            self.comeca_contagem()
            self.pesquisar(cara)
            self.alarme1=True
            try:
                frases=self.driver.find_elements(By.TAG_NAME,'p')
                autores=self.driver.find_elements(By.CLASS_NAME,"autor")
                twets=[]
                for c in range (len(autores)-1):
                    twets.append(f"""“{frases[c].text.replace('"','')}”
__              
~{autores[c].text}""")
                    tamanho=c
                self.postar(twets,tamanho)

            except Exception as e:
                print(e)
    def escolha_dm(self):
        self.inicializacao_classica()
        self.ler_dm()
        self.ler_dm()
        self.postar_dm()


    def rodar(self):
        print("autor,trending,dm ou random?")
        self.escolha=input()
        
        if (self.escolha == 'random') :
            self.escolha_random()

        elif(self.escolha == 'autor') :
            self.escolha_autor()
            
        elif (self.escolha == 'trending') :
            self.escolha_trending()
        
        elif(self.escolha =='dm'):
            self.escolha_dm()

if __name__ == '__main__':
    obj=bote()
    #print(obj.existir_em_dm(txt="jirafa"))