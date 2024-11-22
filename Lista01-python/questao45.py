# 45. Crie uma função somatorio_lista_recursivo(lista) que retorne a soma dos elementos de uma lista recursivamente.
def somatorio_lista_recursivo(lista):
    if not lista:
        return 0
    return lista[0] + somatorio_lista_recursivo(lista[1:])

# Teste
print(somatorio_lista_recursivo([1, 2, 3, 4, 5])) # Saída: 15
