from random import randint
computador = randint(0, 10)
contador = 0
print('-=-'*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-'*10)
while True:
    n = int(input('Diga um valor : '))
    escolha = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    soma = n + computador
    if soma % 2 == 0 and escolha in 'P':
        print('-' * 55)
        print(f'Você jogou {n} e o computador {computador}.Total de {soma} deu Par.')
        print('-' * 55)
        print('\033[32mVocê ganhou!\033[m')
        print('-=-' * 18)
        contador += 1
    if soma % 2 != 0 and escolha in 'P':
        print('-' * 55)
        print(f'Você jogou {n} e o computador {computador}.Total de {soma} deu Ímpar.')
        print('-' * 55)
        print('\033[31mVocê perdeu!\033[m')
        print('-=-' * 18)
        break
    if soma % 2 != 0 and escolha in 'I':
        print('-' * 55)
        print(f'Você jogou {n} e o computador {computador}.Total de {soma} deu Ímpar.')
        print('-' * 55)
        print('\033[32mVocê ganhou!\033[m')
        print('-=-' * 18)
        contador += 1
    if soma % 2 == 0 and escolha in 'I':
        print('-' * 55)
        print(f'Você escolheu {n} e o computador {computador}.Total de {soma} deu Par.')
        print('-' * 55)
        print('\033[31mVocê perdeu!\033[m')
        print('-=-' * 18)
        break
print(f'GAME OVER! Você venceu {contador} vezes.')









