import csv

# Lendo o arquivo CSV
with open('actors.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    dados_csv = list(leitor_csv)

# Obtendo o ator/atrizes com o maior número de filmes
maior_numero_filmes = 0
ator_maior_numero_filmes = ''

for linha in dados_csv[1:]:
    numero_filmes = int(linha[2])
    if numero_filmes > maior_numero_filmes:
        maior_numero_filmes = numero_filmes
        ator_maior_numero_filmes = linha[0]

# Gravando as informações no arquivo "etapa-1.txt"
with open('etapa-1.txt', 'w') as arquivo_txt:
    arquivo_txt.write(f'{ator_maior_numero_filmes}: {maior_numero_filmes} '
                      'filmes')

print("Informações gravadas com sucesso no arquivo 'etapa-1.txt'.")
