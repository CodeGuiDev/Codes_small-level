class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._fabricante = None
        self._Motor = None
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, NomeValor):
        self._fabricante = NomeValor 
    
    @property
    def motor(self):
        return self._Motor
    
    @motor.setter
    def motor(self, valormotor):
        self._Motor = valormotor
    
    def printar_tudo(self):
       return self._Motor, self._fabricante


class fabricante:
    def __init__(self, nome):
        self.nome = nome

class motor:
    def __init__(self, nome):
        self.nome = nome
    
    
carro1 = Carro('Fordian')
fabricante1 = fabricante('RENAULT')
motor1 = motor('1.0')
carro1.fabricante = fabricante1
carro1.motor = motor1
print(carro1.nome, carro1.fabricante.nome, carro1.motor.nome)       