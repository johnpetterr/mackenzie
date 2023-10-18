def maximo(n1, n2):
    if n1 > n2:
        print(n1)
    else:
        print(n2)


def entrada():
    return int(input())


def main():
    n1 = entrada()
    n2 = entrada()
    maximo(n1, n2)


main()
