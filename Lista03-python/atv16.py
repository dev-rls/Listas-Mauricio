'''16. Classe Pessoa com Cumprimento: Crie uma classe Pessoa com um método para cumprimentar outra pessoa (imprimir "Olá, [nome]").'''

class Pessoa:

    def __init__(self, nome):
        self.nome = nome
 
    def cumprimentar(self, outra_pessoa):
        print(f'Olá, {outra_pessoa.nome}!')
 
pessoa1 = Pessoa('Jamily')
pessoa2 = Pessoa('Eduarda')
pessoa1.cumprimentar(pessoa2)
