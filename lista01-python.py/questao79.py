# 79. Implemente uma função conta_palavras_arquivo(nome_arquivo) que retorne o número total de palavras em um arquivo.
def conta_palavras_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        return len(f.read().split())

# Teste para a função conta_palavras_arquivo
def test_conta_palavras_arquivo():
    ('arquivo_palavras.txt', 'Este é um arquivo com várias palavras.')
    assert conta_palavras_arquivo('arquivo_palavras.txt') == 7
    print("test_conta_palavras_arquivo passou!")
