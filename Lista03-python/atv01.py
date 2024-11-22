'''1. Classe Pessoa: Crie uma classe Pessoa com os atributos nome e idade.
Instancie um objeto e imprima suas informações. '''
 
class Pessoa:
    def __init__(self, nome, idade):
       self.nome = nome
       self.idade = idade
 
    def imprimir_informacoes(self):
       print(f'Nome: {self.nome}, Idade: {self.idade}')
 
# Instanciando um objeto
pessoa1 = Pessoa('João', 30)
pessoa1.imprimir_informacoes()
 