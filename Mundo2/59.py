
opcao = 0
numero1 = int(input("Digite um numero"))
numero2 = int(input("Digite outro numeor"))

while opcao != 5:
    print("-" * 10, end="")
    print("Calculadora", end="")
    print("-" * 10)
    opcao = int(input("Menu:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos numeros\n[5] Sair\n"))

    if opcao == 1:
        print(f"{numero1} + {numero2} = {numero1 + numero2}")
    elif opcao == 2:
        print(f"{numero1} x {numero2} = {numero1 * numero2}")
    elif opcao == 3:
        print(f"{max(numero2,numero1)} é maior que {min(numero2, numero1)}")
    elif opcao == 4:
        print("Escolha novamente:")
        numero1 = int(input("Digite um numero"))
        numero2 = int(input("Digite outro numeor"))
    elif opcao == 5:
        print("\nAplicação encerrada")
    else:
        print("Opção inválida. Tente de novo")