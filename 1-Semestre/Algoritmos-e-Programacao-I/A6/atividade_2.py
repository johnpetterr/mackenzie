numero1, numero2 = 1, 1

for i in range(8):
    print(numero1, end=" ")

    valor = numero1 + numero2
    numero1 = numero2
    numero2 = valor
