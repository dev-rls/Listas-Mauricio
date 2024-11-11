# 50. Implemente a função torre_hanoi(n, origem, destino, auxiliar) para resolver o problema da Torre de Hanói.
def torre_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mover disco de {origem} para {destino}")
        return
    torre_hanoi(n-1, origem, auxiliar, destino)
    print(f"Mover disco de {origem} para {destino}")
    torre_hanoi(n-1, auxiliar, destino, origem)

# Teste
torre_hanoi(3, 'A', 'C', 'B')

