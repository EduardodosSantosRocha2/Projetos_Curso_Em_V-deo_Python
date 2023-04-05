valor = int(input('Digite o valor da casa:R$ '))
salario = int(input('Digite o seu salário:R$ '))
anos = int(input('Digite em quantos anos você deseja pagar: '))
meses = anos * 12
mensal = valor / meses
if mensal < salario * 0.30:
    print('Para pagar uma casa de {:.2f} em {} a prestação será de R${:.2f}\n\033[32mEmpréstimo aprovado!\033[m'.format(valor, anos, mensal))
else:
    print('Para pagar uma casa de {:.2f} em {} a prestação será de R${:.2f}\n\033[31mEmpréstimo NEGADO!\033[m'.format(valor, anos, mensal))

