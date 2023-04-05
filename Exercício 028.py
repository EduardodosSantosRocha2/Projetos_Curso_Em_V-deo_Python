import random
from time import sleep
print('Bem vindo! Pronto para jogar?')
print('-=-' * 22)
print('O computador pensou em um número inteiro de 0 a 5, qual foi ele? ')
print('-=-' * 22)
n = int(input('Digite o número:'))
lista = [1, 2, 3, 4, 5 ]
r = random.choice(lista)
print('PROCESSANDO...')
sleep(2)
if n == r:
    print('Você acertou! Parabéns')
else:
    print('Erro crasso! O computador venceu!')
