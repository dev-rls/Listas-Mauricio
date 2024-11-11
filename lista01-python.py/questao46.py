# 46. Escreva uma função inverte_string_recursiva(s) que inverta uma string recursivamente.
def inverte_string_recursiva(s):
    if len(s) == 0:
        return s
    return inverte_string_recursiva(s[1:]) + s[0]

# Teste
print(inverte_string_recursiva("python")) # Saída: nohtyp
