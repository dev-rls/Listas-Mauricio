''' 3. Conta Consoantes: Implemente uma função conta_consoantes(texto) que conta o 
número de consoantes em uma string. '''
texto = input("Digite uma frase: ")

def conta_consoantes(texto):
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTWXYZ"
    contador=0
    for char in texto:
        if char in consoantes:
            contador += 1
    return contador
print("A frase possui:",conta_consoantes(texto), "consoantes")


