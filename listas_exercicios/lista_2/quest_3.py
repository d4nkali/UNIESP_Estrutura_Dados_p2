'''

Questão 3 - Crie uma classe chamada “Retangulo” que tenha atributos “base” e “altura”. 
Implemente um método chamado “calcular_area” que retorna a área do retângulo

Aluno: Danilo Pereira Viana - P2-B

'''

class Retangulo: # Cria a classe circulo

    # Com o construtor, define os seguintes atributos (base, altura)
    def __init__(self, base, altura):

        self.base = base
        self.altura = altura
        
    def calcular_area(self): # Cria a função 'calcular_area'

        area = self.base * self.altura # Define o calculo da área e armazena em uma variavel
        return area # Quando a função for acionada, imprime o valor da área
    
perg_base = float(input("Digite a base do retangulo: ")) # Pergunta a base e armazena em 'perg_base'
perg_altura = float(input("Digite a altura do retangulo:")) # Pergunta a altura e armazena em 'perg_altura'

retangulo_1 = Retangulo(perg_base, perg_altura) # Cria o objeto 'retangulo_1'
area_retangulo = retangulo_1.calcular_area() # Chama a função 'calcular_area'

print() # Espaçamento
print(f"A área do retangulo é de {area_retangulo:.2f}") # Imprime que vai exebir a área

# FIM!