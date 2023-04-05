princ = []
temp = []
cont = 0
maior = 0
menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Digite [S/N] para continuar: ')).upper()[0].strip()
    if escolha == 'N':
        break
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi {maior} Kg. Sendo esse peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]')
print(f'O menor peso foi {menor} Kg. Sendo esse peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]')

