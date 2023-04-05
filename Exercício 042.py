print('\033[32m-=-'*13)
print('\033[35mAnalizador de triângulos')
print('\033[32m-=-'*13)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[32mOs segmentos formam um triângulo', end = ' ')
    if r1 == r2 == r3:
     print('Equilátero!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('\033[35m\033[40mOs segmentos acima não podem formar triângulo!\033[m')
