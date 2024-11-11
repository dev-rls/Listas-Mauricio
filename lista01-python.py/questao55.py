# 55. Escreva uma função converte_segundos(h, m, s) que converte horas, minutos e segundos em segundos.
def converte_segundos(h, m, s):
    return h * 3600 + m * 60 + s

# Teste
print(converte_segundos(1, 2, 3)) # Saída: 3723
