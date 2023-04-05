times = ('Atletico-MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo', 'Athletico-PR',
         'Atlético Goianiense', 'Ceará', 'Internacional', 'Santos', 'Corinthians', 'Juventude',
         'Bahia', 'São Paulo', 'Fluminense', 'Cuiabá', 'Sport', 'América-MG', 'Grêmio', 'Chapecoense')
print('-=-'*100)
print(f'Lista de times do Brasileirão serie A: {times}')
print('-=-'*100)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('-=-'*100)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=-'*100)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=-'*100)
print('O Chapecoense está em {}ª posição'.format(times.index('Chapecoense') + 1))
print('-=-'*100)
