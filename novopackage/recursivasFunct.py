# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
import sys
sys.setrecursionlimit(1004)

def recursiva(inicio=0, kk=4):# aqui voce passa o inicio do valor e o final dele como acompanhante 

    print(inicio, kk) #printei os dois

    # Caso base
    # if inicio >= fim:
    #     return fi'm

    # Caso recursivo
    # contar até chegar ao final
    # na hora que ele chegar aqui ele vai aumentar 1 para inicio
    if inicio == 100: # quando ele chegar a 100 ele para o codigo, mas como o python tem regras ele para antes provavelmente por conta de limite
        return print(f'seu valor final é {kk} e começou com 0 mas terminou com {inicio}')
    else:
        inicio += 1
    return recursiva(inicio, kk) # aqui 
    

print(recursiva())