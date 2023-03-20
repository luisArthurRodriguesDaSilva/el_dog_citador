from src.Fa import *
import src.enderecos as enderecos
import json
import src.enderecos as enderecos
from random import randrange
import requests
from bs4 import BeautifulSoup
from src.ttApi import api, BRAZIL_WOE_ID


class bote:
    def __init__(self,):
        self.arq =enderecos.arq
        self.arq_tr=enderecos.arq_tr
        self.arq_dm=enderecos.arq_dm
        self.api = api
        self.brazil_trends = self.api.get_place_trends(BRAZIL_WOE_ID)
        self.alarme1=False
        #self.existir_em_salvas   = self.existir_em(arquivo=self.arq,coisa="twet",txt="")
        #self.existir_em_dm       = self.existir_em(arquivo=self.arq_dm,coisa="autor",txt="")
    def trending_atual(self):
          caras=[]
          for i in range(int(len(self.brazil_trends[0]['trends'])/10)):
              caras.append(str(self.brazil_trends[0]['trends'][i]['name'].replace('#','')))
          return caras
    
    def existir_em(self,txt,arquivo,coisa):
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
            salvos = json.load(f)
    
        salvos.append({"autor": autor})
    
        with open(self.arq_dm, 'w') as f:
            json.dump(salvos, f,indent=4)

    def postar(self,twets,tamanho):
    
        postado = twets[randrange(0, tamanho)]
        try:
            existir_em_salvas   = self.existir_em(arquivo=self.arq,coisa="twet",txt="")
            if existir_em_salvas==False and len(postado)< 279 and postado!="\n~":
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
        with open(self.arq_dm, "r") as f:
            nomes_da_dm= json.load(f)
            print(nomes_da_dm)
            for i in numeros_aleatorios(quantidade=5,limite=len(nomes_da_dm)-1):
                try:
                    print('i',i)
                    queryAutor = nomes_da_dm[i]['autor']
                    print('queryAutor:',queryAutor)
                    frases,autores = self.pesquisar(queryAutor)
                    twets = []
                    print(frases)
                    for c in range(len(autores) - 1):
                        print('c',c)
                        twets.append(f"""“{frases[c].replace('"', '')}”
__
~{autores[c]}""")
                        tamanho = c
                    self.postar(twets, tamanho)
                    print('postei')
                except Exception as e:
                    print(e) 

    def pesquisar(self,autor = 'frases'):
        if autor == 'frases':
            html = requests.get(f'https://www.pensador.com/{autor}', timeout=5).content 
        else:
            html = requests.get(f'https://www.pensador.com/busca.php?q={autor}', timeout=5).content    
        soup = BeautifulSoup(html, "html.parser")
        phrases = list(map(lambda x:x.text, soup.find_all('p',{'class':'frase'})))
        authors = list(map(lambda x:x.text, soup.find_all('span',{'class':'author-name'})))
        return phrases,authors
        #------------------------------------------------------------------------------------------    
    def ler_dm(self):
        for pessoa in self.api.get_direct_messages():
            mensagem=pessoa._json['message_create']['message_data']['text']
            if(mensagem[0:6]=="autor:" or mensagem[0:6]== "Autor:"):
                autor=mensagem[6:len(mensagem)]
                existir_em_dm       = self.existir_em(arquivo=self.arq_dm,coisa="autor",txt=f"{autor}")
                if(existir_em_dm==False):
                    self.salvar_autor(autor)
                    print(f"adicionado {autor} á lista")
                
    def escolha_random(self):
        frases,autores = self.pesquisar()
        try:
            twets = []
            for c in range(len(autores) - 1):
                twets.append(f"""“{frases[c].replace('"', '')}”
__
~{autores[c]}""")
                tamanho = c
            self.postar(twets, tamanho)
        except Exception as e:
            print(e)
    def escolha_autor(self):
        print("quem?")
        autor=input()
        frases,autores = self.pesquisar(autor)
        self.alarme1 = True
        try:
            twets = []
            for c in range(len(autores) - 1):
                twets.append(f"""“{frases[c].replace('"', '')}”
__
~{autores[c]}""")
                tamanho = c
            self.postar(twets, tamanho)
        except Exception as e:
            print(e)

    def escolha_trending(self):
        for cara in self.trending_atual():
            print(self.trending_atual())
            frases,autores = self.pesquisar(cara)
            self.alarme1=True
            try:
                twets=[]
                for c in range (len(autores)-1):
                    twets.append(f"""“{frases[c].replace('"','')}”
__              
~{autores[c]}""")
                    tamanho=c
                self.postar(twets,tamanho)

            except Exception as e:
                print(e)
    def escolha_dm(self):
        self.ler_dm()
        print('li')
        self.postar_dm()

if __name__ == '__main__':
    obj=bote()