def multiplicador(*args):
    total = 1
    for numero in args:
       total *= numero 
    return total
mulplication = multiplicador(2,2,2,2,2,2,2,2,2,2,2,2)
print(mulplication)

def primos(numeros):
    muliplipo2 = numeros % 2 == 0
    if muliplipo2:
        return print(f'seu numero {numeros} é par')   
    return print(f'o seu numero {numeros} é impar')
primo1 = primos(2)
primo2 = primos(3)
primo3 = primos(4)
primo4 = primos(5)
print(primos(2))
print(primos(3))
print(primos(4))


