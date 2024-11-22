'''6. Classe Animal: Crie uma classe Animal com os atributos espécie e som. Adicione um método que imprima o som do animal.'''

class Animal:

    def __init__(self, especie, som):
       self.especie = especie
       self.som = som
 
    def emitir_som(self):
       print(f'O {self.especie} faz "{self.som}"')
 
# Instanciando um objeto

animal1 = Animal('gato', 'miau miau miau miaaau... miau miau miau miau')
animal1.emitir_som()
 
