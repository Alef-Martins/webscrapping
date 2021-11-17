import requests #solicitações
from bs4 import BeautifulSoup
#import pandas as pd

classificação = []
c = 1


# Armazena a página web em uma variável
response = requests.get('https://www.band.uol.com.br/esportes/automobilismo/formula-1/classificacao')

content = response.content

# Converte a variável content para o formato HTML
site = BeautifulSoup(content, 'html.parser')

# Procura a tag HTML específica     #atributo da tag alvo
posição = site.find('table', attrs={'class': 'pilots table'})
tabelas = posição.find_all('tr', attrs={'class': 'ng-star-inserted'})

print(f'\033[32m\033[1m\033[4m|{"Pos":>4}| {"Piloto":<20}| {"País":<15}| {"Equipe":<20}| Pts   |\033[m')
    
for tabela in tabelas:
    tabelas = posição.find('tr', attrs={'class': 'ng-star-inserted'})
    conteudo = tabela.find_all(name='td')
    cont = 0
    for item in conteudo:
        cont += 1
        if cont == 2:
            conteudo = item.find_next(name='td')
            classificação.append(conteudo.text)
    tabelas = posição.find('tr', attrs={'class': 'ng-star-inserted'})
    piloto = tabela.find('div', attrs={'class': 'info'})
    nome = piloto.find('p', attrs={'class': 'name'})
    país = piloto.find('span', attrs={'class': 'country ng-star-inserted'})
    equipe = piloto.find('span', attrs={'class': 'brand ng-star-inserted'})
    print(f'\033[4m|{c:3}º| {nome.text:<20}| {país.text:<15}| {equipe.text:20}| {classificação[c-1]:6}|')
    c+=1

