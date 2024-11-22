'''18. Classe Relógio: Crie uma classe Relogio com os atributos hora, minuto e segundo. Adicione um método para exibir o horário no formato HH:MM.'''

class Relogio:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
 
    def exibir_horario(self):
        return f'{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}'
 
relogio1 = Relogio(10, 30, 47)
print(relogio1.exibir_horario())

 