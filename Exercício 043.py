print('Use ponto no lugar da virgula!')
p = float(input('Qual é o seu peso:'))
a = float(input('Qual é a sua altura:'))
imc = p / (a ** 2)
if imc < 18.5:
    print('\033[31mAbaixo do peso\033[m!')
elif imc > 18.5 and imc <= 25.0:
    print('\033[32mPeso ideal\033[m!')
elif imc > 25 and imc <= 30:
    print('\033[33mSobrepeso!\033[m')
elif imc > 30 and imc <= 40:
    print('\033[31mObesidade\033[m!')
elif imc > 40:
    print('\033[31mObesiade mórbida\033[m!')