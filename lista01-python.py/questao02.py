'''2. Crie uma função maior(a, b) que receba dois números e retorne o maior entre eles.'''

a = float(input("Digite um nº: "))
b = float(input("Digite outro nº: "))

def maior(a,b):
    if a > b:
        return a
    else:
        return b
if a > b:
    print(a, ",A é maior")
elif a==b:
    print("Números iguais")
else:
    print(b, ",B é maior")

