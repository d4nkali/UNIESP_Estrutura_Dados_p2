"""

Questão 1 - Escreva uma função em Python para ordenar um vetor de inteiros em ordem crescente
usando o algoritmo de seleção.


Aluno: Danilo Pereira Viana - P2-B

"""

vetor = [5, 2, 9, 1, 6] # Cria uma lista de numeros inteiros

print("Vetor original:", vetor) # Imprime a lista original

n = len(vetor)

for i in range(n - 1):

    indice_menor = i

    for j in range(i + 1, n):

        if vetor[j] < vetor[indice_menor]:

            indice_menor = j

    vetor[i], vetor[indice_menor] = vetor[indice_menor], vetor[i]

print("Vetor ordenado crescente:", vetor) # Imprime a lista ja ordenada