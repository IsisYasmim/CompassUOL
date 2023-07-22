def processar_notas(nome, notas):
    # Convertendo as notas para uma lista de inteiros
    notas_int = list(map(int, notas.split(',')))
    # Obtendo as três maiores notas em ordem decrescente
    tres_maiores_notas = sorted(notas_int, reverse=True)[:3]
    # Calculando a média das três maiores notas
    media = round(sum(tres_maiores_notas) / 3, 2)
    return f"Nome: {nome} Notas: {tres_maiores_notas} Média: {media}"


if __name__ == '__main__':
    with open('estudantes.csv', 'r') as file:
        linhas = file.read().splitlines()

    relatorios = []
    for linha in linhas:
        nome, notas = linha.split(',', 1)
        relatorio = processar_notas(nome, notas)
        relatorios.append(relatorio)

    relatorios_ordenados = sorted(relatorios)

    for relatorio in relatorios_ordenados:
        print(relatorio)
