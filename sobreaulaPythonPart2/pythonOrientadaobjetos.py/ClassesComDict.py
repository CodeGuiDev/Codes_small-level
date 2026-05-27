# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados) # ele copia o que tem no dicionario acima (dados)
# p1.nome = 'EITA' # aqui ele altera o parametro nome no valor da variavel pessoa dentro do P1
# print(p1.idade) # aqui dar um print no valor da idade da P1
# p1.__dict__['outra'] = 'coisa' # aqui ele criou outro valor para o P1, num caso adicionou o valor outra > coisa
# p1.__dict__['nome'] = 'EITA' # ja que a variavel existe ele so troca o valor 
# del p1.__dict__['nome'] # com del + nomedavariavel, ele deleta o parametro nome 
print(p1.__dict__) # ele dar um print no dicionario completo P1
# print(vars(p1)) # aqui faz o mesmo doque acima
# print(p1.outra) # deu print no parametro outra
# print(p1.nome) # print no parametro nome 
print(vars(p1)) 
print(p1.nome)