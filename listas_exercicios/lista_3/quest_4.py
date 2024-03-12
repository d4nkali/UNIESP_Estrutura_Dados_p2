"""

Questão 4 - Escreva um programa que cria uma lista de números inteiros e exibe a média dos números da lista.

Aluno: Danilo Pereira Viana - P2-B

"""

# Importa a função randint e apelida de 'r'
from random import randint as r

max_random =r(1, 10) # Aleatoriza o número maximo da lista

lista_num = list(range(1, max_random)) # Cria uma lista com numeros inteiros

soma_lista_num = 0 # Cria uma variavel zerada para armazenar a soma dos números
cont = 0 # Cria uma variavel para contar

for i in lista_num: # Intera e cria um loop para somar os número da lista

    soma_lista_num += i # Vai somando os numeros da lista em 'soma_lista_num'
    cont += 1 # Adiciona mais um no contador


media_lista_num = soma_lista_num / cont # Calcula a média dos números da lista 

# Imprime o resultado
print(f"A média dos números da lista {lista_num} é: {media_lista_num}")