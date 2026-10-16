import math
import sys

historico = []

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    if a < 0:
        raise ValueError("Não é possível calcular raiz quadrada de número negativo.")
    return math.sqrt(a)

def porcentagem(a, b):
    return (a * b) / 100

def obter_numero(mensagem):
    while True:
        try:
            entrada = input(mensagem).strip().replace(',', '.')
            return float(entrada)
        except ValueError:
            print("\033[91mEntrada inválida! Por favor, digite um número válido.\033[0m")

def exibir_menu():
    print("\n" + "=" * 35)
    print("      CALCULADORA PYTHON")
    print("=" * 35)
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Potenciação (^)")
    print("6. Raiz Quadrada (√)")
    print("7. Porcentagem (%)")
    print("8. Ver Histórico")
    print("0. Sair")
    print("=" * 35)

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (0-8): ").strip()

        if opcao == '0':
            print("\nObrigado por usar a calculadora. Até mais!")
            sys.exit(0)

        elif opcao == '8':
            print("\n--- HISTÓRICO DE OPERAÇÕES ---")
            if not historico:
                print("Nenhuma operação realizada ainda.")
            else:
                for i, item in enumerate(historico, 1):
                    print(f"{i}. {item}")
            input("\nPressione ENTER para continuar...")
            continue

        elif opcao in ['1', '2', '3', '4', '5', '7']:
            num1 = obter_numero("Digite o primeiro número: ")
            num2 = obter_numero("Digite o segundo número: ")

            try:
                if opcao == '1':
                    res = somar(num1, num2)
                    op_str = f"{num1} + {num2} = {res}"
                elif opcao == '2':
                    res = subtrair(num1, num2)
                    op_str = f"{num1} - {num2} = {res}"
                elif opcao == '3':
                    res = multiplicar(num1, num2)
                    op_str = f"{num1} * {num2} = {res}"
                elif opcao == '4':
                    res = dividir(num1, num2)
                    op_str = f"{num1} / {num2} = {res}"
                elif opcao == '5':
                    res = potencia(num1, num2)
                    op_str = f"{num1} ^ {num2} = {res}"
                elif opcao == '7':
                    res = porcentagem(num1, num2)
                    op_str = f"{num2}% de {num1} = {res}"

                print(f"\n\033[92mResultado: {res}\033[0m")
                historico.append(op_str)
            except ZeroDivisionError as e:
                print(f"\n\033[91mErro: {e}\033[0m")

        elif opcao == '6':
            num = obter_numero("Digite o número para calcular a raiz quadrada: ")
            try:
                res = raiz_quadrada(num)
                op_str = f"√{num} = {res}"
                print(f"\n\033[92mResultado: {res}\033[0m")
                historico.append(op_str)
            except ValueError as e:
                print(f"\n\033[91mErro: {e}\033[0m")

        else:
            print("\n\033[91mOpção inválida! Escolha um valor entre 0 e 8.\033[0m")

        input("\nPressione ENTER para voltar ao menu...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma interrompido pelo usuário. Até logo!")
        sys.exit(0)
