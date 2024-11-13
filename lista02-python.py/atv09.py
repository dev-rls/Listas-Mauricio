'''9. Ordenação com Quick Sort: Escreva uma função quick_sort(lista) que ordena uma lista 
usando o algoritmo de Quick Sort (versão não recursiva).'''

a=int(input("Digite o valor um: "))
b=int(input("Digite o valor dois: "))
c=int(input("Digite o valor tres: "))
d=int(input("Digite o valor quatro: "))
e=int(input("Digite o valor cinco: "))

lista = quick_sort =[a,b,c,d,e]

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    
    stack = [(0, len(lista) - 1)]
    
    while stack:
        start, end = stack.pop()
        pivot_index = partition(lista, start, end)
        
        if pivot_index - 1 > start:
            stack.append((start, pivot_index - 1))
        if pivot_index + 1 < end:
            stack.append((pivot_index + 1, end))
    
    return lista

def partition(lista, start, end):
    pivot = lista[end]
    i = start - 1
    for j in range(start, end):
        if lista[j] <= pivot:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[end] = lista[end], lista[i + 1]
    return i + 1

print(quick_sort(lista))
