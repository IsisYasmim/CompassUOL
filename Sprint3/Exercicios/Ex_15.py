"""
Implemente a classe Lampada. A classe Lâmpada recebe um booleano no se
construtor, True se a lâmpada estiver ligada, False caso esteja desligada.
A classe Lampada possuí os seguintes métodos:
"""


class Lampada:

    def __init__(self):
        self.esta_ligada = False

    def liga(self):
        self.esta_ligada = True

    def desliga(self):
        self.esta_ligada = False

    def esta_ligada(self):
        return self.esta_ligada


# Teste da classe Lampada
lampada = Lampada()
lampada.liga()
print("A lâmpada está ligada?", lampada.esta_ligada)

lampada.desliga()
print("A lâmpada ainda está ligada?", lampada.esta_ligada)
