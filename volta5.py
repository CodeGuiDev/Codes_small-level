perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
sair = 'nada' 
resposta = ''
acertos = 0
while sair not in 'sair':
    for pergunta in perguntas:
        print(pergunta['Pergunta'])
        print()
        for i, opcao in enumerate(pergunta['Opções']):
            print(f'{i}) {opcao}'),
        resposta = input('escolha uma opção: ')
        for ponto in pergunta['Resposta']:
            print()
            if resposta == ponto['Resposta' \
            '']:
                acertos += 1
                print()
                print('certa resposta')
            else:
                print('voce errou, para proxima pergunta galera: ')
