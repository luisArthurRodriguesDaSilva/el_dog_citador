import requests

from bs4 import BeautifulSoup
q='thomas edson'
html = requests.get(f'https://www.pensador.com/{q}',  timeout=1).content

soup = BeautifulSoup(html, "html.parser")
phrases = list(map(lambda x:x.text, soup.find_all('p',{'class':'frase'})))
authors = list(map(lambda x:x.text, soup.find_all('span',{'class':'author-name'})))
print(len(authors),len(phrases))

for  author, phrase in zip(authors,phrases):
  print(phrase,'\n',author,'\n')
