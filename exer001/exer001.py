# Declaraçãode classe
class Gafanhoto:
    def __init__(self):  # metodo contrutor
        self.nome = ""
        self.idede = 0

    #Metodo de intâcia
    def aniversario(self):
        self.idede += 1


    def mesagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idede} anos de idade."

# Declaração de objeto
g1 = Gafanhoto()
g1.nome = "Cassio"
g1.idede = 35
print(g1.mesagem())

g2 = Gafanhoto()
g1.nome = "Jessica"
g2.idede = 32
print(g2.mesagem())

g3 = Gafanhoto()
g2.nome = "Ana"
g3.idede = 35
print(g3.mesagem())






