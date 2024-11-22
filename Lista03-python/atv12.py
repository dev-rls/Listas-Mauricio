'''12. Classe Filme: Crie uma classe Filme com os atributos titulo e duracao. Adicione um método para exibir os detalhes.'''

class Filme:

    def __init__(self, titulo, duracao):

       self.titulo = titulo

       self.duracao = duracao
 
    def exibir_detalhes(self):

       print(f'Título: {self.titulo}, Duração: {self.duracao} minutos')
 
# Instanciando um objeto

filme1 = Filme('Vingadores:Ultimato', 168)

filme1.exibir_detalhes()