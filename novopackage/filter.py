# filter é nada mais que um filtro funcional ou programaçao funcional
# que seria programaçao mais pura, imutabilidades, sem erros e pequenos
# significado e utilizaçao: Filtra elementos de uma lista com base em uma função (ou condição) que retorna
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def filtrar_preco(produto):#funçao criada e um parametro dito pra receber o filter
    return produto['preco'] > 100


# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 100
# ]
novos_produtos = filter( #filtra uma funçao pode ser ate lambda(funçao anonima e sem valor é usada e feita em uma linha só)
    # lambda produto: produto['preco'] > 100,
    filtrar_preco,# usou a funçao la de cima
    produtos #iterable colocado onde ele vai receber os valores e la emcima vai ter a logica EXE: > 100
)


print_iter(produtos)
print_iter(novos_produtos)