def conta_vogais(texto: str) -> int:
    # Filtrando apenas os caracteres que são vogais
    vogais = filter(lambda x: x.lower() in 'aeiou', texto)

    # Contando o número de vogais
    numero_vogais = len(list(vogais))

    return numero_vogais


if __name__ == '__main__':
    texto_exemplo = "Oieee, teste"
    resultado = conta_vogais(texto_exemplo)
    print(resultado)
