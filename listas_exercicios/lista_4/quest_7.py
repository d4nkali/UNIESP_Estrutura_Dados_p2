"""

Questão 7 - Crie uma função que aceite um vetor de números inteiros e retorne o terceiro maior número.
Certifique-se de que sua função funcione mesmo se houver números duplicados no vetor.


Aluno: Danilo Pereira Viana - P2-B

"""

vetor = [51, 2, 76, 23, 90, 32, 45, 54, 18]

def descobrir_ter_maior(vetor):

    maior_num = seg_maior = ter_maior = float('-inf')

    for i in vetor:

        if i > maior_num:

            ter_maior = seg_maior
            seg_maior = maior_num
            maior_num = i

        elif i > seg_maior and i != maior_num:

            ter_maior = seg_maior
            seg_maior = i

        elif i > ter_maior and i != maior_num and i != seg_maior:

            ter_maior = i

    return ter_maior


print("O terceiro maior numero da lista ", vetor, "é: ", descobrir_ter_maior(vetor))