# 62. Implemente uma função valida_senha(senha) que verifique se uma senha atende a requisitos (tamanho, caracteres especiais, etc.).
def valida_senha(senha):
    if len(senha) < 8:
        return False
    if not any(c.isupper() for c in senha):
        return False
    if not any(c.islower() for c in senha):
        return False
    if not any(c.isdigit() for c in senha):
        return False
    if not any(c in "!@#$%^&*()_+" for c in senha):
        return False
    return True

# Teste para a função valida_senha
def test_valida_senha():
    assert valida_senha("Senha123!") == True
    assert valida_senha("senha123") == False
    assert valida_senha("12345678") == False
    assert valida_senha("Senha") == False
    print("test_valida_senha passou!")
