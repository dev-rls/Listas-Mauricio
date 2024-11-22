''' 37. Escreva uma função eh_armstrong(n) que verifica se um número é um número de 
Armstrong.'''

n = int(input("Digite um nº: "))

def eh_armstrong(n):
    num_str = str(n)
    num_digitos = len(num_str)
    soma = sum(int(digito) ** num_digitos for digito in num_str)
    return soma == n

print(eh_armstrong(n))
