n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite outro valor: '))
n4 = int(input('Digite outro valor: '))
numeros = (n1, n2, n3, n4)
print(f'O numero 9 aparece {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O primeiro valor 3 foi digitado na {numeros.index(3)+1}ª posição ')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os numeros pares digitados são: ', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end='  ')


