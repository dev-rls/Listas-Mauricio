# 60. Implemente uma função filtra_pares(lista) que retorne uma lista apenas com os números pares.
def filtra_pares(lista):
    return [x for x in lista if x % 2 == 0]

# Teste
print(filtra_pares([1, 2, 3, 4, 5, 6])) # Saída: [2, 4, 6]
