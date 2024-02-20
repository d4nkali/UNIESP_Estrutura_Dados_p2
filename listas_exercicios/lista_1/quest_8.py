# Questão 8 - Faça um programa que determine se um número é primo ou não.

# Aluno: Danilo Pereira Viana - P2-B


# Pergunta para o usuário digitar um número inteiro positivo e armazena em uma variavel 'numero'
numero = int(input("Digite um número inteiro positivo para descobrir se ele é Primo ou não: "))

if numero > 1: # Se 'numero' for maior que 1, então:

    for calc in range(2, numero): # Verifica se o número é primo

        if numero % calc == 0: # Se o 'numero' for dividido por 'calc' e o resto for igual a zero, então:

            print(f"O número {numero} não é primo") # Imprime que não é primo
            break # Encerra o programa

    else: # Senão:

        print(f"O número {numero} é primo") # Imprime que é primo

# FIM!