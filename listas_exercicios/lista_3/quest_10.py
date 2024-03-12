"""

Questão 10 - Escreva um programa que cria uma lista de números inteiros e remove todos os números repetidos,
exibindo a lista resultante.

Aluno: Danilo Pereira Viana - P2-B

"""

# Importa a função randint e apelida de 'r'
from random import randint as r

# Aleatoriza o número maximo das listas
max_random = r(1, 30)
max_random_2 = r(8, 42) 

# Cria a 2 listas com numeros inteiros
lista_num = list(range(1, max_random))
lista_num_2 = list(range(8, max_random_2))

lista_num_difer = [] # Cria uma lista vazia para armazenar os números diferentes

for i in lista_num: # Intera para encontrar os números diferentes das listas

    if i not in lista_num_2: # Se o número estiver em 'lista_num', mas não em 'lista_num_2', então:

        lista_num_difer += [i] # Adiciona o número a lista


# Imprime o resultado
if lista_num_difer: # Se tiver números na lista, então:

    print(f"Esses números não se repetem nas duas listas: {lista_num_difer}")

else: # Se estiver vazia, então:

    print("Não há números que se repetem nas duas listas.")