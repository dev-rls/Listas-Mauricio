# 75. Escreva uma função inverte_dicionario(dic) que inverta as chaves e valores de um dicionário.
def inverte_dicionario(dic):
    return {v: k for k, v in dic.items()}

# Teste para a função inverte_dicionario
def test_inverte_dicionario():
    assert inverte_dicionario({'a': 1, 'b': 2}) == {1: 'a', 2: 'b'}
    assert inverte_dicionario({'x': 5, 'y': 10}) == {5: 'x', 10: 'y'}
    assert inverte_dicionario({'a': 'x', 'b': 'y'}) == {'x': 'a', 'y': 'b'}
    print("test_inverte_dicionario passou!")
