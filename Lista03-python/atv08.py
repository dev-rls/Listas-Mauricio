'''8. Classe Calculadora Simples: Crie uma classe Calculadora com métodos para somar 

e subtrair dois números.'''

class Calculadora:
    def somar(self, a, b):
       return a + b

    def subtrair(self, a, b):
       return a - b
 
# Usando a calculadora

calc = Calculadora()
print(f'Soma: {calc.somar(10, 5)}')
print(f'Subtração: {calc.subtrair(10, 5)}')