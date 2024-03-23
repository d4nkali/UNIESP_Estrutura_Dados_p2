"""

Questão 6 - Escreva um programa que ordene um vetor de inteiros em ordem decrescente e, 
em seguida, conte quantos números pares e quantos números ímpares existem no vetor ordenado.


Aluno: Danilo Pereira Viana - P2-B

"""

vetor = [1, 1, 4, 5, 7, 8, 11, 19, 8, 3, 7, 87]

def ordenar_decrescente(vetor):

    n = len(vetor)
    for i in range(n):

        for j in range(0, n - i - 1):

            if vetor[j] < vetor[j + 1]:

                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]

def cont_par_impar(vetor):

    par = 0
    impar = 0

    for num in vetor:

        if num % 2 == 0:

            par += 1

        else:

            impar += 1

    return par, impar


ordenar_decrescente(vetor)
num_pares, num_impares = cont_par_impar(vetor)

print("Nessa lista que foi ordenada em ordem decrescente:", vetor, "A quantidade de numeros pares é de:", num_pares, "e a quantidade de numeros impares é de:", num_impares)