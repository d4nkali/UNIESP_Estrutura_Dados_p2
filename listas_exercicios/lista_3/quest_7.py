"""

Questão 7 - Escreva um programa que cria uma lista de números inteiros e exibe os números pares da lista.

Aluno: Danilo Pereira Viana - P2-B

"""

# Importa a função randint e apelida de 'r'
from random import randint as r

max_random =r(1, 30) # Aleatoriza o número maximo da lista

lista_num = list(range(1, max_random)) # Cria uma lista com numeros inteiros

lista_num_par= [] # Cria uma lista vazia para armazenar os números pares

for i in lista_num: # Intera para encontrar os números pares da lista

    if i % 2 == 0: # Se numero o número for par, então:

        lista_num_par += [i] # Adiciona o número a lista


# Imprime o resultado
print(f"Os números pares da lista {lista_num} são: {lista_num_par}")