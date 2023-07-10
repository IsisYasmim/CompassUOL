import csv

# Lendo o arquivo CSV
with open('actors.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    dados_csv = list(leitor_csv)

# Contando a frequência dos filmes
frequencia_filmes = {}

for linha in dados_csv[1:]:
    filmes = linha[4].split(',')
    for filme in filmes:
        filme = filme.strip()
        if filme in frequencia_filmes:
            frequencia_filmes[filme] += 1
        else:
            frequencia_filmes[filme] = 1

# Encontrando o(s) filme(s) mais frequente(s)
filmes_mais_frequentes = []
frequencia_maxima = max(frequencia_filmes.values())

for filme, frequencia in frequencia_filmes.items():
    if frequencia == frequencia_maxima:
        filmes_mais_frequentes.append(filme)

# Gravando as informações no arquivo "etapa-3.txt"
with open('etapa-4.txt', 'w') as arquivo_txt:
    arquivo_txt.write('O nome do(s) filme(s) mais frequente(s) e sua'
                      ' respectiva frequencia:\n')

    for filme in filmes_mais_frequentes:
        frequencia = frequencia_filmes[filme]
        arquivo_txt.write(f'{filme}: frequencia {frequencia}\n')

print("Informações gravadas com sucesso no arquivo 'etapa-4.txt'.")
