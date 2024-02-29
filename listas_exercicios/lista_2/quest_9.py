'''

Questão 9 - Crie uma classe chamada “Triangulo” com atributos “lado1”, “lado2” e “lado3”. 
Implemente um método chamado “calcular_perimetro” que retorna o perímetro do triângulo.

Aluno: Danilo Pereira Viana - P2-B

'''

class Triangulo: # Cria a classe Triangulo

    def __init__(self, lados): # Com o construtor, define o atributo 'lados'
        
        self.lados = lados

    def calcular_perimetro(self): # Cria a função 'calcular_perimetro'

        perimetro = sum(self.lados) # Soma os lados do triangulo e armazena em 'perimetro'
        return perimetro # Quando a função for executada, retorna o valor 'perimetro'
    

triangulo_1 = Triangulo([4, 3, 4]) # Cria o objeto 'triangulo_1' com os atributos definidos
per_trian_1 = triangulo_1.calcular_perimetro() # Chama a função 'calcular_perimetro'

# Imprime os resultados
print(f"A o perimetro desse triangulo com os lados {triangulo_1.lados} é de {per_trian_1}")

# FIM!