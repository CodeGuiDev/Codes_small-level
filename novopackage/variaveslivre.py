#variaves livre + nonlocal
##
def concatenar(string_inicial):
    valorfinal = string_inicial

    def interna(valorparaconcatenar):
        valorfinal += valorparaconcatenar
        return valorfinal
    return interna
c = concatenar('c')
print(c('b'))
print(c('s'))
print(c('d'))