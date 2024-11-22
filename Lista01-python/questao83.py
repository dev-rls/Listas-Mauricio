# 83. Implemente uma função adiciona_dias(data, n) que adicione n dias a uma data e retorne o novo valor.
from datetime import datetime, timedelta

def adiciona_dias(data, n):
    data = datetime.strptime(data, "%d/%m/%Y")
    nova_data = data + timedelta(days=n)
    return nova_data.strftime("%d/%m/%Y")

# Teste para a função adiciona_dias
def test_adiciona_dias():
    assert adiciona_dias("01/01/2024", 10) == "11/01/2024"
    assert adiciona_dias("31/12/2024", 1) == "01/01/2025"
    assert adiciona_dias("01/01/2024", 0) == "01/01/2024"
    print("test_adiciona_dias passou!")

