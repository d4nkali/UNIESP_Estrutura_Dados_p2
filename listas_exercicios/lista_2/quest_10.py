'''

Questão 10 - Crie uma classe chamada “Funcionario” com atributos “nome”, “salario” e “cargo”. 
Implemente um método chamado “aumentar_salario” que recebe um valor percentual de aumento e 
atualiza o salário do funcionário.

Aluno: Danilo Pereira Viana - P2-B

'''

class Funcionario: # Cria a classe Funcionario

    # Com o construtor, define os seguintes atributos (nome, cargo, salario)
    def __init__(self, nome, cargo, salario): 
        
        self.nome =nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percent_aumento): # Cria a função 'aumentar_salario' com o atributo 'percent_aumento'

        if percent_aumento <= 0: # Se o percentual do aumento for menor ou igual a zero, então:

            print("Erro. O valor tem que ser maior que 0") # Imprime uma frase de erro

        else: # Senão:

            aumento = self.salario * (percent_aumento / 100) # Calcula o aumento e armazena em 'aumento'
            aumento += self.salario
            return aumento # # Quando chamar a função, ira retornar 'aumento'
        

# Cria o objeto 'funcionario_1' com os atributos definidos
funcionario_1 = Funcionario("Luiz", "Programador", 2100) 
# Imprime o salario antes do aumento
print(f"Valor do funcionario {funcionario_1.nome} antes do aumento: {funcionario_1.salario}") 

# Pergunta ao usuario de quanto sera o aumento e armazena na variavel 'perg_aumento'
perg_aumento = float(input("Digite em quantos porcentos sera o aumento: "))
# Chama a função 'aumentar_salario' usando o percentual armazenado para calcular o aumento e armazena em 'novo_salario'
novo_salario = funcionario_1.aumentar_salario(perg_aumento)

# Imprime os resultados
print(f"O novo salario apos o reajuste é de R${novo_salario:.2f}")

# FIM!