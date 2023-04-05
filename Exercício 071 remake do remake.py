print('='*30)
print('{:^30}'.format('Nippon Ginkō'))
print('='*30)
valor = int(input('どのような価値を引き出したいですか: '))
ced = 10000
total = valor
contced = 0
while True:
    if total >= ced:
        total -= ced
        contced += 1
    else:
        if contced > 0:
            print(f'合計 {contced} グレード 価値の ¥{ced}')
        if ced == 10000:
            ced = 5000
        elif ced == 5000:
            ced = 2000
        elif ced == 2000:
            ced = 1000
        contced = 0
        if total == 0:
            break
