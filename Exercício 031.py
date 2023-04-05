print('Ola, abaixo nossa tabela de preço!')
print('-=-'* 13)
print('R$0,50 por Km para viagens até 200Km\nR$0,45 para viagens acima de 200Km')
print('-=-'* 13)
v = int(input('Qual a distância da viagem em Km:'))
if v <= 200:
    preço = v * 0.50
    print('O valor da viagem de {}Km é R${:.2f}'.format(v, preço))
else:
 preço = v * 0.45
 print('O valor de {}Km é R${:.2f}'.format(v, preço))
