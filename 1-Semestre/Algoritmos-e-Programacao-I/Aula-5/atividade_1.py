while True:
    print("\n1 - Soma" +
          "\n2 - Subtração" +
          "\n3 - Multiplicação" +
          "\n4 - Divisão" +
          "\n0 - Sair")

    opcao = int(input("Digite a opção desejada: "))
    if opcao == 0:
        break

    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    match opcao:
        case 1:
            print(f"{n1} + {n2} = {n1 + n2}")
        case 2:
            print(f"{n1} - {n2} = {n1 - n2}")
        case 3:
            print(f"{n1} * {n2} = {n1 * n2}")
        case 4:
            print(f"{n1} / {n2} = {n1 / n2}")
        case _:
            print("Opção inválida!")

print("Fim do programa!")
