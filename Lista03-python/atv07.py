'''7. Classe Produto: Crie uma classe Produto com os atributos nome e preço. Adicione um método para aplicar um desconto ao preço.'''

class Produto:

    def __init__(self, nome, preco):
       self.nome = nome
       self.preco = preco
 
    def aplicar_desconto(self, porc):
       self.preco -= self.preco * (porc / 100)
 
# Instanciando um objeto

produto1 = Produto('Videogame', 4000)
produto1.aplicar_desconto(10)
print(f'Preço com desconto: {produto1.preco}')