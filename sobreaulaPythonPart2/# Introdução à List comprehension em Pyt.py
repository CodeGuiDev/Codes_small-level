# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
import pprint
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
# print(list(range(10)))
# print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    for produto in produtos
    if produto['preco'] > 20 and produto['preco'] * 1.05 > 10 
]

# print(novos_produtos)

lista2 = [n for n in range(10) if n <= 5
]
def limpeza(v):
    pprint.pprint(v, sort_dicts=False, width=35)
limpeza(novos_produtos)

