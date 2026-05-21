# famoso tenta executar, caso der um erro especifico ou sem comando, ele imprimi o "except"
import sys
platform = 'A minha '
print(sys.platform)
print(platform)
#try:
  #  a = 18 
    # b = 0 
 #   print('linha 1')
    #c = a / b
    #print('linha 2')
#except ZeroDivisionError and NameError:
#    print('nao deu certo viu ')
#


def divide(a, d):
    try:
        return a / d
    except ZeroDivisionError:
        print('ksksks erro de merda viu')

divide(8,0)