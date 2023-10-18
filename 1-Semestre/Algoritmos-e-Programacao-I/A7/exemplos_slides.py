def soma(n1, n2):
    return n1 + n2


def subtrair(n1, n2):
    return n1 - n2


def multiplicar(n1, n2):
    return n1 * n2


def dividir(n1, n2):
    return n1 / n2


def menu():
    print(" 1– SOMA\n 2– SUBTRAÇÃO\n 3– MULTIPLICAÇÃO\n 4– DIVISÃO\n 5– PARAR")
    opcao = int(input("ESCOLHA UMA OPERAÇÃO ACIMA: "))

    while opcao < 1 or opcao > 5:
        opcao = int(input("\nOPÇÃO INVÁLIDA. TENTE DE NOVO: "))

    return opcao


def escolha(op, n1, n2):
    resultado = None

    match op:
        case 1:
            resultado = soma(n1, n2)
        case 2:
            resultado = subtrair(n1, n2)
        case 3:
            resultado = multiplicar(n1, n2)
        case 4:
            if n1 != 0 or n2 != 0:
                resultado = dividir(n1, n2)

    return resultado


def entrada(n):
    return float(input(f"NÚMERO {n}: "))


def main():
    while True:
        opcao = menu()
        if opcao == 5:
            break

        print("\nDIGITE 2 NÚMEROS.")
        n1 = entrada(1)
        n2 = entrada(2)

        if escolha(opcao, n1, n2) is None:
            print("NÃO HÁ DIVISÃO POR ZERO.\n")
        else:
            print("RESULTADO: ", escolha(opcao, n1, n2), "\n")


main()
