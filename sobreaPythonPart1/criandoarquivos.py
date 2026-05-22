# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
caminho_arquivo = 'aula116.txt'

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close() 
with open(caminho_arquivo, 'w+') as arquivo: 
    print('Olá mundo')
    print('Arquivo vai ser fechado')
    arquivo.writelines(
        ('Linha 1\n', 'Linha 2\n', 'Linha 3\n')
    )
    arquivo.seek(0) # move o cursor para o início do arquivo

    # lê o conteúdo do arquivo
    print(arquivo.readlines())# quando utiliza o readlines ele lê o arquivo e retorna uma lista com as linhas do arquivo, cada linha é um elemento da lista
    #quando retorna readlines ele vai pro final do cursor, entao se eu quiser ler novamente 
    arquivo.seek(0) 
    print(arquivo.readline(), end='')
# se estiver no WINDOWS, lembresse de usa duas barras invertidas por conta dar barra de escape
# caminho_arquivo = 'C:\\Users\\marce\\Desktop\\aula116.txt'
# ou usar raw string
# caminho_arquivo = r'C:\Users\marce\Desktop\aula116.txt'
# o que esse r' faz? ele diz para o python que aquela string é raw, ou seja, ela é literal, e não tem caracteres de escape