import json
from exercicioClasse import DADOS, Pessoa, dump


with open(DADOS, "r") as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])
  