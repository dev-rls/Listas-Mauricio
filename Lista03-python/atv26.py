'''26. Classe Calculadora com Histórico: Crie uma classe Calculadora com

um histórico de operações realizadas.'''

class Calculadora:

    def __init__(self):

       self.historico = []
 
    def somar(self, a, b):

       resultado = a + b

       self.historico.append(f'Soma: {a} + {b} = {resultado}')

       return resultado
 
    def subtrair(self, a, b):

       resultado = a - b

       self.historico.append(f'Subtração: {a} - {b} = {resultado}')

       return resultado
 
    def exibir_historico(self):

       for operacao in self.historico:

            print(operacao)
 
calc = Calculadora()

calc.somar(10, 5)

calc.subtrair(10, 5)

calc.exibir_historico()