'''9. Classe Aluno: Crie uma classe Aluno com atributos nome e nota. Adicione um método que exiba se o aluno está aprovado (nota >= 7).'''

class Aluno:

    def __init__(self, nome, nota):
       self.nome = nome
       self.nota = nota
 
    def verificar_aprovacao(self):
       if self.nota >= 7:
            print(f'{self.nome} está aprovada.')

       else:
            print(f'{self.nome} está reprovada.')
 
# Instanciando um objeto
aluno1 = Aluno('Raquel', 8.5)
aluno1.verificar_aprovacao()