'''19. Diagonais de uma Matriz: Implemente uma função diagonais_matriz(matriz) que 
recebe uma matriz quadrada e retorna uma lista contendo os elementos das duas 
diagonais.'''

a = int(input("Insira o 1º valor: "))
b = int(input("Insira o 2º valor: "))
c = int(input("Insira o 3º valor: "))
d = int(input("Insira o 4º valor: "))
e = int(input("Insira o 5º valor: "))
f = int(input("Insira o 6º valor: "))
g = int(input("Insira o 7º valor: "))
h = int(input("Insira o 8º valor: "))
i = int(input("Insira o 9º valor: "))

matriz = [
    [a, b, c],
    [d, e, f],
    [g, h, i]
]
def diagonais_matriz(matriz):
    diagonal_principal = [matriz[i][i] for i in range(len(matriz))]
    diagonal_secundaria = [matriz[i][len(matriz) - 1 - i] for i in range(len(matriz))]
    return diagonal_principal + diagonal_secundaria

print(diagonais_matriz(matriz)) 
