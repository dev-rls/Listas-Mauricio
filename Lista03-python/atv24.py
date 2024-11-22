'''24. Classe Elevador: Crie uma classe Elevador com atributos andarAtual e totalAndares. Adicione métodos para subir e descer.'''

class Elevador:

    def __init__(self, total_andares):
       self.andar_atual = 0
       self.total_andares = total_andares
 
    def subir(self):
       if self.andar_atual < self.total_andares:
            self.andar_atual += 1

       else:
            print('Já está no último andar.')
 
    def descer(self):
       if self.andar_atual > 0:
            self.andar_atual -= 1

       else:
            print('Já está no térreo.')
 
# Conforme movo (subir ou descer), o andar muda.
elevador = Elevador(10)
elevador.subir()
elevador.subir()
elevador.descer()

print(f'Andar atual: {elevador.andar_atual}')