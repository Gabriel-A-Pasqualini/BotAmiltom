from bs4 import BeautifulSoup
from urllib.request import urlopen
from federal_primeiro_ganhador import Primeiroganhador

import requests

url = "https://noticias.uol.com.br/loterias/loteria-federal/"

response = urlopen(url)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')

tabela = soup.find("div", class_="lottery-results-table").get_text()

print()
print()

listateste = list(tabela.split())
'''
for i in range(0,len(listateste)): 
    i == len(listateste)

    destino = listateste[i]
    #destino[0,4,7,10,13,16]
    #bilhete[1,5,8,11,14,17]
    #premio [2,6,9,12,15,18]
'''
bilhete = listateste[1]
primeiro_bilhete = listateste[5]
segundo_bilhete = listateste[8]
terceiro_bilhete = listateste[11]
quarto_bilhete = listateste[14]
quinto_bilhete = listateste[17]

print(bilhete)
print(primeiro_bilhete)
print(segundo_bilhete)
print(terceiro_bilhete)
print(quarto_bilhete)
print(quinto_bilhete)
'''
i = 2
f = 2 
while i == f:
'''

cd_ganhador = primeiro_bilhete[4]+primeiro_bilhete[5]

primeiro = Primeiroganhador(cd_ganhador)
print("")
print("numero que deu: "+cd_ganhador )
print("")
print(primeiro)
print("")
