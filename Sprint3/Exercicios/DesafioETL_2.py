import csv

# Lendo o arquivo CSV
with open('actors.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    dados_csv = list(leitor_csv)

    # Percorrendo as linhas e fazendo o tratamento
for linha in dados_csv:
    linha[0] = linha[0].replace('"', '')
    linha[0] = linha[0].replace(',', '')

# Gravando as informações no arquivo "etapa-1.txt"
with open('etapa-2.txt', 'w') as arquivo_txt:
    for linha in dados_csv[1:]:
        nome_ator = linha[0]
        media_faturamento = linha[3]
        arquivo_txt.write('A media de faturamento bruto por filme'
                          f' do {nome_ator}: {media_faturamento}\n')

print("Informações gravadas com sucesso no arquivo 'etapa-2.txt'.")
