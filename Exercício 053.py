frase = str(input('Digite a frase:')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letras in range(len(junto)-1, -1, -1):
    inverso += junto[letras]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palídromo')





