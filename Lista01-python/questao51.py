# 51. Crie uma função verifica_ano_bissexto(ano) que retorna True se o ano for bissexto.
def verifica_ano_bissexto(ano):
    return (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))

# Teste
print(verifica_ano_bissexto(2020)) # Saída: True
