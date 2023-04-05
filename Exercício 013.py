salário=float(input('Qual é  salário do funcionário? R$'))
novosalário = salário + (salário*15 / 100)
print('Um funcionário que ganhava{:.2f},com 15% de aumento,passara a receber R${:.2f}'.format(salário, novosalário))