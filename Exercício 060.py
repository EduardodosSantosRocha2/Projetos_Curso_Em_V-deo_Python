num = int(input('Digite o número desejado:'))
c = num
f = 1
print('~'*14)
print('Calculando {}!'.format(c))
print('~'*14)
while c > 0:
    print('{}'.format(c), end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))
