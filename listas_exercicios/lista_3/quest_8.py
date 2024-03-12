"""

Questão 8 - Escreva um programa que cria uma lista de números inteiros e exibe os números ímpares da lista.

Aluno: Danilo Pereira Viana - P2-B

"""

# Importa a função randint e apelida de 'r'
from random import randint as r

max_random =r(1, 30) # Aleatoriza o número maximo da lista

lista_num = list(range(1, max_random)) # Cria uma lista com numeros inteiros

lista_num_impar= [] # Cria uma lista vazia para armazenar os números impares

for i in lista_num: # Intera para encontrar os números impares da lista

    if i % 2 != 0: # Se numero o número for impar, então:

        lista_num_impar += [i] # Adiciona o número a lista


# Imprime o resultado
print(f"Os números impares da lista {lista_num} são: {lista_num_impar}")