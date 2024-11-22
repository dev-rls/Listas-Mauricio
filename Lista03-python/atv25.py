'''25. Classe Pessoa com IMC: Crie uma classe Pessoa com atributos altura e peso.

Adicione um método para calcular o IMC (peso / altura²).'''

class Pessoa:

    def __init__(self, nome, altura, peso):

       self.nome = nome

       self.altura = altura

       self.peso = peso
 
    def calcular_imc(self):

       imc = self.peso / (self.altura ** 2)

       print(f'IMC de {self.nome}: {imc:.2f}')
 
# O IMC ideal para uma pessoa é entre 18,5 e 24,9.

pessoa1 = Pessoa('Raquel', 1.62, 56)

pessoa1.calcular_imc()