import random 
import os 
tentar_novamente = 0
while True:
    opcoes = ['pedra', 'papel', 'tesoura']
    computador = random.choice(opcoes)
    print('bem-vindo ao jogo de pedra, papel e tesoura!')
    minhajogada = input("digite uma jogada(pedra, papel ou tesoura)")


    def jogar(minhajogada, jogadadocomputador):
        if minhajogada == jogadadocomputador:
            return 'empate'
        elif minhajogada == 'pedra' and jogadadocomputador == 'tesoura':
            return 'você ganhou'
        elif minhajogada == 'papel' and jogadadocomputador == 'pedra':
            return 'você ganhou'
        elif minhajogada == 'tesoura' and jogadadocomputador == 'papel':
            return 'você ganhou'
        else:
            return 'você perdeu'
        
    if minhajogada not in opcoes:
        print('jogada inválida, tente novamente')
        tentar_novamente += 1
        if tentar_novamente >= 3:
            print('muitas tentativas, encerrando o jogo')
            break
        continue
    else:
        jogo = jogar(minhajogada, computador)
        print(f'computador jogou {computador}')
        print(jogo)
    
    jogar_novamente = input('deseja jogar novamente? (s/n)')
    if jogar_novamente.lower() != 's':
        break