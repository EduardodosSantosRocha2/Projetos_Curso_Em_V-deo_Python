cont = ('zero', 'um', 'dois', 'três','quatro', 'cinco'
         , 'seis', 'sete', 'oito','nove','dez', 'onze',
         'doze', 'treze', 'quatorze','quinze',
         'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0 or num > 20:
        break
    else:
        if num >= 0 and num <= 20:
            print(f'O número {num} por extenso é {cont[num]} ')
        resposta = ' '
        while resposta not in 'SN':
            resposta = str(input('Deseja continuar [S/N]: ')).upper().strip()
        if resposta == 'N':
            break
print('='*25)
print('{:^25}'.format('FIM'))
print('='*25)
