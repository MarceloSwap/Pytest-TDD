from calculadora import Calculadora

def menu():
    print("\n=== Calculadora TDD ===")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Sair")

if __name__ == "__main__":
    calc = Calculadora()

    while True:
        menu()
        opcao = input("Escolha a operação: ")

        if opcao == "0":
            print("Saindo...")
            break

        try:
            a = float(input("Digite o primeiro número:"))
            b = float(input("Digite o segundo número: "))

            if opcao == "1":
                print("Resultado:", calc.somar(a, b))
            elif opcao == "2":
                print("Resultado:", calc.subtrair(a, b))
            elif opcao == "3":
                print("Resultado:", calc.multiplicar(a, b))
            elif opcao == "4":
                print("Resultado:", calc.dividir(a, b))
            else:
                print("Opção inválida!")

        except ValueError:
            print("Entrada inválida! Digite apenas números.")
        except ZeroDivisionError as e:
            print("!", e)
