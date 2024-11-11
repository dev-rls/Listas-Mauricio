'''6. Escreva uma função soma_lista(lista) que receba uma lista de números e retorne a 
soma de todos os elementos''' 
a = float(input("Digite um nº: "))
b = float(input("Digite outro nº: "))
c = float(input("Digite mais um nº: "))

lista = soma_lista= [a, b, c]

def soma_lista(lista):
    soma=0
    for numero in lista:
        soma = + numero
        return soma
print(lista)
print(sum(lista))
