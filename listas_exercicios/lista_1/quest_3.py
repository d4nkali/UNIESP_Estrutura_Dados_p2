# Questão 3 - Escreva um programa que solicite um número ao usuário e imprima todos os números pares de 0 até esse número.

# Aluno: Danilo Pereira Viana - P2-B


# Pergunta para o usuário digitar um número e armazena em uma variavel 'numero'
numero = int(input("Digite um numero: "))

# Imprime que ira exebir os números pares de 0 até o que o do usúario digitou
print(f"Numeros pares de 0 até {numero}:")

# Cria um loop for que intera os numeros de 0 até o que o do usúario digitou em 'numero'
for numero in range(numero + 1):

    if numero % 2 == 0: # Se o número for dividido por 2 e o resto igual a zero, então:
        
        print(numero) # Imprime esse numero

# FIM!