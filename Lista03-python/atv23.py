'''23. Classe Funcionário: Crie uma classe Funcionario com os atributos nome e salario. Adicione um método para calcular um aumento de salário.'''

class Funcionario:

    def __init__(self, nome, salario):
       self.nome = nome
       self.salario = salario
 
    def calcular_aumento(self, porc):
       self.salario += self.salario * (porc / 100)
 
# Usando a classe Funcionario
funcionario1 = Funcionario('Abel', 3000)
funcionario1.calcular_aumento(10)
print(f'Novo salário: {funcionario1.salario}')