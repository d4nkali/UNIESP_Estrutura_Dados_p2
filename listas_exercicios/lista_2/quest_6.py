'''

Questão 6 - Crie uma classe chamada “Produto” com atributos “nome”, “preco” e “quantidade”. 
Implemente um método chamado “calcular_total” que retorna o valor total do produto (preço * quantidade).

Aluno: Danilo Pereira Viana - P2-B

'''

class Produto:  # Cria a classe Produto

    # Com o construtor, define os seguintes atributos (nome, preco, quantidade)
    def __init__(self, nome, preco, quantidade): 

        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self): # Cria a função 'calcular_total'

        valor_total = self.preco * self.quantidade # Calcula o total e armazena em 'valor_total'
        return valor_total # Quando chamar a função, ira retornar o 'valor_total'
    

# Pergunta a qunatidade do produto e armazena em uma variavel
quant_produto = float(input("Quantas bananas voce quer: ")) 


produto_1 = Produto("Banana", 3.00, quant_produto) # Cria o objeto 'produto_1' com os atributos definidos
exebir_total = produto_1.calcular_total() # Chama a função 'calcular_total'


# Imprime as informações
print(f"O total a ser pago é de: R${exebir_total}")

# FIM!