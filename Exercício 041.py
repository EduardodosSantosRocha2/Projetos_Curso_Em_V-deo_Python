from datetime import date
atual = date.today().year
ano = int(input('Qual o ano do seu nascimento:'))
idade = atual - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: \033[1;32mMIRIM\033[m')
elif idade > 9 and idade <= 14:
    print('Classificação: \033[1;32mINFANTIL\033[m')
elif idade > 14 and idade <= 19:
    print('Classificação: \033[1;32mJUNIOR\033[m')
elif idade > 19 and idade <= 25:
    print('Classificação: \033[1;32mSÊNIOR\033[m')
elif idade > 25:
    print('Classificação: \033[1;32mMASTER\033[m')

