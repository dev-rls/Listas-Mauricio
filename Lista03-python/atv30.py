'''30. Classe Carro com Combustível: Crie uma classe Carro com os atributos marca e combustivel. Adicione métodos para abastecer e verificar o nível de combustível.'''

class Carro:

    def __init__(self, marca, combustivel=0):
       self.marca = marca
       self.combustivel = combustivel
 
    def abastecer(self, litros):
       self.combustivel += litros
 
    def verificar_combustivel(self):
       print(f'Nível de combustível: {self.combustivel} litros')
 
# Usando a classe Carro
carro1 = Carro('Honda Civic')
carro1.abastecer(50)
carro1.verificar_combustivel()