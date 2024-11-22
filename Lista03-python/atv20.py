'''20. Classe Pessoa com Altura: Crie uma classe Pessoa que inclua o atributo altura. Adicione um método para verificar se a pessoa 
é mais alta que 1,75 m.'''

class Pessoa:

    def __init__(self, nome, altura):
       self.nome = nome
       self.altura = altura
 
    def verificar_altura(self):
       if self.altura > 1.75:

            print(f'{self.nome} é mais alto(a) que 1,75 m.')

       else:
            print(f'{self.nome} não é mais alto(a) que 1,75 m.')
 
# Usando a classe Pessoa
pessoa1 = Pessoa('Carlos', 1.80)
pessoa1.verificar_altura()
