def adiciona_clientes(nome, lista=None):
    if lista is None: # se a lista for None, ou seja, se não for passada como argumento, ele vai criar uma nova lista
        lista = [] # e criou
    lista.append(nome) # e apos isso ela adiciona o nome do cliente na lista
    return lista # retorna a lista com o nome do cliente adicionado e o velho dependendo do caso das variaveis 


cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)