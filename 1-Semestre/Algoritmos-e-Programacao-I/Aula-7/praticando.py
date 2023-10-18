def atualiza_preco(valor):
    return valor + (valor * 0.1)


def taxa(valor):
    return valor * 0.025


def main():
    valor_produto = float(input())
    valor_atualizado = atualiza_preco(valor_produto)
    valor_da_taxa = taxa(valor_atualizado)
    print("%.2f" % valor_atualizado)
    print("%.2f" % valor_da_taxa)


main()
