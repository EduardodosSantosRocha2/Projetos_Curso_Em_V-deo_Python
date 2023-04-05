cont = 0
lista = []
while True:
    numeros = int(input('Digite um número: '))
    lista.append(numeros)
    cont += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Digite [S/N] se deseja continuar: ')).strip().upper()[0]
    if escolha == 'N':
        break
lista.sort(reverse=True)
print(f'{cont} números foram digitados!')
print(f'Os valores ordenados em ordem decrescente são {lista} ')
if 5 in lista:
    print('O número 5 foi digitado')
else:
    print('O número 5 não foi digitado')