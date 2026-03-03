def solicitar_quantidade():
    while True:
        try:
            quantidade = int(input("Quantos números deseja ordenar? "))
            if quantidade > 0:
                return quantidade
            else:
                print("Digite um número maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def ler_valores(quantidade):
    dados = []

    for i in range(quantidade):
        while True:
            try:
                valor = int(input(f"Digite o valor {i + 1}: "))
                dados.append(valor)
                break
            except ValueError:
                print("Valor inválido. Digite um número inteiro.")

    return dados


def selection_sort(lista):
    tamanho = len(lista)

    for i in range(tamanho):
        menor_indice = i

        for j in range(i + 1, tamanho):
            if lista[j] < lista[menor_indice]:  # corrigido
                menor_indice = j

        if menor_indice != i:
            lista[i], lista[menor_indice] = lista[menor_indice], lista[i]  # corrigido


def exibir_lista(mensagem, lista):
    print(f"{mensagem}: {lista}")  # corrigido


def programa_principal():
    print("=== Ordenação com Selection Sort ===")

    quantidade = solicitar_quantidade()
    dados = ler_valores(quantidade)

    exibir_lista("Lista antes da ordenação", dados)

    selection_sort(dados)

    exibir_lista("Lista após a ordenação", dados)


if __name__ == "__main__":
    programa_principal()
