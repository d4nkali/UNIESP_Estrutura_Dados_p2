# Questão 7 - Crie um programa que imprima a sequência de Fibonacci até um valor inserido pelo usuário.

# Aluno: Danilo Pereira Viana - P2-B


# Pergunta para o usuário digitar um número inteiro positivo e armazena em uma variavel 'numero'
numero = int(input("Digite um número limite para a sequência de Fibonacci: "))
list_fib = [0, 1] # Cria uma lista

while list_fib[-1] + list_fib[-2] <= numero: # Ira ficar repetindo até chegar ou ultrapassar 'numero'
    
    result = list_fib[-1] + list_fib[-2] # Fará a logica da sequencia e armazenar o resultado em 'result'
    list_fib.append(result) # Adiciona o número a lista

# Imprime os resultados
print(f"Resultado da Sequência de Fibonacci até o número {numero}: {list_fib}")

# FIM!