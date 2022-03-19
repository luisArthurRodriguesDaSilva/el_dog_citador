from random import randrange, uniform
import json
import tweepy
import chaves

global BRAZIL_WOE_ID
global salvos
global arq

BRAZIL_WOE_ID = 23424768

arq = (r'C:\Users\luarp\PycharmProjects\testecit\salvas')
arq_tr=(r'C:\Users\luarp\PycharmProjects\testecit\trending_atual')

auth = tweepy.OAuthHandler(chaves.chave1, chaves.chave2)
auth.set_access_token(chaves.chave3, chaves.chave4)
api = tweepy.API(auth)

def trending_atual():
    brazil_trends = api.get_place_trends(BRAZIL_WOE_ID)
    caras=[]
    for i in range(int(len(brazil_trends[0]['trends'])/5)):
        caras.append(str(brazil_trends[0]['trends'][i]['name'].replace('#','')))
    return caras


def existir_em_salvas(postado):
    global salvos
    with open(arq, "r") as f:
        salvos = json.load(f)
    resposta = False
    for i in range (len(salvos)):
        #print(f"(em existir) {salvos[i]['twet']}\n(tamanho) {len(salvos)}  i:{i}")
        if salvos[i]['twet']==postado:
            resposta=True
            break
    return resposta
def salvar_twet(twete):
    global salvos
    arq = (r'C:\Users\luarp\PycharmProjects\testecit\salvas')

    with open(arq, "r") as f:
        salvos = json.load(f)

    salvos.append({"twet": twete})

    with open(arq, 'w') as f:
        json.dump(salvos, f,indent=4)
def postar(twets,tamanho):

    postado = twets[randrange(0, tamanho)]
    print(f"em postar")
    if existir_em_salvas(postado)==False and len(postado)< 279 and postado!="\n~":
        print(f"--------{existir_em_salvas(postado)}")
        try:
            api.update_status(postado)
        except Exception as e:
            print("-----------------")
            print(f"{e} : {postado}")
            postar(twets, tamanho)
            print("-----------------")
        salvar_twet(postado)

    else:
        print(f"repetiu{postado}")
        postar(twets,tamanho)