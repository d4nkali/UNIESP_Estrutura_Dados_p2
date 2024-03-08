class Pilha:

    def __init__(self):
        self.items = []

    def empilhar(self, item):
        self.items = self.items + [item]

    def desempilhar(self):
        if not self.is_vazia():
            item_removido = self.items[-1]
            self.items = self.items[:-1]
            return item_removido
        else:
            print("A pilha está vazia. Não é possível desempilhar.")

    def topo(self):
        if not self.is_vazia():
            return self.items[-1]
        else:
            print("A pilha está vazia. Não há topo para visualizar.")

    def is_vazia(self):
        return len(self.items) == 0

    def tamanho(self):
        return len(self.items)

    def imprimir(self):
        if not self.is_vazia():
            print("Itens da pilha:")
            for item in self.items:
                print(item)
        else:
            print("A pilha está vazia. Não há itens para imprimir.")


# Criando uma pilha e empilhando
            
p1 = Pilha()

p1.empilhar(8)
p1.empilhar(6)
p1.empilhar(7)
p1.empilhar(2)
p1.empilhar(1)
p1.empilhar(4)

p1.imprimir()


"""

# Criando uma pilha, empilhando e visualizando o topo da pilha
p1 = Pilha()

p1.empilhar(8)
p1.empilhar(6)
p1.empilhar(7)
p1.empilhar(2)
p1.empilhar(1)
p1.empilhar(4)

p1.topo()

"""


"""
# Criando uma pilha, empilhando e desempoilhando dados
p1 = Pilha()

p1.empilhar(8)
p1.empilhar(6)
p1.empilhar(7)
p1.empilhar(2)
p1.empilhar(1)
p1.empilhar(4)

p1.desempilhar()

p1.topo()

"""


"""

# Tentando desempenhar uma pilha vazia
p1 = Pilha()

p1.empilhar(2)
p1.empilhar(1)
p1.empilhar(4)

p1.desempilhar()
p1.desempilhar()
p1.desempilhar()
p1.desempilhar()

"""