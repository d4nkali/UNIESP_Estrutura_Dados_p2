""" 

Quinto exemplo dos codigos do Google Colaboratory testados em sala de aula do dia 16/02/2024

Automatically generated by Colaboratory.

Original file is located at: 
    https://colab.research.google.com/drive/1E7ppwKPORhJbRboaj5X2wEgWWs7tqJEd

"""

class Produto:
  def __init__(self, nome, descricao, valor):
    self.nome = nome
    self.descricao = descricao
    self.valor = valor

p1 = Produto('Uva', 'Isabel', '6,00')
print(p1.nome, p1.descricao, p1.valor)

p2 = Produto('Maça', 'Argentina', '8,00')
print(p2.nome, p2.descricao, p2.valor)

# FIM!