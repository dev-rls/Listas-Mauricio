'''11. Produto Escalar entre Vetores: Implemente uma função produto_escalar(vetor1, 
vetor2) que retorna o produto escalar entre dois vetores (listas de números) de mesmo 
tamanho.'''


vetor1 = list(map(int, input("Digite os valores do vetor 1 separados por espaço: ").split()))
vetor2 = list(map(int, input("Digite os valores do vetor 2 separados por espaço: ").split()))

def produto_escalar(vetor1, vetor2):
    return sum(x * y for x, y in zip(vetor1, vetor2))

print(produto_escalar(vetor1, vetor2))
