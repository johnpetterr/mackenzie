numero = int(input("Consumo em metros cúbicos: "))

if numero <= 10:
    valor = 7
elif 10 < numero <= 30:
    valor = (numero - 10) * 1 + 7
elif 30 < numero <= 100:
    valor = (numero - 30) * 2 + 27
else:
    valor = (numero - 100) * 5 + 167

print("Valor a pagar: R$ %.2f" % (numero - 11))
