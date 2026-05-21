# map - para mapear dados
from functools import partial
from types import GeneratorType

# def print_iter(iterator):
#     print(*list(iterator), sep='\n')
#     print()


produtos = [
     {'nome': 'Produto 5', 'preco': 10.00},
     {'nome': 'Produto 1', 'preco': 22.32},
     {'nome': 'Produto 3', 'preco': 10.11},
     {'nome': 'Produto 2', 'preco': 105.87},
     {'nome': 'Produto 4', 'preco': 69.90}, ]


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)


aumentar_dez_porcento = partial( #esse partial ele pega uma funçao e vai distrubuindo ela parcialmente,
    #ela vai passando valores aos poucos:
     aumentar_porcentagem,
     porcentagem=1.1
 )

novos_produtos = [
      {**p,# os dois ** faz com que mostre toda a lista na tela
          'preco': aumentar_dez_porcento(p['preco'])}# aqui ele muda especificamente o valor do "preco" usando 
          #variavel que recebeu uma parcialmente uma funçao e executa ela com o round que coloca duas casas decimais ok?
      for p in produtos #aqui é o que o iterator 'p' recebe no caso aqui é os produtos 
  ]
##so que aqui adiante é funcionalidades de reduzir o trabalho do DEV

def muda_preco_de_produtos(produto):
     return {# pega um produto e retorna ele, resumo so facilita escritas e erros 
         **produto,
         'preco': aumentar_dez_porcento(
             produto['preco']
         )
     }


# novos_produtos = list(map(
#     muda_preco_de_produtos,
#     produtos
# ))


# print_iter(produtos)
# print_iter(novos_produtos)

# print(
#     list(map(
#         lambda x: x * 3,
#         [1, 2, 3, 4]
#     ))
# )