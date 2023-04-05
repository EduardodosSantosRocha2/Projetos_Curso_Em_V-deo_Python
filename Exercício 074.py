from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
ordem = sorted(numeros)
print(f'Eu sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior número sorteado foi {ordem[-1]}')
print(f'O menor número sorteado foi {ordem[0]}')







#print(f'\nO maior número sorteado foi {max(numeros)}')
#print(f'O menor número sorteado foi {min(numeros)}')



