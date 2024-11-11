# 42. Crie uma função soma_recursiva(n) que soma todos os números de 1 até n recursivamente.
def soma_recursiva(n):
    if n == 0:
        return 0
    return n + soma_recursiva(n-1)

# Teste
print(soma_recursiva(5)) # Saída: 15

