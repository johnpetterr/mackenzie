numero = int(input("Digite os números encerrando com 0: "))
maior, menor = numero

soma = 0

while numero != soma:
    soma += numero

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

    numero = int(input())

print("Soma: %d" % soma)
print("Maior: %d" % maior)
print("Menor: %d" % menor)
