import json
import tweepy
import chaves
import enderecos
from random import randrange, uniform

auth = tweepy.OAuthHandler(chaves.chave1, chaves.chave2)
auth.set_access_token(chaves.chave3, chaves.chave4)
BRAZIL_WOE_ID = 23424768

class bote:
      def __init__(self,auth,BRAZIL_WOE_ID,enderecos):
            self.arq =enderecos.arq
            self.arq_tr=enderecos.arq_tr
            self.api = tweepy.API(auth)
            self.brazil_trends = self.api.get_place_trends(BRAZIL_WOE_ID)

      def trending_atual(self):
            caras=[]
            for i in range(int(len(self.brazil_trends[0]['trends'])/5)):
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
      
      