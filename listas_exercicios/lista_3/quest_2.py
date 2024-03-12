"""

Questão 2 - Escreva um programa que cria uma lista de nomes e exibe o número total de nomes na lista.

Aluno: Danilo Pereira Viana - P2-B

"""

# Cria a lista com os nomes
lista_nomes = ["Arnaldo", "Cleiton", "Akira", "Osvaldo", "Senna", "Fábio", "Danilo"]

cont_lista = 0 # Cria um contador vazio

for i in lista_nomes: # Intera para contar quantos nomes tem na lista

    cont_lista += 1 # Adicionar mais 1 no contador


# Imprime os resultados
print(f"A lista possui {cont_lista} nomes.")