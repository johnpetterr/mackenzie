ano = int(input("Insira o ano para ser analisado: "))

if (ano % 400 == 0 or ano % 4 == 0) and ano % 100 != 0:
    print("O ano %d é bissexto." % ano)
else:
    print("O ano %d não é bissexto." % ano)
