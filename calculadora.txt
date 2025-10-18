def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

def menu():
    print("=== CALCULADORA ===")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

def main():
    while True:
        menu()
        escolha = input("Escolha uma opção (1-5): ")

        if escolha == '5':
            print("Encerrando a calculadora...")
            break

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: entrada inválida. Use números.")
            continue

        if escolha == '1':
            print("Resultado:", somar(num1, num2))
        elif escolha == '2':
            print("Resultado:", subtrair(num1, num2))
        elif escolha == '3':
            print("Resultado:", multiplicar(num1, num2))
        elif escolha == '4':
            print("Resultado:", dividir(num1, num2))
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
