# 63. Escreva uma função calcula_juros_compostos(capital, taxa, tempo) que retorne o montante final.
def calcula_juros_compostos(capital, taxa, tempo):
    return capital * (1 + taxa) ** tempo

# Teste para a função calcula_juros_compostos
def test_calcula_juros_compostos():
    assert calcula_juros_compostos(1000, 0.05, 2) == 1102.5
    assert calcula_juros_compostos(500, 0.1, 3) == 665.5
    assert calcula_juros_compostos(100, 0.2, 1) == 120.0
    print("test_calcula_juros_compostos passou!")

