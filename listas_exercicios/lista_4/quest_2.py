"""

Questão 2 - Escreva uma função em Python para ordenar um vetor de inteiros, ele deve receber um parâmetro 
que serve como chave para realizar a ordenação crescente ou decrescente.


Aluno: Danilo Pereira Viana - P2-B

"""

vetor = [5, 2, 9, 1, 6] # Cria uma lista de numeros inteiros

def ordenacao(vetor): # Cria a função "ordenacao"

    print("Vetor original:", vetor)
    # Pergunta a forma que vai ser ordenado
    select_option = int(input("Deseja ordenar de que forma: 1 = Crescente ou 2 = Decrescente: "))

    if select_option == 1: # Se for escolhido a opção 1

        n = len(vetor)

        for i in range(n - 1):

            indice_menor = i

            for j in range(i + 1, n):

                if vetor[j] < vetor[indice_menor]:

                    indice_menor = j

            vetor[i], vetor[indice_menor] = vetor[indice_menor], vetor[i]

        print("Vetor ordenado crescente:", vetor)

    elif select_option == 2: # Se for escolhido a opção 2

        n = len(vetor)

        for i in range(n - 1):

            indice_menor = i

            for j in range(i + 1, n):

                if vetor[j] > vetor[indice_menor]:

                    indice_menor = j

            vetor[i], vetor[indice_menor] = vetor[indice_menor], vetor[i]

        print("Vetor ordenado decrescente:", vetor)

    else: # Senão

        print("Erro")

ordenacao(vetor) # Chama a função "ordenacao"