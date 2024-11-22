'''21. Classe Livro com Estoque: Adicione à classe Livro um atributo para controlar a quantidade em estoque.'''

class Livro:

    def __init__(self, titulo, autor, estoque):
       self.titulo = titulo
       self.autor = autor
       self.estoque = estoque
 
    def exibir_detalhes(self):
       print(f'Título: {self.titulo}, Autor: {self.autor}, Estoque: {self.estoque}')
 
# Usando a classe Livro

livro1 = Livro('A Cabana', 'William P.Young', 20)
livro1.exibir_detalhes()
 