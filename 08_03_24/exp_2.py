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


# Trabalhando com a identificação de uma expressão
expressao = '(a+b)*(a+b)'
for i in expressao:
  print(i)


# Criando um contador
expressao = '(a+b)*(a+b)'
cp=0
for i in expressao:
  if i=='(' or i==')':
    cp+=1
if cp%2==0:
  print('Expressão correta')
else:
  print('Expressão incorreta')


# Criando uma estrutura de pilha para
p1 = Pilha()
expressao = '(a+b))*(a+b)'
for i in expressao:
  if i=='(':
    p1.empilhar(i)

p1.imprimir()


p1 = Pilha()
expressao = '(a+b)*(a+b))'
for i in expressao:
  if i=='(':
    p1.empilhar(i)
for i in expressao:
  if not p1.is_vazia() and i==')':
    p1.desempilhar()
p1.imprimir()


p1 = Pilha()
expressao = '(a+b)*)(a+b)'
for i in expressao:
  if i=='(':
    p1.empilhar(i)
  elif i==')':
    if not p1.is_vazia():
      p1.desempilhar()
    else:
      p1.empilhar('x')
p1.imprimir()


def verifica(expressao):
  p1 = Pilha()
  for i in expressao:
    if i=='(':
      p1.empilhar(i)
    elif i==')':
      if not p1.is_vazia():
        p1.desempilhar()
      else:
        p1.empilhar('x')
  if (p1.is_vazia()):
    return 1
  else:
    return -1
  

expressao = '(a+b)*)(a+b)'
verifica(expressao)


arquivo = open("conjunto1.txt", "r")
linhas = arquivo.readlines()
for linha in linhas:
    print("Expressão Correta" if verifica(linha) == 1 else "Expressão Incorreta", "->", linha)