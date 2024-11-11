# 48. Crie uma função mcd(a, b) que calcule o máximo divisor comum de dois números usando recursão.
def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a % b)

# Teste
print(mcd(48, 18))

