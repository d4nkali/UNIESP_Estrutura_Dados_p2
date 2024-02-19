# Questão 4 - Crie um programa que leia uma lista de números e exiba o maior e o menor valor da lista.

# Aluno: Danilo Pereira Viana - P2-B


# Importando a biblioteca random
from random import randint

# Criando uma lista vazia
list_numero = []

# Cria um loop com o for 10 vezes
for i in range(10):
    sorteio_numeros = randint(1, 100) # Escolhe um número entre 1 a 100 a armazena em 'sorteio_numeros'
    list_numero.append(sorteio_numeros) # Adiciona o número de 'sorteio_numeros' e adiciona a lista

# Compara e armazena o maior número da lista
list_numero_maior = max(list_numero)
# Compara e armazena o menor número da lista
list_numero_menor = min(list_numero)

# Imprimindo os resultados
print(f"A lista possui esses numeros: {list_numero}")
print(f"O maior número da lista é: {list_numero_maior}")
print(f"O menor número da lista é: {list_numero_menor}")

# FIM!