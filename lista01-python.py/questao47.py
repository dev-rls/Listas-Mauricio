# 47. Implemente uma função conta_ocorrencias_recursiva(lista, elem) que conte o número de ocorrências de um elemento em uma lista de forma recursiva.
def conta_ocorrencias_recursiva(lista, elem):
    if not lista:
        return 0
    return (1 if lista[0] == elem else 0) + conta_ocorrencias_recursiva(lista[1:], elem)

# Teste
print(conta_ocorrencias_recursiva([1, 2, 3, 1, 4], 1)) # Saída: 2
