numero = int(input("Digite um número inteiro e natural: "))
fatorial = 1

while numero < 0:
    numero = int(input("O número informado não é inteiro ou natural. Tente de novo: "))

for i in range(1, numero + 1):
    fatorial *= i

print(numero, fatorial, sep="! = ")
