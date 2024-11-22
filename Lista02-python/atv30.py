'''30. Histograma de Ocorrências em Lista: Crie uma função histograma(lista) que recebe 
uma lista e retorna um dicionário com o número de ocorrências de cada elemento da 
lista.'''

def histograma(lista):
    hist = {}
    for item in lista:
        if item in hist:
            hist[item] += 1
        else:
            hist[item] = 1
    return hist

# Solicitando a entrada do usuário
entrada = input("Digite os números separados por espaço: ")

# Convertendo a entrada em uma lista de inteiros
lista = list(map(int, entrada.split()))

# Calculando e imprimindo o histograma
print(histograma(lista))
