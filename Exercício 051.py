print('='*20)
print('\033[1m10 TERMOS DE UMA PA\033[m')
print('='*20)
p1 = int(input('Primeiro mais:'))
r = int(input('Razão:'))
decimo = p1 + (10 - 1) * r
for c in range(p1, decimo, r):
    print('{}'.format(c), end=' ➞ ')
print('Acabou')