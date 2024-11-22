from calculadora import Calculadora
 
def menu():

    print("Calculadora Simples")

    print("1. Soma")

    print("2. Subtração")

    print("3. Multiplicação")

    print("4. Divisão")

    print("5. Sair")
 
def main():

    calc = Calculadora()

    while True:

        menu()

        escolha = input("Escolha uma operação (1-5): ")

        if escolha == '5':

            print("Saindo...")

            break

        elif escolha in ['1', '2', '3', '4']:

            a = float(input("Digite o primeiro número: "))

            b = float(input("Digite o segundo número: "))

            if escolha == '1':

                resultado = calc.calcular('soma', a, b)

            elif escolha == '2':

                resultado = calc.calcular('subtracao', a, b)

            elif escolha == '3':

                resultado = calc.calcular('multiplicacao', a, b)

            elif escolha == '4':

                resultado = calc.calcular('divisao', a, b)

            print(f'Resultado: {resultado}')

        else:

            print("Escolha inválida. Tente novamente.")
 
if __name__ == "__main__":

    main()

 