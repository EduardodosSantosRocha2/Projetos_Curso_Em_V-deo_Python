from datetime import date
contadormaior = 0
contadormenor = 0
pessoa = ''
pessoasmenores = ''
for nascimento in range(1, 8):
    ano = int(input('Qual seu ano de nascimento:'))
    idade = date.today().year - ano
    if idade >= 18:
        contadormaior += 1
        if contadormaior == 1:
            pessoa = 'Pessoa é menor'
        if contadormaior > 1:
            pessoa = 'Pessoas são maiores'
    if idade <= 18:
        contadormenor += 1
        if contadormenor == 1:
            pessoasmenores = 'Pessoa é maior'
        if contadormenor > 1:
            pessoasmenores = 'Pessoas são maiores'
print('{} {} de idade'.format(contadormaior, pessoa))
print('{} {} de idade'.format(contadormenor, pessoasmenores))