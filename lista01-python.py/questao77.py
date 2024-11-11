# 77. Crie uma função le_arquivo(nome_arquivo) que leia o conteúdo de um arquivo e retorne uma string.
def le_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        return f.read()

# Teste para a função le_arquivo
def test_le_arquivo():
    ('arquivo_teste.txt', 'Conteúdo do arquivo')
    assert le_arquivo('arquivo_teste.txt') == 'Conteúdo do arquivo'
    print("test_le_arquivo passou!")
