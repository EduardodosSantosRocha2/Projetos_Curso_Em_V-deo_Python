maior = menor = 0
valores = []
for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para posição {v}: ')))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} na posição ', end=' ')
for e, v in enumerate(valores):
    if v == maior:
        print(f'{e}...', end='')
print(f'\nO menor valor digitado foi {menor} na posição ', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')



