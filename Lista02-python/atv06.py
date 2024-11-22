'''6. Diferença de Conjuntos: Implemente uma função diferenca_conjuntos(lista1, lista2)
que retorna os elementos presentes em lista1 que não estão em lista2.'''

a=int(input("Digite o valor 01: "))
b=int(input("Digite o valor 02: "))
c=int(input("Digite o valor 03: "))
d=int(input("Digite o valor 04: "))

lista1 = [a, b, c, d]
lista2 = [b, d]
def diferenca_conjuntos(lista1, lista2):
    return [item for item in lista1 if item not in lista2]

print(diferenca_conjuntos(lista1, lista2))
