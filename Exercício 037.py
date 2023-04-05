print('='*20)
print('{:^20}'.format('Base de conversão'))
print('='*20)
n = int(input('Digite um número: '))
print('Qual base você deseja:\n[1]Binário\n[2]Octal\n[3]Hexadecimal')
escolha = int(input('Digite a sua escolha: '))
if escolha == 1:
    print(bin(n))
elif escolha == 2:
    print(oct(n))
elif escolha == 3:
    print(hex(n))
