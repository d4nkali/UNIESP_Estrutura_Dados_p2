"""

Questão 5 - Escreva um programa que cria uma lista de palavras e exibe a quantidade de palavras
que começam com a letra 'A'.

Aluno: Danilo Pereira Viana - P2-B

"""

# Cria a lista com os nomes
lista_nomes = ["Arnaldo", "Cleiton", "Akira", "Osvaldo", "Senna", "Fábio", "Danilo"]

cont_a = 0 # Cria um contador vazio

for i in lista_nomes: # Intera para contar quantos nomes tem na lista

    if i[0].upper() == "A": # Se o nome começar com 'A', então:

        cont_a += 1 # Adicionar mais 1 no contador


# Imprime os resultados
print(f"A lista {lista_nomes} possui {cont_a} nomes que começam com 'A'.")