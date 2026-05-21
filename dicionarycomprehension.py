KK = {
    'nome': 'CANETA AZUL',
    'preco': 2.5,
    'para': 'escritorio',
}
kk = {
    chave:'kk' or valor     
    if isinstance(valor, float) else valor.upper()
    for chave, valor 
    in KK.items()
}
print(kk)