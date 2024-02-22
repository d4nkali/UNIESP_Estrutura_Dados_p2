'''

Questão 1 - Crie uma classe chamada “Circulo” que tenha um atributo “raio”. 
Implemente um método chamado “calc_area” que retorna a área do círculo.

Aluno: Danilo Pereira Viana - P2-B

'''

pi = 3.14159265359 # Define o valor de pi

class Circulo: # Cria a classe circulo

    # Com o construtor, define o atributo raio
    def __init__(self, raio):

        self.raio = raio

    # Cria a função de calcular a área
    def calc_area(self): 

        area = pi * (self.raio ** 2) # Calcula a área do circulo e armazena em 'area'
        return area # Quando chamar a função, retorna o valor de 'area'


pergunta_raio = int(input("Digite o raio do seu circulo: ")) # Pergunta o raio e armazena em uma variavel
circulo = Circulo(pergunta_raio) # Cria o objeto 'circulo'
area_circulo = circulo.calc_area() # Roda a função "calc_area" no objeto 'circulo'

print() # Espaçamento
print(f"A área do círculo com raio {pergunta_raio} é de ≅: {area_circulo:.2f}") # Imprime a área

# FIM!