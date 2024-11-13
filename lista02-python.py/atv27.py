'''27. Verifica Ordem Crescente: Crie uma função esta_ordenada(lista) que verifica se uma 
lista está ordenada em ordem crescente.'''

def esta_ordenada(lista):
    return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))

# Solicitando a entrada do usuário
entrada = input("Digite os números da lista separados por espaço: ")

# Convertendo a entrada em uma lista de inteiros
lista = list(map(int, entrada.split()))

# Verificando se a lista está ordenada e imprimindo o resultado
print(esta_ordenada(lista))
