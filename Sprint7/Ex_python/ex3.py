import pandas as pd

# lendo o arquivo csv
df = pd.read_csv('actors.csv')

# fazendo tratamento de dados
df['Actor'] = df['Actor'].str.replace('"', '').str.replace(',', '')

# encontrando o ator/atriz com maior média por filme
nome_ator = df[df['Average per Movie']
               == df['Average per Movie'].max()]

print("O ator/atriz com o maior média por filme é "
      f"{nome_ator['Actor'].values[0]}")
