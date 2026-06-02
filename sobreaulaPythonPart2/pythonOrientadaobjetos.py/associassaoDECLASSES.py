# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.
class Escritor: # aqui nois criamos uma classe escritor
    def __init__(self, nome) -> None:
        self.nome = nome # recebe um nome e uma ferramenta onde ja é none 
        self._ferramenta = None

    @property # usamos getter para receber o valor da ferramenta NONE
    def ferramenta(self):
        return self._ferramenta
 
    @ferramenta.setter
    def ferramenta(self, ferramenta): #aqui receber o getter e ja troca valor para ferramenta que digitariamos abaixo
        print(self.ferramenta) 
        self._ferramenta = ferramenta
       


class FerramentaDeEscrever: 
    def __init__(self, nome):
        self.nome = nome # nome da ferramenta

    def escrever(self): # se a ferramenta estar escrevendo ou nao 
        return f'{self.nome} está escrevendo'


escritor = Escritor('Luiz') 
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Máquina')
escritor.ferramenta = maquina_de_escrever

print(caneta.escrever())
print(maquina_de_escrever.escrever())
print(escritor.ferramenta.escrever())