# 52. Escreva uma função soma_diagonais(matriz) que retorne a soma dos elementos das diagonais de uma matriz.
def soma_diagonais(matriz):
    diagonal_principal = sum(matriz[i][i] for i in range(len(matriz)))
    diagonal_secundaria = sum(matriz[i][len(matriz)-i-1] for i in range(len(matriz)))
    return diagonal_principal + diagonal_secundaria

# Teste
print(soma_diagonais([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # Saída: 25

