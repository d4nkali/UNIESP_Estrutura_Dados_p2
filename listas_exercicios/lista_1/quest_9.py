# Questão 9 - Escreva um programa que leia uma lista de nomes e retorne uma nova lista com apenas os nomes que começam com a letra 'A.

# Aluno: Danilo Pereira Viana - P2-B


# Pergunta para o usuário digitar varios nomes e armazena em uma lista
list_nomes = input("Digite os nomes separados por espaço: ").split()

# Filtra os nomes que começam com 'A'
list_nomes_a = [nome for nome in list_nomes if nome.startswith('A')]

if list_nomes_a: # Se tiver nomes na lista de nomes que começa com 'A'

    # Imprime a lista com nomes que começam com 'A'
    print(f"Nomes que começam com a letra 'A': {list_nomes_a}")

else:

    print("Nenhum nome encontrado que comece com a letra 'A'")

#FIM !