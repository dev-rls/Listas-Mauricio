'''26. Ordenação com Merge Sort: Implemente uma função merge_sort(lista) que ordena 
uma lista usando o algoritmo de Merge Sort.'''
def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

    return lista

# Solicitando a entrada do usuário
entrada = input("Digite os números da lista separados por espaço: ")

# Convertendo a entrada em uma lista de inteiros
lista = list(map(int, entrada.split()))

# Ordenando a lista e imprimindo o resultado
print(merge_sort(lista))
