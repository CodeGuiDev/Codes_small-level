# crie uma lista com numeros pares de 1 a 10 e imprima na tela 
pares = [n for n in range(10) if n % 2 == 0]
print(pares)
quadrados = [n * n for n in range(10)]
print(quadrados)
lista_palavra = 'maça', 'uva', 'laranja'
tamanho = [len(p) for p in lista_palavra]
print(tamanho)
