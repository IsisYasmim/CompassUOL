from functools import reduce


def calcula_saldo(lancamentos) -> float:
    # Mapeando os valores para seus sinais (+1 ou -1)
    valores = map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos)

    saldo_final = reduce(lambda acumulado, x: acumulado + x,
                         valores, 0)

    return saldo_final


if __name__ == '__main__':
    lancamentos = [
        (200, 'D'),
        (300, 'C'),
        (100, 'C')
    ]
    resultado = calcula_saldo(lancamentos)
    print(resultado)
