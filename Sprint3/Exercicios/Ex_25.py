'''
Crie uma classe Avião que possua os atributos modelo, velocidade_maxima, cor e
capacidade.
Ao final, itere pela lista imprimindo cada um dos objetos no seguinte formato:
“O avião de modelo “x” possui uma velocidade máxima de “y”, capacidade para
“z” passageiros e é da cor “w”.
Sendo x, y, z e w cada um dos atributos da classe “Avião”.
Valores de entrada:
modelo BOIENG456: velocidade máxima 1500 km/h: capacidade para 400
passageiros: Cor Azul
modelo Embraer Praetor 600: velocidade máxima 863km/h: capacidade para 14
passageiros: Cor Azul
modelo Antonov An-2: velocidade máxima de 258 Km/h: capacidade para 12
passageiros: Cor Azul

'''


class Avião:
    def __init__(self, modelo, velocidade_maxima, capacidade, cor='Azul'):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.cor = cor
        self.capacidade = capacidade


if __name__ == '__main__':
    aviões = []

    avião1 = Avião("BOIENG456", "1500 Km/h", "400 passageiros")
    aviões.append(avião1)

    avião2 = Avião("Embraer Praetor 600", "863 Km/h", "14 passageiros")
    aviões.append(avião2)

    avião3 = Avião("Antonov An-2", "258 Km/h", "12 passageiros")
    aviões.append(avião3)

    # Iterando pela lista e imprimindo os objetos
    for avião in aviões:
        print(f'O avião de modelo {avião.modelo} possui uma velocidade máxima '
              f'de {avião.velocidade_maxima}, capacidade para '
              f'{avião.capacidade} e é da cor {avião.cor}.')
