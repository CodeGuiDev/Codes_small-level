def soma(x):
    def somas(y):
        return x + y
    yield soma

#abrir a mente guilherme
def multiplicacao(x, y):
    return x * y

def cria_funcao(fucao, x): # aqui ele passa uma função(exemplo: fuction soma ou mulltiplica)
    def interna(y):#ele cria uma interna para guarda o x e resgarta o Y so apos de ja ter o X entendeu?
        return fucao(x, y) # aqui ele retorna na fuction "interna" que pega a function que ele escolheu e duas variaves apos ja ttelas
    return interna # e aqui ele retorna a "cria_funçao" por inteiro mas retornando so a interna ja que é o corpo principal
teste = cria_funcao(soma, 5)
print(teste(4))