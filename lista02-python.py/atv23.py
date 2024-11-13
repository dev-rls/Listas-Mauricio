'''23. Multiplicação de Valores Pares: Implemente uma função multiplica_pares(lista) que 
multiplica todos os números pares em uma lista.'''

a = int(input("Insira o 1º valor: "))
b = int(input("Insira o 2º valor: "))
c = int(input("Insira o 3º valor: "))
d = int(input("Insira o 4º valor: "))
e = int(input("Insira o 5º valor: "))
f = int(input("Insira o 6º valor: "))

lista = [a, b, c, d, e, f]
def multiplica_pares(lista):
    resultado = 1
    for num in lista:
        if num % 2 == 0:
            resultado *= num
    return resultado

print(multiplica_pares(lista))
