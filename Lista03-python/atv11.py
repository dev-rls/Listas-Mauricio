'''11. Classe Conta Bancária: Crie uma classe ContaBancaria com os atributos saldo. Adicione métodos para depositar e sacar dinheiro.'''

class ContaBancaria:

    def __init__(self, saldo=0):
       self.saldo = saldo

    def depositar(self, valor):
       self.saldo += valor
 
    def sacar(self, valor):
       if valor <= self.saldo:
            self.saldo -= valor

       else:
            print('Saldo insuficiente.')
 
# Usando a Conta Bancária

conta = ContaBancaria(1000)

conta.depositar(500)

conta.sacar(200)

print(f'Saldo atual: {conta.saldo}')