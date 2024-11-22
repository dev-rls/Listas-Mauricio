'''5. Classe Círculo: Crie uma classe Circulo com um atributo raio.

Adicione um método para calcular o perímetro (2πr).'''

import math
 
class Circulo:

    def __init__(self, raio):

        self.raio = raio
 
    def calcular_perimetro(self):

        return 2 * math.pi * self.raio
 
# Instanciando um objeto

circulo1 = Circulo(7)

print(f'Perímetro do círculo: {circulo1.calcular_perimetro()}')
