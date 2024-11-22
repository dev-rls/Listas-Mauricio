
'''3. Classe Carro: Crie uma classe Carro com os atributos marca e ano. 

Adicione um método que exiba essas informações.''' 

class Carro:

    def __init__(self, marca, ano):

       self.marca = marca

       self.ano = ano
 
    def exibir_informacoes(self):

       print(f'Marca: {self.marca}, Ano: {self.ano}')
 
# Instanciando um objeto

carro1 = Carro('Toyota', 2020)

carro1.exibir_informacoes()
 
