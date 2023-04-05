lista1 = []
lista2 = []
lista3 = []
while True:
    numero = int(input('Digite um número:'))
    lista1.append(numero)
    if numero % 2 == 0:
        lista2.append(numero)
    if numero % 2 != 0:
        lista3.append(numero)
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Digite [S/N] para continuar: ')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'A lista completa é {lista1}')
print(f'Os números pares da lista são: {lista2}')
print(f'Os números impares da lista são: {lista3}')
