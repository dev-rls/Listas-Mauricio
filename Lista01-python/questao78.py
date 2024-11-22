# 78. Escreva uma função conta_linhas(nome_arquivo) que retorne o número de linhas de um arquivo.
def conta_linhas(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        return len(f.readlines())

# Teste para a função conta_linhas
def test_conta_linhas():
    ('arquivo_linhas.txt', 'Linha 1\nLinha 2\nLinha 3\n')
    assert conta_linhas('arquivo_linhas.txt') == 3
    print("test_conta_linhas passou!")
