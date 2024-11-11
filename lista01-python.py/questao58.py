# 58. Escreva uma função conta_maiusculas(texto) que conta o número de letras maiúsculas em um texto.
def conta_maiusculas(texto):
    return sum(1 for char in texto if char.isupper())

# Teste
print(conta_maiusculas("Python É Lindo")) # Saída: 3
