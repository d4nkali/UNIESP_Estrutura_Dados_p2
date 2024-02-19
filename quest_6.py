# Questão 6 - Escreva um programa que peça um número inteiro positivo ao usuário e calcule o fatorial desse número.

# Aluno: Danilo Pereira Viana - P2-B


# Criando a variavel do fatorial
fatorial = 1
# Pergunta para o usuário digitar um número inteiro positivo e armazena em uma variavel 'numero'
numero = int(input("Digite um número inteiro positivo: "))

if numero == 0 or numero == 1: # Se o numero for 0 ou 1, então

    fatorial = 1 # Define o fatorial como 1

else: # Senão

    # Cria um loop com for onde irá calcular o fatorial e armazenar na variavel 'fatorial'
    for calc in range(1, numero + 1):
        fatorial *= calc

# Imprime o resultado
print(f'O fatorial de {numero} é: {fatorial}')

# FIM!