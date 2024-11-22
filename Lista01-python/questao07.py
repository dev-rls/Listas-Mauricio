''' 7. Crie uma função conta_vogais(texto) que retorne o número de vogais em uma string. '''
texto = input("Digite uma frase: ")
def conta_vogais(texto):
    vogais = 'aeiouAEIOUáé'
    return sum (1 for char in texto if char in vogais)
print(conta_vogais(texto))
