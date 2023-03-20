from bs4 import BeautifulSoup
import requests

def getQuotes(autor = 'frases'):
  if autor == 'frases':
      html = requests.get(f'https://www.pensador.com/{autor}', timeout=5).content 
  else:
      html = requests.get(f'https://www.pensador.com/busca.php?q={autor}', timeout=5).content    
  soup = BeautifulSoup(html, "html.parser")
  phrases = list(map(lambda x:x.text, soup.find_all('p',{'class':'frase'})))
  authors = list(map(lambda x:x.text, soup.find_all('span',{'class':'author-name'})))
  return phrases,authors