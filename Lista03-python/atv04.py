'''4. Classe Livro: Crie uma classe Livro com os atributos titulo e autor.

Adicione um método para exibir os detalhes do livro.'''
 
class Livro:

    def __init__(self, titulo, autor):

       self.titulo = titulo

       self.autor = autor
 
    def exibir_detalhes(self):

       print(f'Título: {self.titulo}, Autor: {self.autor}')
 
# Instanciando um objeto

livro1 = Livro('A Cabana', 'Willian P. Young')

livro1.exibir_detalhes()
 
 