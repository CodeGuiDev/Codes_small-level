lista_a = [2, 3, 6.8, 9, 7, 6.5]
lista_b = [5, 56, 3.2, 7, 9, 9.6, 8.1]
def soma(lista1, lista2):
    intervalo = min((len(lista_a), len(lista_b)))
    return [lista1[i] + lista2[i] for i in range(intervalo)]
print(soma(lista_a, lista_b))
# zip ele funciona como uniao da duas lista mas quando uma lista nao tem um indice e a outra lista tem entao ele para 
# de utilizar o adiante
#outra solução de uniao de lista usando zip
lista_4 = [ 3, 6.8, 9, 7, 6.5]
lista_3 = [ 56, 3.2, 7, 9, 9.6, 8.1]
novalista = [x + y for x, y in zip(lista_3, lista_4)] #aqui temos ate list compreehension ele pega dois valores que nao 
#existem e faz um nova lista, faz um FOR para que os valores recebam um numero de cada lista.

print(novalista) 