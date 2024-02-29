'''

Questão 5 -  Crie uma classe chamada “Pessoa” com atributos “nome” e “idade”. 
Implemente um método chamado “falar” que imprime uma mensagem com o nome da pessoa.

Aluno: Danilo Pereira Viana - P2-B

'''

class Pessoa: # Cria a classe Pessoa

    # Com o construtor, define os seguintes atributos (nome, idade)
    def __init__(self, nome, idade):

        self.nome = nome
        self.idade = idade


    def falar(self): # Cria a função 'falar'
    
        # Imprime as informações
        return print(f"Olá {self.nome} com idade de {self.idade} anos")
    

pessoa_1 = Pessoa("Carlos", 18) # Cria o objeto 'conta_1' com atributo do titular
pessoa_1.falar() # Chama a função 'falar' 

# FIM!