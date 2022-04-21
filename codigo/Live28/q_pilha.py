from collections import deque


class Pilha:
    def __init__(self):
        self.lista = deque()

    def insere(self, val):
        self.lista.append(val)

    def remove(self):
        return self.lista.pop()

    def __repr__(self):
        return f"Pilha [{', '.join((str(x) for x in self.lista))}]"
