# Questão 5 - Faça um programa que leia uma lista de números e retorne a média dos números pares

# Aluno: Danilo Pereira Viana - P2-B


# Importando a biblioteca random
from random import randint

# Criando as listas
list_numero = []
list_numero_par = []
# Variavel para contar a quantidade de números pares
quant_par = 0

# Cria um loop com o for 10 vezes
for i in range(10):

    sorteio_numeros = randint(1, 100) # Escolhe um número entre 1 a 100 a armazena em 'sorteio_numeros'
    list_numero.append(sorteio_numeros) # Adiciona o número de 'sorteio_numeros' e adiciona a lista
    
    if (sorteio_numeros % 2) == 0: # Se o número for par, então:
        list_numero_par.append(sorteio_numeros) # Adiciona o número a lista de pares
        quant_par += 1 # Adiciona + 1 a contagem de números pares


if quant_par >= 0: # Se tiver mais de um numero par, então:

    media_numero_par = sum(list_numero_par) / quant_par # Soma os números da lista, divide pela quantidade de numeros pares e armazena em uma variavel

else: # Senão:

    media_numero_par = 0 # Define a media de números pares para 0


# Imprimindo os resultados
print(f"A lista possui esses numeros: {list_numero}")
print(f"Dentre eles, existem {quant_par} números pares: {list_numero_par}")
print(f"A media dos números pares da {media_numero_par:.1f}")

# FIM!