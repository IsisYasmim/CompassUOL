import csv

# Lendo o arquivo CSV
with open('actors.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    dados_csv = list(leitor_csv)

    # Removendo o cabeçalho
    dados_csv = dados_csv[1:]

    # Convertendo o faturamento bruto para float e armazenando em uma lista
    faturamento_bruto = [float(linha[1]) for linha in dados_csv]

    # Obtendo a lista de atores
    atores = [linha[0] for linha in dados_csv]

    # Ordenando os atores pelo faturamento bruto em ordem decrescente
    atores_ordenados = [ator for _,
                        ator in sorted(zip(faturamento_bruto, atores),
                                       reverse=True)]

# Gravando as informações no arquivo "etapa-5.txt"
with open('etapa-5.txt', 'w') as arquivo_txt:
    arquivo_txt.write('Lista de Atores Ordenada por Faturamento Bruto Total '
                      'em ordem decrescente:\n')
    for ator in atores_ordenados:
        arquivo_txt.write(ator + '\n')

print("Informações gravadas com sucesso no arquivo 'etapa-5.txt'.")
