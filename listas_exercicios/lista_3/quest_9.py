"""

Questão 9 - Escreva um programa que cria duas listas de números inteiros e exibe os números 
que estão presentes em ambas as listas.

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

lista_num_iguais = [] # Cria uma lista vazia para armazenar os números iguais

for i in lista_num: # Intera para encontrar os números iguais das listas

    if i in lista_num_2: # Se o número além de estar em 'lista_num' estiver tambem em 'lista_num_2', então:

        lista_num_iguais += [i] # Adiciona o número a lista


# Imprime o resultado
if lista_num_iguais: # Se tiver números na lista, então:

    print(f"Os números que são iguais nas duas listas são: {lista_num_iguais}")

else: # Se estiver vazia, então:

    print("Não há números iguais nas duas listas.")