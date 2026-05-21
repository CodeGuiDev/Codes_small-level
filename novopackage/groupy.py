from itertools import groupby
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]
#vote nessa aula revise
alunos_agrupados = sorted(alunos, key=lambda a: a['nota']) #aqui ele faz uma tupla para ordena a lista acima la de alunos
# alunos_agrupadosNome = sorted(alunos, key=lambda a: a['nome']) # uma sorted para ORDENALA por NOME ou NOTA(ABC)
# grupo = groupby(alunos_agrupados, key=lambda a: a['nota']) # aqui o GROUPBY 
# grupo_nomes = groupby(alunos_agrupadosNome, key=lambda a: a['nome'])
 

# for chave, novo in grupo:
#     print(f'alunos com a nota {chave}')
# for bla, nomes in grupo_nomes:
#     for doidos in nomes:
#         print(doidos)
    # for aluno in novo:
    #     print(f'')
for aluno, chave in alunos_agrupados:
     print(aluno)
     print(chave)