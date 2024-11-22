'''15. Classe Quadrado: Crie uma classe Quadrado com um atributo lado. Adicione métodos para calcular a área e o perímetro.'''

class Quadrado:

    def __init__(self, lado):
        self.lado = lado
 
    def calcular_area(self):
        return self.lado ** 2
 
    def calcular_perimetro(self):
        return 4 * self.lado
 
# Usando a classe Quadrado
quadrado1 = Quadrado(4)
print(f'Área: {quadrado1.calcular_area()}')
print(f'Perímetro: {quadrado1.calcular_perimetro()}')