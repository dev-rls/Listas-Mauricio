# 54. Crie uma função media_notas(dicionario) que recebe um dicionário de alunos e notas e retorna a média das notas.
def media_notas(dicionario):
    return sum(dicionario.values()) / len(dicionario)

# Teste
print(media_notas({'João': 8, 'Maria': 9, 'Pedro': 7})) # Saída: 8.0

