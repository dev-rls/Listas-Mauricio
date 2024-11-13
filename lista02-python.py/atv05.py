'''5. Soma dos N primeiros Naturais: Escreva uma função soma_naturais(n) que retorna a 
soma dos N primeiros números naturais.'''

n=int(input("Insira um valor: "))

def soma_naturais(n):
    return sum(range(1, n + 1))

print(soma_naturais(n))
