# 44. Implemente uma função potencia_recursiva(base, exp) que calcula a potência de forma recursiva.
def potencia_recursiva(base, exp):
    if exp == 0:
        return 1
    return base * potencia_recursiva(base, exp - 1)

# Teste
print(potencia_recursiva(2, 3)) # Saída: 8
