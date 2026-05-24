# metodos da classe para manter a classe
class camera():
    def __init__(self, nome, filmando=False):
        self.nome= nome 
        self.filmando = filmando
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} ja estar filmando')
            return        
        print(f'{self.nome} estar filmando')
        self.filmando = True
    def parar_de_filmar(self):
        if not self.filmando:
            print(f'{self.nome} nao estar filmando')
            return
        print(f'{self.nome} parou de filmar')
        self.filmando = False
    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} precisa parar de filmar')
            return
        print(f'{self.nome} fotografou')
c1 = camera('PocoX5Pro')
c1.filmar()
c1.filmar()
c1.parar_de_filmar()
c1.parar_de_filmar()
c1.fotografar()
c1.fotografar()