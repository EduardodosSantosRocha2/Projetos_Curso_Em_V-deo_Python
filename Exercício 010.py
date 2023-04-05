real = float(input('Digite o valor em reais:R$'))
dolar = real/5.09
euro = real/6.21
iene = real/0.046
print('Com R${:.2f} você pode comprar: \nUS${:.2f}\n€{:.2f}\n￥{:.2f}  '.format(real, dolar, euro, iene))