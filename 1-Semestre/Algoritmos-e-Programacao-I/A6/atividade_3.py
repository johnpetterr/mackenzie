serie, numero = 0, 1

for denominador in range(1, 51):
    serie += numero / denominador

    if denominador != 50:
        print(f"{numero} / {denominador} +", end="\n")
    else:
        print(f"{numero} / {denominador} = ", end="")

    numero += 2

print(serie)
