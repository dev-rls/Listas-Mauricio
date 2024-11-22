'''27. Classe Animal com Movimento: Crie uma classe Animal com um método mover 

que imprima uma mensagem indicando como ele se move (exemplo: "O peixe nada").'''

class Animal:

    def __init__(self, especie, movimento):

       self.especie = especie

       self.movimento = movimento
 
    def mover(self):

       print(f'O {self.especie} {self.movimento}')
 
# Usando a classe Animal

animal1 = Animal('passáro', 'voa')

animal1.mover()