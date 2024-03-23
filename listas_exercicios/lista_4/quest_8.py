"""

Questão 8 - Crie uma função que receba um vetor de números inteiros e retorne a mediana, 
ou seja, o valor do meio quando o vetor é ordenado. Certifique-se de que sua função funcione 
para vetores com um número ímpar de elementos.


Aluno: Danilo Pereira Viana - P2-B

"""

vetor = [51, 2, 76, 23, 90, 32, 45, 54, 18]

def ordenar_lista(vetor):

    n = len(vetor)
    for i in range(n):

        for j in range(0, n-i-1):

            if vetor[j] > vetor[j+1]:

                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]

def calc_mediana(vetor):

    ordenar_lista(vetor)
    meio = len(vetor) // 2

    return vetor[meio]


print("O valor do meio da lista qunado ordenado é: ", calc_mediana(vetor))