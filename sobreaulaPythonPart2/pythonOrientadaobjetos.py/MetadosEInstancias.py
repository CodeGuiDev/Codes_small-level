# metodos em instancias de classes Python
# hard code: nada mais é que algo que foi inscrito direto no codigo 
class Carro:
    def __init__(self, nomedocarro): # init sempre retorna NONE significa tipagem de dados 
        self.nome = nomedocarro
    def acelerar(self):
       print(f'{self.nome} estar acelerando') 

fusca = Carro('fusca')
print(fusca.nome)
fusca.acelerar() #a classe em si é so um mode (sem dados) entao ela nao sabe nada, so quando passa o self ele funciona 


celta = Carro('celta')
print(celta.nome)
celta.acelerar()