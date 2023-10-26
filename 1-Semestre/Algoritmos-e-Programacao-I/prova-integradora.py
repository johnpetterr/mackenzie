"""
Prova Integradora - Questões que caíram em minha prova :)
"""
dado = int(input("Digite um número: "))


def code1():
    # Dado = 5
    constante1, constante2 = 34, 76

    if dado % 3 == 0:
        print(dado * constante1 + 5)
    else:
        print(dado + constante2 / 2)


def code2():
    # Dado = 7
    a, b, c, d = 8, 4, 2, 1

    if 1 <= dado <= 5:
        b, d, a, c = a, c, dado, 0
    elif 5 < dado <= 9:
        c, a, b, d = d, (a - b), dado, 3
    else:
        print("Número inválido!")

    print(a, b, c, d, sep=", ")


def code3():
    # Dado = 30
    a, b, c, d = 0, 0, 0, 0

    if dado == 10:
        a, b, c, d = -10, dado, 7, c + a
    elif dado == 20 or dado == 30:
        a, b, c = 6, 4, dado
        d = b * a
    else:
        print("Número inválido!")

    print(a, b, c, d, sep=", ")
