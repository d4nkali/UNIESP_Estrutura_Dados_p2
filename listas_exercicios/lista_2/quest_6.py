'''

Questão 6 - Crie uma classe chamada “Produto” com atributos “nome”, “preco” e “quantidade”. 
Implemente um método chamado “calcular_total” que retorna o valor total do produto (preço * quantidade).

Aluno: Danilo Pereira Viana - P2-B

'''

class Produto:

    def __init__(self, nome, preco, quantidade):

        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):

        valor_total = self.preco * self.quantidade
        return valor_total
    
quant_produto = float(input("Quantas bananas voce quer: "))

produto_1 = Produto("Banana", 3.00, quant_produto)
exebir_total = produto_1.calcular_total()


print(f"O total a ser pago é de: R${exebir_total}")

# FIM!