total = maisde1000 = maisbarato = menorpreco = cont = 0
barato = ''
print('LOJA SUPER BARATÃO')
while True:
    nome = str(input('Nome do Produto: ')).strip()
    preco = int(input('Preço:R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        maisde1000 += 1
    if cont == 1:
        menorpreco = preco
        barato = nome
    else:
        if preco < menorpreco:
            menorpreco = preco
            barato = nome
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
print('Fim do programa ')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maisde1000} custando mais de R$1000.00')
print(f'O produto mais barato é {barato} custando R${menorpreco}')

