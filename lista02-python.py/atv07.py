''' 7. Ordenação com Selection Sort: Crie uma função selection_sort(lista) que ordena uma 
lista usando o algoritmo de Selection Sort.'''

a=int(input("Digite o valor um: "))
b=int(input("Digite o valor dois: "))
c=int(input("Digite o valor tres: "))
d=int(input("Digite o valor quatro: "))
e=int(input("Digite o valor cinco: "))

lista = selection_sort =[a,b,c,d,e]

def selection_sort(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

print(selection_sort(lista))
