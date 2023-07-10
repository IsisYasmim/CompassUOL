class Calculo:
    def soma(self, X, Y):
        print(f'Somando: {X} + {Y} = {X+Y}')

    def subtracao(self, X, Y):
        print(f'Subtraindo: {X} - {Y} = {X-Y}')


if __name__ == '__main__':
    x = 4
    y = 5
    calculo = Calculo()
    calculo.soma(x, y)
    calculo.subtracao(x, y)
