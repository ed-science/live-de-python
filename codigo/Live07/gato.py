class gatinho:
    def __init__(self, nome, cor, idade):
        self.nome = nome
        self.cor = cor
        self.idade = idade
        self.mingal_com_fome = False
        self.rodado = 0

    def miar(self):
        return 'MIAAAUUUUUUUUUUUUU' if self.mingal_com_fome else 'Miau, Miau'

    def andar(self):
        self.rodado += 1
        self.mingal_com_fome = True
        return 'Mingau andando'

    @property
    def velho(self):
        return self.idade > 3

    @property
    def cansado(self):
        return self.rodado > 5

# mingau = gatinho('mingau', 'branco', 2)

# print(mingau.nome)
# print(mingau.cor)
# print(mingau.idade)
# print(mingau.miar())
# print(mingau.miar())

# print(mingau.andar())
# print(mingau.andar())
# print(mingau.andar())
# print(mingau.andar())
# print(mingau.andar())
# print(mingau.andar())
# print(mingau.velho)
# print(mingau.cansado)
