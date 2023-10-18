modelo_carros = []
litros = []


def entrada_carro():
    for _ in range(4):
        modelo_carros.append(input())

    return modelo_carros


def entrada_consumo():
    for _ in range(4):
        litros.append(int(input()))

    return litros


def economico():
    menor_consumo = min(litros)
    position = litros.index(menor_consumo)
    return modelo_carros[position]


def main():
    entrada_carro()
    entrada_consumo()
    print(economico())


main()
