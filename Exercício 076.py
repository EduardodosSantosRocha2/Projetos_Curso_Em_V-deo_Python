listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25,
            'Tranferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Caneta', 22.30, 'Livro', 34.90)
print('\033[1m-'*36)
print('{:^36}'.format('Listagem de preço'))
print('-'*36)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:<7.2f}')

