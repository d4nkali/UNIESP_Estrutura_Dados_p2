"""

Questão 5 -  Implemente uma função que aceite um vetor de números inteiros e remova todos os 
elementos duplicados, retornando o vetor resultante sem duplicatas. 


Aluno: Danilo Pereira Viana - P2-B

"""

vetor = [1, 1, 4, 5, 7, 8, 11, 19, 8, 3, 7, 87]

def rem_dup(vetor):

    vetor_sem_dup = []

    for i in vetor:

        if i not in vetor_sem_dup:

            vetor_sem_dup.append(i)

    return vetor_sem_dup

vetor_sem_dup = rem_dup(vetor)
print("Lista sem valores duplicados:", vetor_sem_dup)