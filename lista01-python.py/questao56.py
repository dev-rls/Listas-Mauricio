# 56. Crie uma função gera_fibonacci_lista(n) que gera uma lista com os n primeiros números de Fibonacci.
def gera_fibonacci_lista(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# Teste
print(gera_fibonacci_lista(5)) # Saída: [0, 1, 1, 2, 3]
