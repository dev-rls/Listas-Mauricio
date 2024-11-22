'''29. Intervalo entre Elementos de uma Lista: Implemente uma função 
intervalo_entre_elementos(lista) que calcula o intervalo (diferença) entre o maior e o 
menor valor de uma lista.'''

def intervalo_entre_elementos(lista):
    return max(lista) - min(lista)

# Solicitando a entrada do usuário
entrada = input("Digite os números separados por espaço: ")

# Convertendo a entrada em uma lista de inteiros
lista = list(map(int, entrada.split()))

# Calculando e imprimindo o intervalo entre os elementos
print(intervalo_entre_elementos(lista))
