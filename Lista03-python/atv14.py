'''14. Classe Eletrodoméstico: Crie uma classe Eletrodomestico com os atributos nome e potencia. Adicione um método para ligar o aparelho.'''

class Eletrodomestico:

    def __init__(self, nome, potencia):
       self.nome = nome
       self.potencia = potencia
 
    def ligar(self):
       print(f'{self.nome} está ligado.')
 
# Usando a classe Eletrodoméstico
eletro1 = Eletrodomestico('Microondas', 900)
eletro1.ligar()