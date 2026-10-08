import abc 

class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo=0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractclassmethod
    def sacar(self, valor):
        ...
    
    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'(DEPOSITO {valor })')
    
    def detalhes(self, msg=''):
        print(f'o seu saldo é {self.sakdo:2f} {msg}')

class ContaPoupança(Conta):
    def sacar(self, valor):
        valor_pos_saquado = self.saldo - valor

        if valor_pos_saquado >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo
    
    
        print('NAo foi possivel sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO {valor})')
class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, Limite=0):
        super().__init__(agencia, conta, saldo)
        self.Limite = Limite
    
    def sacar(self, valor):
        valor_pos_saquado -= self.saldo - valor
        limite_maximo = -self.Limite

        if valor_pos_saquado >= limite_maximo:
            self.saldo -= valor 
            self.detalhes(f'(SAQUE NEGADO) {valor}')
            return self.saldo 
        
        print('Não foi possível sacar o valor desejado')
        print(f'Seu limite é {-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO {valor})')
        return self.saldo
if __name__ == '__main__':
    cp1 = ContaPoupança(111, 222)
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)
    cp1.sacar(1)
    print('##')
    cc1 = ContaCorrente(111, 222, 0, 100)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(98)
    cc1.sacar(1)
    print('##')