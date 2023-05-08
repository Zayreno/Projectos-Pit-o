class Bebida:

    fria = True

    def servir(self):
        print("A bebida foi servida")

    def beber(self):
        print("A bebida foi bebida")

class Cocacola(Bebida):
    def semAcucar(self):
        print("Servir versão sem açúcar")

class Pepsi(Bebida):
    def semGelo(self):
        print("Servir sem gelo")

class Sumol(Bebida):
    def semLaranja(self):
        print("Servir o de ananás")


cocacola = Cocacola()
pepsi = Pepsi()
sumol = Sumol()


cocacola.semAcucar()
pepsi.semGelo()
sumol.semLaranja()