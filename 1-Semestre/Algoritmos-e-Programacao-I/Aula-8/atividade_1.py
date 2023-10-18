def menu():
    print("(1) Cadastrar um amigo (no final da lista)\n"
          "(2) Mostrar os nomes de todos os amigos\n"
          "(3) Cadastrar um amigo (no inicio da lista)\n"
          "(4) Remover um nome\n"
          "(5) Substituir um nome\n"
          "(6) Mostrar o número total de amigos cadastrados\n"
          "(7) Colocar os nomes dos amigos em ordem alfabética\n"
          "(9) Sair do programa\n")

    opcao = int(input("Opção selecionada: "))
    while opcao < 1 or opcao > 9:
        opcao = int(input("Opção selecionada inválida. Tente de novo: "))

    return opcao


def adicionar_amigo_no_final(lista_amigos):
    nome_amigo = input("\nDigite o nome do seu amigo(a): ")
    lista_amigos.append(nome_amigo)


def mostrar_amigos(lista_amigos):
    print(lista_amigos)


def adicionar_amigo_no_inicio(lista_amigos):
    nome_amigo = input("\nDigite o nome do seu amigo(a): ")
    lista_amigos.insert(0, nome_amigo)


def pegar_posicao(lista_amigos, posicao):
    return lista_amigos.index(posicao)


def remover_amigo(lista_amigos):
    while True:
        try:
            nome_amigo = input("\nDigite o nome do seu amigo(a) que deseja remover: ")
            position = pegar_posicao(lista_amigos, nome_amigo)
            del lista_amigos[position]
            break
        except (IndexError, ValueError):
            print("\nNome não encontrado na lista.")
            sair = input("Deseja parar (1- Sim, 2- Nao)?")
            if sair == "1":
                break


def substituir_nome_amigo(lista_amigos):
    while True:
        try:
            nome_para_substituir = input("\nDigite o nome do amigo que será substituído: ")
            nome_amigo_novo = input("Informe o novo nome do amigo que vai substituir: ")
            posicao = pegar_posicao(lista_amigos, nome_para_substituir)
            lista_amigos[posicao] = nome_amigo_novo
            break
        except (IndexError, ValueError):
            print("\nNome não encontrado na lista.")
            sair = input("Deseja parar (1- Sim, 2- Nao)? ")
            if sair == "1":
                break


def mostra_total_amigos(lista_amigos):
    print("\nTotal de amigos na lista: %d" % len(lista_amigos))


def ordernar_nomes_lista(lista_amigos):
    print(f"\nOrdenação da lista antiga: {lista_amigos}")
    lista_amigos.sort()
    print(f"Ordenação da lista atualizada: {lista_amigos}")


def main():
    lista_amigos = []
    while True:
        option = menu()
        match option:
            case 1:
                adicionar_amigo_no_final(lista_amigos)
            case 2:
                mostrar_amigos(lista_amigos)
            case 3:
                adicionar_amigo_no_inicio(lista_amigos)
            case 4:
                remover_amigo(lista_amigos)
            case 5:
                substituir_nome_amigo(lista_amigos)
            case 6:
                mostra_total_amigos(lista_amigos)
            case 7:
                ordernar_nomes_lista(lista_amigos)
            case 9:
                break


main()
