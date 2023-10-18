quantidade_alunos = int(input())
contador, soma_media = 0, 0

while quantidade_alunos > contador:
    if quantidade_alunos == 0:
        break

    media_alunos = float(input())

    if media_alunos >= 6.0:
        print("PARABÉNS VOCÊ ESTÁ APROVADO")

    soma_media += media_alunos
    contador += 1

if quantidade_alunos != 0:
    media_geral = soma_media / quantidade_alunos
    print(media_geral)
else:
    print("NÃO HOUVE PROCESSAMENTO")
