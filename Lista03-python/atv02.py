'''2. Classe Retângulo: Crie uma classe Retângulo com os atributos largura e altura.
Adicione um método para calcular a área.'''
class Retangulo:
    def __init__(self, largura, altura):
       self.largura = largura
       self.altura = altura
 
    def calcular_area(self):
       return self.largura * self.altura
 
# Instanciando um objeto
retangulo1 = Retangulo(5, 10)
print(f'Área do retângulo: {retangulo1.calcular_area()}')