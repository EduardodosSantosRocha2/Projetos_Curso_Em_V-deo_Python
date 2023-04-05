print('\033[32m-=-'*13)
print('\033[35mAnalizador de triângulos')
print('\033[32m-=-'*13)
r1 = float(input('\033[35mPrimeiro segmento:'))
r2 = float(input('\033[35mSegundo segmento:'))
r3 = float(input('\033[35mTerceiro segmento:'))
if r1 < r2 +r3 and r2< r1 + r3 and r3 < r2+r1:
    print('\033[34mOs segmentos podem acima forma triângulo!')
else:
    print('\033[35m\033[40mOs segmentos acima não podem formar triângulo!')