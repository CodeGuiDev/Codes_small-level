# o que sao "class"~
# class é um modelo para criar objetos, um objeto é uma instancia de uma classe
class Pessoa:
    def __init__(self, nome, sobrenome, idade): 
        self.nome = nome
        self.idade = idade # oq significa "self"?
        self.sobrenome = sobrenome
        # self é uma referencia para o objeto que esta sendo criado, ele é usado para acessar
# agora vamos criar um objeto da classe Pessoa
pessoa1 = Pessoa("João", 30, "Gustavo") # aqui passamos dois parametros para usar a classe Pessoa, nome e idade
print(pessoa1.nome, pessoa1.sobrenome, pessoa1.idade) # pode ser colocado em mesma linha 
print(pessoa1.idade) 
print(pessoa1.sobrenome)