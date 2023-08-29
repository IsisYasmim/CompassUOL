'''
Ex1:
Identifique o ator/atriz com maior número de filmes
e o respectivo número de filmes.
'''

import pandas as pd

# lendo o arquivo csv
df = pd.read_csv('actors.csv')

# fazendo tratamento de dados
df['Actor'] = df['Actor'].str.replace('"', '').str.replace(',', '')

# encontrando o ator/atriz com maior número de filmes
nome_ator = df[df['Number of Movies']
               == df['Number of Movies'].max()]

print("O ator/atriz com o maior número de filmes é "
      f"{nome_ator['Actor'].values[0]} com "
      f"{nome_ator['Number of Movies'].values[0]} filmes.")
