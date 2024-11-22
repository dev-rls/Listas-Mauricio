'''10. Classe Temperatura: Crie uma classe Temperatura com um método para converter graus Celsius para Fahrenheit.'''

class Temperatura:

    def celsius_para_fahrenheit(self, celsius):
       return (celsius * 9/5) + 32
 
temp = Temperatura()
print(f'35°C em Fahrenheit: {temp.celsius_para_fahrenheit(35)}')