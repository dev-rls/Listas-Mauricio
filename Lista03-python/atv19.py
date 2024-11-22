'''19. Classe Conversor de Moeda: Crie uma classe ConversorMoeda com um método para converter dólares para reais.'''

class ConversorMoeda:

    def __init__(self, taxa_cambio):

       self.taxa_cambio = taxa_cambio
 
    def converter_para_reais(self, dolares):

       return dolares * self.taxa_cambio
 
# Usando a classe ConversorMoeda
conversor = ConversorMoeda(5.25)  # Exemplo de taxa de câmbio
print(f'200 dólares em reais: {conversor.converter_para_reais(200)}')
