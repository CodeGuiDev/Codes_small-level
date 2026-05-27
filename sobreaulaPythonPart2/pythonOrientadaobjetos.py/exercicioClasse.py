import json


DADOS = 'dados.json'



class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo 
        self.ano = ano


class Pessoa:
    def __init__(self, nome, carro):
        self.nome = nome
        self.carro = carro    
        
    def Dict(self): 
        return {
            "nome": self.nome,
            "carro": self.carro.__dict__
        }


my_car = Carro("Cardian", 2025)
Guilherme = Pessoa("guilherme", my_car) # so um adento, nao dar pra salvar as classes sem ela ser DICT no arquivo jSON todos valores 
p1 = Pessoa("guilherme", "cardian")
p2 = Pessoa("Joel", "Hordan")
p3 = Pessoa("Farias", "Creta")

bd = [vars(p1), p2.__dict__, vars(p3)]


def dump():
    with open("dados.json", "w", encoding='utf-8') as arquivo_origem:
        json.dump(bd, arquivo_origem,ensure_ascii=False, indent=4)
    
    