"""

Questão 4 - Crie uma função que recebe um vetor de números inteiros e retorna o segundo menor número.
Certifique-se de que sua função funcione mesmo se houver números duplicados no vetor.


Aluno: Danilo Pereira Viana - P2-B

"""

vetor = [1, 1, 4, 5, 7, 8, 11, 19] # Cria uma lista com numeros inteiros

def descobrir_seg_menor_num(vetor): # Cria a função 'descobrir_seg_menor_num'

    # Cria 2 variaveis com valores iniciais infinito para armazernar os numeros menores futuramente
    menor_num = float('inf')
    seg_menor_num = float('inf')
    
    for i in vetor: # Cria um loop e incrementa os numeros da lista

        if i < menor_num: # Se a variavel 'menor_num' for menor que o numero na lista

            seg_menor_num = menor_num # Adiciona o numero que estava anteriomente em 'menor_num' a 'seg_menor_num'
            menor_num = i # Adiciona o numero atual a 'menor_num'

        elif i < seg_menor_num and i != menor_num:  # Se o número atual for menor que 'seg_menor_num' e diferente de 'menor_num'

            seg_menor_num = i # Adiciona o numero atual a 'seg_menor_num'
    
    return seg_menor_num # Retorna o valor de 'seg_menor_num'

# Imprime os resultados
print(f"O segundo menor número da lista {vetor} é: {descobrir_seg_menor_num(vetor)}")