def exibir_menu():
    print("Escolha uma opção:")
    print("1. Calcular a soma de dois números")
    print("2. Verificar se um número é par ou ímpar")
    print("3. Imprimir os primeiros N números naturais")
    print("4. Sair")

def calcular_soma():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    soma = num1 + num2
    print(f"A soma de {num1} e {num2} é {soma}")

def verificar_paridade():
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        print(f"O número {num} é par.")
    else:
        print(f"O número {num} é ímpar.")

def imprimir_numeros():
    n = int(input("Digite a quantidade de números naturais a serem impressos: "))
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

def main():
    while True:
        exibir_menu()
        opcao = int(input("Digite a opção desejada: "))
        
        if opcao == 1:
            calcular_soma()
        elif opcao == 2:
            verificar_paridade()
        elif opcao == 3:
            imprimir_numeros()
        elif opcao == 4:
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()