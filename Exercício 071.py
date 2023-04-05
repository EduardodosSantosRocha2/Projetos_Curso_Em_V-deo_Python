print('='*30)
print('{:^30}'.format('BANCO TOOPAYPAL'))
print('='*30)
valor = int(input('Qual valor você deseja sacar? R$ '))
total = valor
ced = 200
contced = 0
while True:
    if total >= ced:
        total -= ced
        contced += 1
    else:
        if contced > 0:
            print(f'Total de {contced} de R${ced}')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        contced = 0
        if total == 0:
            break




