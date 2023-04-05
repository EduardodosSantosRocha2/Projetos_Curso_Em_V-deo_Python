from random import randint
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
print('''Escolha entre: 
0 = pedra 
1 = papel 
2 = tesoura''')
jogador = int(input('Qual é a sua jogada:'))
print("-=-"* 10)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print("-=-"* 10)
if computador == 0:
    if jogador == 0:
        print('\033[33mEmpate\033[m!')
    elif jogador == 1:
        print('\033[32mVocê ganhou\033[m!')
    elif jogador == 2:
        print('\033[31mPerdeu\033[m!')
    else:
        print('\033[31mOpção invalida\033[m')
if computador == 1:
    if jogador == 1:
        print('n')
    elif jogador == 0:
        print('\033[31mPerdeu\033[m!')
    elif jogador == 2:
        print('\033[32mVocê ganhou\033[m!')
    else:
        print('\033[31mOpção invalida\033[m')
if computador == 2:
            if jogador == 0:
                print('\033[32mVocê ganhou\033[m!')
            elif jogador == 1:
                print('\033[31mPerdeu\033[m!')
            elif jogador == 2:
                print('\033[33mEmpate\033[m!')





