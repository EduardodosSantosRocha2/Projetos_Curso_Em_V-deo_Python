t1 = 0
t2 = 1
contador = 3
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar: '))
print('{} → {} →'.format(t1, t2), end=' ')
while contador <= n:
    t3 = t1 + t2
    print('{} →'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    contador += 1
print('Fim!')