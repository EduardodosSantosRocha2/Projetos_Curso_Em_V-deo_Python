from time import sleep
print('-=-' * 7)
print('  Calculo do DETRAN')
print('-=-' * 7)
velocidade = int(input('Qual a velocidade do carro:'))
if velocidade > 80:
    print('Multado! Você excedeu o limite permitido que é de 80km/h')
    sleep(2)
    print('A multa é de R$7,00 reais por cada km acima do limite!')
    sleep(3)
    print('Processando o valor...')
    sleep(4)
    print('O valor a ser pago é R${:.2f}!'.format((velocidade - 80) * 7))
else:
    print('Nenhuma multa!')