import math

custo_espetaculo, preco_convite = float(input()), float(input())

convites_lucro = custo_espetaculo * 1.23

quantidade_convites = math.ceil(custo_espetaculo / preco_convite)
quantidade_convites_lucro = math.ceil(convites_lucro / preco_convite)

print(quantidade_convites)
print(quantidade_convites_lucro)
