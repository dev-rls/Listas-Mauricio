'''17. Intercala Listas Ordenadas: Crie uma função intercala_listas_ordenadas(lista1, lista2)
que recebe duas listas ordenadas e retorna uma nova lista intercalada e ordenada.'''

a = int(input("Insira o 1º valor: "))
b = int(input("Insira o 2º valor: "))
c = int(input("Insira o 3º valor: "))
d = int(input("Insira o 4º valor: "))
e = int(input("Insira o 5º valor: "))
f = int(input("Insira o 6º valor: "))

# Criando as listas a partir dos valores de entrada
lista1 = [a, b, c]
lista2 = [d, e, f]

# Função para intercalar listas ordenadas
def intercala_listas_ordenadas(lista1, lista2):
    i, j = 0, 0
    lista_intercalada = []
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            lista_intercalada.append(lista1[i])
            i += 1
        else:
            lista_intercalada.append(lista2[j])
            j += 1
    lista_intercalada.extend(lista1[i:])
    lista_intercalada.extend(lista2[j:])
    return lista_intercalada

# Intercalando e imprimindo as listas
print(intercala_listas_ordenadas(sorted(lista1), sorted(lista2)))
