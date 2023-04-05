contadormaisde18 = contadormulheresmenos20anos = contadorhomenscadrastrados = 0
while True:
    print('-'*25)
    print('CADASTRE UMA PESSOA')
    print('-'*25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        contadormaisde18 += 1
    if sexo in 'M':
        contadorhomenscadrastrados += 1
    if sexo in 'F' and idade < 20:
        contadormulheresmenos20anos += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        break
print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {contadormaisde18}')
print(f'Ao todo temos {contadorhomenscadrastrados} homens cadastrados')
print(f'Ao todo {contadormulheresmenos20anos} mulheres tem menos de 20 anos.')




