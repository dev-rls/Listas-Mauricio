'''13. Classe Veículo: Crie uma classe Veiculo com atributos modelo e velocidade. Adicione um método para aumentar a velocidade.'''

class Veiculo:

    def __init__(self, modelo, velocidade=0):

       self.modelo = modelo

       self.velocidade = velocidade
 
    def aumentar_velocidade(self, incremento):

       self.velocidade += incremento
 
# Usando a classe Veículo

veiculo1 = Veiculo('Tesla')

veiculo1.aumentar_velocidade(322)

print(f'Modelo: {veiculo1.modelo}, Velocidade: {veiculo1.velocidade} km/h')