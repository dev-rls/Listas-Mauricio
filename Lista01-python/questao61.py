# 61. Crie uma função bubblesort(lista) que ordene uma lista usando o algoritmo Bubble Sort.
def bubblesort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Teste para a função bubblesort
def test_bubblesort():
    assert bubblesort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert bubblesort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bubblesort([1]) == [1]
    print("test_bubblesort passou!")
