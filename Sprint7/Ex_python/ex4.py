import pandas as pd

# lendo o arquivo CSV
df = pd.read_csv('actors.csv')

# contando quantas vezes cada filme aparece
frequencia_filmes = df['#1 Movie'].value_counts()

# criando tuplas com os filmes e sua frequência
lista_filmes = [(filme, frequencia) for filme,
                frequencia in frequencia_filmes.items()]

# ordenando do maior para o menor
lista_filmes.sort(key=lambda x: x[1], reverse=True)

for filme, frequencia in lista_filmes:
    print(f"O filme {filme} aparece {frequencia} vez(es) no dataset")
