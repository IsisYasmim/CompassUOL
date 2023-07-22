def calcular_valor_maximo(operadores, operandos):
    # Zipando os operadores e operandos
    lista_zip = list(zip(operadores, operandos))
    # Utilizando a função eval pois os dados recebidos são seguros
    resultados = map(lambda x: eval(str(x[1][0]) + x[0] + str(x[1][1])),
                     lista_zip)

    # Obtendo o maior valor dentre os resultados usando a função max
    maior_valor = max(resultados)

    return maior_valor


if __name__ == '__main__':
    operadores = ['+', '-', '*', '/', '+']
    operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]

    resultado = calcular_valor_maximo(operadores, operandos)
    print(resultado)
