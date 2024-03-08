"""

Questão 1 - Escreva um programa que cria uma lista de números inteiros e exibe o maior número da lista. 

Aluno: Danilo Pereira Viana - P2-B

"""

# Importa a função randint e apelida de 'r'
from random import randint as r

max_random =r(1, 130) # Aleatoriza o número maximo da lista

lista_num = list(range(1, max_random)) # Cria uma lista com numeros inteiros

lista_num_maior = lista_num[0] # Cria uma variavel para armazenar o maior número

for i in lista_num: # Intera para encontrar o maior número da lista

    if i > lista_num_maior: # Se encontar um numero maior que o que esta em 'lista_num_maior'

        lista_num_maior = i # Adiciona o numero a variavel


# Imprime o resultado
print(f"O maior número da lista é: {lista_num_maior}")