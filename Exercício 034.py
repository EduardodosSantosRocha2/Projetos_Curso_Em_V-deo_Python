salario = float(input('Qual o salário do funcionario?R$'))
if salario > 1250.00:
    novo = salario + (salario * 0.10)
    print('Quem ganhava R${:.2f} passa a ganhar:R${:.2f}'.format(salario, novo))
else:
    novo = salario + (salario * 0.15)
    print('Quem ganhava R${:.2f} passa a ganhar:R${:.2f}'.format(salario, novo))
