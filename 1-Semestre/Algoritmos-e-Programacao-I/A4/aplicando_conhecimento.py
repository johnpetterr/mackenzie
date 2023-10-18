idade = int(input())

if idade >= 18:
    print("SÊNIOR")
elif idade >= 14:
    print("JUVENIL B")
elif idade >= 11:
    print("JUVENIL A")
elif idade >= 8:
    print("INFANTIL B")
elif idade >= 5:
    print("INFANTIL A")
else:
    print("NÃO TEM IDADE PARA SER ATLETA")
