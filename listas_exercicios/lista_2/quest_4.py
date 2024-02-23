'''

Questão 4 - Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”.
Implemente métodos “depositar” e “sacar” para manipular o saldo.

Aluno: Danilo Pereira Viana - P2-B

'''

class ContaBancaria:

    def __init__(self, titular, saldo = 890.80):

        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):

        if valor > 0:

            self.saldo += valor
            print(f"Depósito no valor de R${valor} realizado. Seu novo saldo é de: R${self.saldo}")

        else:

            print("Valor inválido para o depósito. O valor para o deposito deve ser maior que zero.")

    def sacar(self, valor):

        if valor > 0 and valor <= self.saldo:

            self.saldo -= valor
            print(f"Saque no valor de R${valor} realizado. Seu novo saldo: R${self.saldo}")

        else:

            print("Valor inválido para saque. Verifique se há saldo suficiente ou se o valor para o saque é maior que zero.")

conta1 = ContaBancaria(titular="Lucas")
conta1.depositar(1000)
conta1.sacar(500)

# FIM!