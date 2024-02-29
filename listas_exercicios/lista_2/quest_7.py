'''

Questão 7 -  Crie uma classe chamada “Carro” com atributos “marca”, “modelo” e “ano”. 
Implemente um método chamado “detalhes” que retorna uma string com as informações do carro.

Aluno: Danilo Pereira Viana - P2-B

'''

class Carro: # Cria a classe Carro

    # Com o construtor, define os seguintes atributos (marca, modelo, ano)
    def __init__(self, marca, modelo, ano):

        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self): # Cria a função 'detalhes'

        informacoes = [self.marca, self.modelo, self.ano] # Cria uma lista para armazenar as informações do objeto
        return informacoes # Quando chamar a função, ira retornar a lista


carro_1 = Carro("Fiat", "Uno", "2006") # Cria o objeto 'carro_1' com os atributos definidos

inf_carro_1 = carro_1.detalhes() # Chama a função 'detalhes'
print(inf_carro_1) # Imprime as informações

# FIM!