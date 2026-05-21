"""
Higher order functions HOF
Funções de primeira classe
"""
 
def saudacao(msg, nome):
    return f'{msg}, {nome}'
 
 
def executar_uma_funcao(funcao_que_queremos_executar, *args): # na funçao fazemos empacotamento
    return funcao_que_queremos_executar(*args) # fora da funçao fazemos desempacotamento
 
 
print(executar_uma_funcao(saudacao, "Bom dia", "Fulano"))
print(executar_uma_funcao(saudacao, "Boa noite", "Beltrano")) 