'''28. Classe Banco: Crie uma classe Banco que contenha várias ContaBancaria. 

Adicione um método para listar os saldos de todas as contas.'''

class ContaBancaria:
    def __init__(self, saldo=0):
       self.saldo = saldo
 
class Banco:

    def __init__(self):
       self.contas = []

    def adicionar_conta(self, conta):
       self.contas.append(conta)
 
    def listar_saldos(self):
       for conta in self.contas:

            print(f'Saldo: {conta.saldo}')
 
# Usando a classe Banco
banco = Banco()
conta1 = ContaBancaria(1000)
conta2 = ContaBancaria(2000)

banco.adicionar_conta(conta1)
banco.adicionar_conta(conta2)
banco.listar_saldos()