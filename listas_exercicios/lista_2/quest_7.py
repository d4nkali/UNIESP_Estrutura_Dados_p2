'''

Questão 7 -  Crie uma classe chamada “Carro” com atributos “marca”, “modelo” e “ano”. 
Implemente um método chamado “detalhes” que retorna uma string com as informações do carro.

Aluno: Danilo Pereira Viana - P2-B

'''

class Carro:

    def __init__(self, marca, modelo, ano):

        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):

        informacoes = [self.marca, self.modelo, self.ano]
        return informacoes

carro_1 = Carro("Fiat", "Uno", "2006")

inf_carro_1 = carro_1.detalhes()
print(inf_carro_1)

# FIM!