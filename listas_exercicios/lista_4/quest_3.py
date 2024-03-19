"""

Questão 3 - Escreva um programa que encontre o elemento máximo em um vetor de inteiros não ordenado sem 
usar a função `max()`. Em seguida, encontre o elemento mínimo sem usar a função `min()`. 

Aluno: Danilo Pereira Viana - P2-B

"""

# Importa a função randint e apelida de 'r'
from random import randint as r

max_random =r(1, 130) # Aleatoriza o número maximo da lista

lista_num = list(range(1, max_random)) # Cria uma lista com numeros inteiros

lista_num_maior = lista_num[0] # Cria uma variavel para armazenar o maior número
lista_num_menor = lista_num[0] # Cria uma variavel para armazenar o menor número

for i in lista_num: # Intera para encontrar o maior número da lista

    if i > lista_num_maior: # Se encontar um número maior que o que esta em 'lista_num_maior'

        lista_num_maior = i # Adiciona o número a variavel


for j in lista_num: # Intera para encontrar o menor número da lista

    if j <= lista_num_menor: # Se encontar um número menor que o que esta em 'lista_num_menor'

        lista_num_menor = j # Adiciona o numero a variavel


# Imprime o resultado
print(f"O maior número da lista {lista_num} é: {lista_num_maior}")
print(f"O menor número da lista {lista_num} é: {lista_num_menor}")