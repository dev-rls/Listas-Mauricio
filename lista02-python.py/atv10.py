'''10. Diferença entre Máximo e Mínimo: Crie uma função diferenca_max_min(lista) que 
retorna a diferença entre o maior e o menor elemento de uma lista.'''

a=int(input("Digite o valor um: "))
b=int(input("Digite o valor dois: "))
c=int(input("Digite o valor tres: "))
d=int(input("Digite o valor quatro: "))
e=int(input("Digite o valor cinco: "))

lista = diferenca_max_min =[a,b,c,d,e]

def diferenca_max_min(lista):
    return max(lista) - min(lista)

print(diferenca_max_min(lista))  
#o resultado é a subtração do maior nº da lista menos o menor nº da lista.
