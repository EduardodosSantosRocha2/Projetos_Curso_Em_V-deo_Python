while True:
    print('-' * 30)
    n = int(input('Digite a tabuada desejada: '))
    if n < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')


