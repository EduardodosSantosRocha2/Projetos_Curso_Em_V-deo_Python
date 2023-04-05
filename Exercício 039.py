from datetime import date
atual = date.today().year
ano = int(input('Qual é o ano do seu nascimento:'))
idade = atual - ano
falta = 18 - idade
passou = idade - 18
if idade < 18:
    print('\033[32mAinda não é a hora de você se alistar\033[m.\033[31mFalta {} anos\033[m!'.format(falta))
elif idade == 18:
    print('\033[32mEstá na hora de você se alistar!\033[m')
else:
    print('\033[31mO seu tempo de alistamento já passou a {} anos\033[m.\033[32mCompareça na unidade mais próxima\033[m!'.format(passou))