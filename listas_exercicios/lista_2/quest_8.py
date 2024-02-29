'''

Questão 8 - Crie uma classe chamada “Aluno” com atributos “nome” e “notas”. 
Implemente um método chamado “calcular_media” que retorna a média das notas do aluno.

Aluno: Danilo Pereira Viana - P2-B

'''

class Aluno: # Cria a classe Carro

    def __init__(self, nome, notas): # Com o construtor, define os seguintes atributos (nome, notas)
        
        self.nome = nome
        self.notas = notas

    def calcular_media(self): # Cria a função 'calcular media'

        media = sum(self.notas) / len(self.notas) # Calcula a media e armazena em 'media'
        return media # Quando a função for executada, retorna o valor 'media'

 
aluno_1 = Aluno("Carlos", [7, 6, 9])  # Cria o objeto 'aluno_1' com os atributos definidos
media_aluno_1 = aluno_1.calcular_media() # Chama a função 'calcular media'

# Imprime as informações
print(f"A media do aluno {aluno_1.nome} é {media_aluno_1:.2f}")

# FIM!