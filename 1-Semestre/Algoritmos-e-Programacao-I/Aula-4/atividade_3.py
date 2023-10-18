km = float(input("Digite a distância em km: "))
litros = float(input("Digite a quantidade de litros: "))

consumo = km / litros

if consumo < 8:
    print("Venda o carro!")
elif consumo <= 12:
    print("Econômico!")
else:
    print("Super econômico!")
