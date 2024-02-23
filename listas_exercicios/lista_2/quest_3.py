'''

Questão 3 - Crie uma classe chamada “Retangulo” que tenha atributos “base” e “altura”. 
Implemente um método chamado “calcular_area” que retorna a área do retângulo

Aluno: Danilo Pereira Viana - P2-B

'''

class Retangulo:

    def __init__(self, base, altura):

        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        area = self.base * self.altura
        return area
    
perg_base = float(input("Digite a base do retangulo: "))
perg_altura = float(input("Digite a altura do retangulo:"))
retangulo_1 = Retangulo(perg_base, perg_altura)
area_retangulo = retangulo_1.calcular_area()

print()
print(f"A área do retangulo é de {area_retangulo:.2f}")

# FIM!