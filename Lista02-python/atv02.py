''' 2. Produto de uma Lista: Escreva uma função produto_lista(lista) que calcula o produto 
(multiplicação) de todos os elementos de uma lista.
 '''
v1 = int(input("Digite o valor 1: "))
v2 = int(input("Digite o valor 2: "))
v3 = int(input("Digite o valor 3: "))
v4 = int(input("Digite o valor 4: "))

lista = produto_lista= [v1,v2,v3,v4]

def produto_lista(lista):
    produto = 1
    for num in lista:
        produto*=num
    return produto

lista=[v1,v2,v3,v4]
print(produto_lista(lista))
