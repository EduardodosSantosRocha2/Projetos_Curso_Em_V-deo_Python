num = int(input('Digite o número desejado [999 para parar]: '))
contador = 0
soma = 0
while num != 999:
   soma += num
   contador += 1
   num = int(input('Digite o número desejado [999 para parar]: '))
print('Você digitou {} números é a soma entre eles é {}'.format(contador, soma))
print('Fim!')

