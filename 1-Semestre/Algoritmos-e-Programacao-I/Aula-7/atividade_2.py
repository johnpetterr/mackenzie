def multiplo(n1, n2):
    if n1 % n2 == 0:
        return True
    else:
        return False


def entrada():
    return int(input())


def main():
    n1 = entrada()
    n2 = entrada()
    print(multiplo(n1, n2))


main()
