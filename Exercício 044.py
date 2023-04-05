preco = float(input('Qual o preço normal do produto:R$'))
condicao = int(input('''Digite o número da condição de pagamento
\033[32m[ 1 ] Á vista dinheiro/cheque com 10% de desconto.\033[m
\033[33m[ 2 ] Á vista no cartão com 5% de desconto.\033[m
\033[36m[ 3 ] Em até 2x no catão sem juros.\033[m
\033[31m[ 4 ] 3x ou mais no cartão com 20% de juros.\033[m 
Qual a sua escolha:'''))
if condicao == 1:
    print('O valor do produto será R${:.2f}'.format(preco - (preco * 0.10)))
elif condicao == 2:
    print('O valor do produto será R${:.2f}'.format(preco - (preco * 0.05)))
elif condicao == 3:
    parcela = preco / 2
    print('Sua compra vai ser parcelada em 2x sem juros de R${:.2f}'.format(parcela))
    print('O valor do produto será R${:.2f}'.format(preco))
elif condicao == 4:
    print('O valor do produto será R${:.2f}'.format(preco + (preco * 0.20)))
else:
    print('\033[31mOpção invalida de pagamento.Tente novamente!\033[m')
