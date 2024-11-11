''' 8. Implemente uma função inverte_string(s) que retorne a string s invertida. '''
def inverte(nome, sobrenome):
    nomeinverso = sobrenome + "," +nome
    return nomeinverso
nome=input("Nome: ")
sobrenome =input("Sobrenome: ")
invertido = inverte(nome,sobrenome)
print("Olá", invertido)
