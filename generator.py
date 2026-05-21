def gerador(n=0):
    yield 1 # apos chegar nesse valor, ele pausa, generator == nada mais é que funçao que pausa com 
    #determinado limite que você ompoe.
    print('continuando')
    yield 2 
    print('loucura brasil')
    yield variavel
    print('acabou ?')
    return 'ACabou sim'
minizador = gerador(n=0)
variavel = {
    'papai': 'mamae',
    'nunca': 'amei',
}
print(next(minizador))
print(next(minizador)) 
print(next(minizador)) 
print(next(minizador))
# agora vamos falar sobre 'yield from'
 
