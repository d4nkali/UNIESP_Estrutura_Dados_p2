# Questão 1 - Faça um programa que calcule a média de três números inseridos pelo usuário.

# Aluno: Danilo Pereira Viana - P2-B


# Pergunta as notas e armazena em variaveis

nota_1 = int(input("Digite a primeira nota: "))
nota_2 = int(input("Digite a segunda nota: "))
nota_3 = int(input("Digite a terceira nota: "))

# Soma as tres notas, divide pro tres e armazena em uma variavel
nota_f = (nota_1 + nota_2 + nota_3) / 3 

print(f"A media foi de {nota_f:.1f}") # Imprime a nota final

# FIM!