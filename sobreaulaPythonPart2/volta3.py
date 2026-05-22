#com exercicio
def multiplicador(multipli):
    def multiplicar(numero):
        return numero * multipli
    return multiplicar
du = multiplicador(2)
tri = multiplicador(3)
qua = multiplicador(4)
print(du(4))
print(tri(10))
print(qua(22))