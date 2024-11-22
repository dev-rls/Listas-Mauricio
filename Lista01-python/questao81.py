# 81. Crie uma função data_atual() que retorne a data atual no formato "dd/mm/aaaa".
from datetime import datetime

def data_atual():
    return datetime.now().strftime("%d/%m/%Y")

# Teste para a função data_atual
def test_data_atual():
    assert data_atual() == datetime.now().strftime("%d/%m/%Y")
    print("test_data_atual passou!")
