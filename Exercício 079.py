numeros = []
for v in range(0, 5):
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    e = ' '
    while e not in 'SsNn':
        e = str(input('Quer continuar [S/N]: ')).upper()[0].strip()
    if e == 'N':
        break
numeros.sort()
print(f'Você digitou os valores {numeros}')

