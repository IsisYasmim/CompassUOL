import csv

# Lendo o arquivo CSV
with open('actors.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    dados_csv = list(leitor_csv)

    # Percorrendo as linhas e fazendo o tratamento
for linha in dados_csv[1:]:
    linha[0] = linha[0].replace('"', '')
    linha[0] = linha[0].replace(',', '')


# Obtendo o ator/atrizes com o maior faturamento
maior_numero_fat = 0
ator_maior_numero_fat = ''

for linha in dados_csv[1:]:
    numero_fat = float(linha[3])
    if numero_fat > maior_numero_fat:
        maior_numero_fat = numero_fat
        ator_maior_numero_fat = linha[0]

# Gravando as informações no arquivo "etapa-3.txt"
with open('etapa-3.txt', 'w') as arquivo_txt:
    arquivo_txt.write(f'{ator_maior_numero_fat}: '
                      f'faturamento {maior_numero_fat}')

print("Informações gravadas com sucesso no arquivo 'etapa-3.txt'.")
