print('\033[1;35m-=-\033[m'*20)
print('\033[1;32mTODOS OS NÚMEROS PARES QUE ESTÃO NO INTERVALO ENTRE 1 E 50.\033[m')
print('\033[1;36m-=-\033[m'*20)
for c in range(0, 51, 2):
    print('{}'.format(c), end=' ')