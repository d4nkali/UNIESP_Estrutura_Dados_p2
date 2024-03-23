"""

Questão 3 - Escreva um programa que encontre o elemento máximo em um vetor de inteiros não ordenado sem 
usar a função `max()`. Em seguida, encontre o elemento mínimo sem usar a função `min()`. 

Aluno: Danilo Pereira Viana - P2-B

"""

vetor = [51, 2, 76, 23, 90, 32, 45, 54, 18] # Cria o vetor com os seguintes elementos

def calc_max(vetor): # Cria a função 'calc_max'

    maximo = vetor[0]

    for i in vetor:

        if i > maximo:

            maximo = i

    return maximo


def calc_min(vetor): # Cria a função 'calc_min'
    
    minimo = vetor[0]

    for j in vetor:

        if j < minimo:

            minimo = j

    return minimo


# Executa as funções
maximo = calc_max(vetor)
minimo = calc_min(vetor)


# Imprime os resultados
print("O maior numero é:", maximo)
print("O menor numero é:", minimo)