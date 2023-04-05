print('='*30)
print('{:^30}'.format('BANK FED'))
print('='*30)
valor = int(input('What amount do you want to withdraw: '))
total = valor
ced = 100
contced = 0
while True:
    if total >= ced:
        total -= ced
        contced += 1
    else:
        if contced > 0:
            print(f'Total of {contced} grades in US${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        contced = 0
        if total == 0:
            break
