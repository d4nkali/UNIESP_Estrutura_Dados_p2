'''

Questão 4 - Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”.
Implemente métodos “depositar” e “sacar” para manipular o saldo.

Aluno: Danilo Pereira Viana - P2-B

'''

class ContaBancaria:  # Cria a classe ContaBancaria

    # Com o construtor, define os seguintes atributos (titular, saldo com valor inicial de 890.90)
    def __init__(self, titular, saldo = 890.80):

        self.titular = titular
        self.saldo = saldo


    def depositar(self, valor): # Cria a função 'depostiar'

        if valor > 0: # Se o valor do deposito for maior que 0, então:

            self.saldo += valor # Adiciona a quantia do deposito ao saldo
            # Imprime a mudança
            print(f"Depósito no valor de R${valor} realizado. Seu novo saldo é de: R${self.saldo}")

        else: # Senão

            # Imprime mensagem de erro
            print("Valor inválido para o depósito. O valor para o deposito deve ser maior que zero.")


    def sacar(self, valor):

        if valor > 0 and valor <= self.saldo:  # Se o valor do saque for maior que 0 e menor ou igual ao saldo, então:

            self.saldo -= valor # Desconta do saldo
            # Imprime a mudança
            print(f"Saque no valor de R${valor} realizado. Seu novo saldo: R${self.saldo}")

        else: # Senão:

            # Imprime mensagem de erro
            print("Valor inválido para saque. Verifique se há saldo suficiente ou se o valor para o saque é maior que zero.")


conta_1 = ContaBancaria(titular="Lucas") # Cria o objeto 'conta_1' com atributo do titular
conta_1.depositar(1000) # Chama a função 'depositar' com valor de 1000
conta_1.sacar(500) # Chama a função 'sacar' com valor de 500

# FIM!