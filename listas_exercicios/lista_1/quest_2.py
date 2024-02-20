# Questão 2 - Crie um programa que determine se um número inserido pelo usuário é par ou ímpar.

# Aluno: Danilo Pereira Viana - P2-B


# Pergunta para o usuário digitar um número e armazena em uma variavel 'numero'
numero = int(input("Digite um número: "))

if numero % 2 == 0: # Se o número for dividido por 2 e o resto igual a zero, então:

    print(f"{numero} é um número par.") # Imprime que o número e informa que ele é par

else: # Senão:

    print(f"{numero} é um número ímpar.") # Imprime que o número e informa que ele é impar

# FIM!