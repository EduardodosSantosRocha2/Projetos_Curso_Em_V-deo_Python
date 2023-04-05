numero1 = int(input('Digite um número inteiro:'))
numero2 = int(input('Digite outro número inteiro:'))
if numero1 > numero2:
    print('O \033[33mprimeiro\033[m número é \033[32mmaior\033[m!')
elif numero1 == numero2:
    print('\033[31mNão existe\033[m valor maior, os dois numeros são \033[34miguais\033[m!')
else:
    print('O \033[33msegundo número\033[m é \033[32mmaior\033[m!')