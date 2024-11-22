# 41. Implemente a função fibonacci(n) que retorna o n-ésimo termo da sequência de Fibonacci.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Teste
print(fibonacci(5)) # Saída: 5
