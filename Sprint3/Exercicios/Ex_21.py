class Passaro:
    def voar(self):
        classe = type(self).__name__
        print(f"{classe}")
        print("Voando...")

    def emitir_som(self):
        classe = type(self).__name__
        print(f"{classe} emitindo som...")


class Pato(Passaro):
    def emitir_som(self):
        super().emitir_som()
        print("Quack Quack")


class Pardal(Passaro):
    def emitir_som(self):
        super().emitir_som()
        print("Piu Piu")


if __name__ == '__main__':
    # Testando as classes
    pato = Pato()
    pato.voar()
    pato.emitir_som()

    pardal = Pardal()
    pardal.voar()
    pardal.emitir_som()
