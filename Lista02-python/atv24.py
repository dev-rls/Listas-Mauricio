'''24. Números Primos até N: Escreva uma função numeros_primos(n) que retorna uma lista 
de todos os números primos até um número n dado.'''

n = int(input("Digite um nº: "))

def numeros_primos(n):
    primos = []
    for num in range(2, n + 1):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primos.append(num)
    return primos
    
print(numeros_primos(n))
