'''22. Classe Agenda: Crie uma classe Agenda com um atributo para armazenar contatos e métodos para adicionar e listar contatos.'''

class Agenda:

    def __init__(self):
       self.contatos = []
 
    def adicionar_contato(self, nome, telefone):
       self.contatos.append({'nome': nome, 'telefone': telefone})
 
    def listar_contatos(self):
       for contato in self.contatos:

            print(f'Nome: {contato["nome"]}, Telefone: {contato["telefone"]}')
 
# Usando a classe Agenda
agenda = Agenda()
agenda.adicionar_contato('Dayane', '1234-5678')
agenda.adicionar_contato('Hugo', '9876-5432')
agenda.listar_contatos()