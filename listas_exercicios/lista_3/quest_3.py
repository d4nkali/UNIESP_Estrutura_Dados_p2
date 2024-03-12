"""

Questão 3 - Escreva um programa que cria uma lista de números inteiros e exibe a soma de todos os números da lista.


Aluno: Danilo Pereira Viana - P2-B

"""

# Importa a função randint e apelida de 'r'
from random import randint as r

max_random =r(1, 10) # Aleatoriza o número maximo da lista

lista_num = list(range(1, max_random)) # Cria uma lista com numeros inteiros

soma_lista_num = 0 # Cria uma variavel zerada para armazenar a soma dos números

for i in lista_num: # Intera para encontrar somar os número da lista

    soma_lista_num += i # Vai somando os numeros da lista em 'soma_lista_num'


# Imprime o resultado
print(f"A soma dos números da lista {lista_num} é: {soma_lista_num}")