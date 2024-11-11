# 82. Escreva uma função dias_entre_datas(data1, data2) que retorne a diferença em dias entre duas datas.
from datetime import datetime

def dias_entre_datas(data1, data2):
    data1 = datetime.strptime(data1, "%d/%m/%Y")
    data2 = datetime.strptime(data2, "%d/%m/%Y")
    return abs((data2 - data1).days)

# Teste para a função dias_entre_datas
def test_dias_entre_datas():
    assert dias_entre_datas("01/01/2024", "10/01/2024") == 9
    assert dias_entre_datas("10/01/2024", "01/01/2024") == 9
    assert dias_entre_datas("01/01/2024", "01/01/2024") == 0
    print("test_dias_entre_datas passou!")
