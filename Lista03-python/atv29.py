'''29. Classe Jogo: Crie uma classe Jogo com atributos nome e pontuacao. Adicione métodos para iniciar o jogo e registrar a pontuação.'''

class Jogo:

    def __init__(self, nome):
       self.nome = nome
       self.pontuacao = 0
 
    def iniciar_jogo(self):
       print(f'Iniciando o jogo {self.nome}...')
 
    def registrar_pontuacao(self, pontos):
       self.pontuacao += pontos
 
    def exibir_pontuacao(self):
       print(f'Pontuação: {self.pontuacao}')
 
# Usando a classe Jogo
jogo1 = Jogo('Guitar Hero')
jogo1.iniciar_jogo()
jogo1.registrar_pontuacao(250)
jogo1.exibir_pontuacao()