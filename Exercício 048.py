total = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        total += 1
        soma += c
print('\033[31mA soma de\033[m \033[1;35m{}\033[m \033[33mnúmeros impares\033[m \033[34mque são múltiplos de 3\033[m \033[32mentre 1 e 500\033[m é \033[1;36m{}\033[m'.format(total, soma))


