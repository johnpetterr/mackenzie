def valor_pagamento(valor, dias):
    if dias == 0:
        return valor

    multa = 3 / 100
    juros = dias * (0.1 / 100)

    return valor + ((valor * multa) + (valor * juros))


def main():
    valor = float(input())
    dias = int(input())
    print(valor_pagamento(valor, dias))


main()
