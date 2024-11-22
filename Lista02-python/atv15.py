'''15. Multiplicação de Matrizes 2x2: Crie uma função multiplica_matrizes(matriz1, matriz2)
que recebe duas matrizes 2x2 e retorna o resultado da multiplicação entre elas.'''

valores_matriz1 = list(map(int, input("Digite os valores da matriz1 separados por espaço: ").split()))
valores_matriz2 = list(map(int, input("Digite os valores da matriz2 separados por espaço: ").split()))

# Convertendo as listas de valores em matrizes 2x2
matriz1 = [[valores_matriz1[0], valores_matriz1[1]], [valores_matriz1[2], valores_matriz1[3]]]
matriz2 = [[valores_matriz2[0], valores_matriz2[1]], [valores_matriz2[2], valores_matriz2[3]]]

def multiplica_matrizes(matriz1, matriz2):
    resultado = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    return resultado

print(multiplica_matrizes( matriz1, matriz2))
