'''28. Remove Múltiplos de um Número: Escreva uma função remove_multiplos(lista, n) que 
remove todos os múltiplos de n de uma lista.'''

def remove_multiplos(lista, n):
    return [x for x in lista if x % n != 0]

# Solicitando a entrada do usuário
entrada_lista = input("Digite os números da lista separados por espaço: ")
n = int(input("Digite o valor de n: "))

# Convertendo a entrada em uma lista de inteiros
lista = list(map(int, entrada_lista.split()))

# Removendo os múltiplos de n e imprimindo a lista resultante
print(remove_multiplos(lista, n))

