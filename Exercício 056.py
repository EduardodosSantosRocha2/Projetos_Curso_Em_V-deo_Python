somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totaldemulherescommenosde20 = 0
for p in range(1, 3):
    print('---- {}° PESSOA ----'.format(p))
    nome = str(input('Qual o seu nome:')).strip()
    idade = int(input('Qual a sua idade:'))
    sexo = str(input('Sexo [M/F]')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totaldemulherescommenosde20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos é se chama {}'.format(maioridadehomem, nomevelho.capitalize()))
print('Ao todo {} mulheres tem menos de 20 anos'.format(totaldemulherescommenosde20))






