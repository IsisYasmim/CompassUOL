'''
Ex2:
Apresente a média da coluna contendo o número de filmes.
'''

import pandas as pd

# lendo o arquivo CSV
df = pd.read_csv('actors.csv')

# fazendo tratamento de dados
df['Actor'] = df['Actor'].str.replace('"', '').str.replace(',', '')

# calculando a media usando a função mean()
media = df['Number of Movies'].mean()

print(f'A média do número de filmes é: {media:.2f}')
