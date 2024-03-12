"""

Questão 6 - Escreva um programa que cria uma lista de strings e exibe a mais longa palavra da lista.

Aluno: Danilo Pereira Viana - P2-B

"""

# Cria uma lista com frases famosas de filmes
lista_frases = ["Não sei, so sei que foi assim.", "It's Over, Anakin, I Have the High Ground", 
                "Pois um mago nunca se atrasa, nem se adianta, ele chega exatamente quando pretende chegar.", 
                "A primeira regra do clube da luta é não falar sobre o clube da luta."]

maior_frase = "" # Cria uma variavel vazia para armazenar a maior frase

for i in lista_frases: # Intera e cria um loop para descobri a maior frase da lista

    if len(i) > len(maior_frase): # Se achar uma frase que for maior a da variavel 'maior_frase', então:

        maior_frase = i # Adiciona a maior frase na variavel


# Imprime os resultados
print(f"A maior frase da lista é: {maior_frase}")