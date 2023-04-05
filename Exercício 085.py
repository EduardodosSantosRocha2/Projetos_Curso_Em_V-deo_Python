lista = [[], []]
for v in range(0, 7):
    valor = int(input(f'Digite o {v}° valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    elif valor % 2 != 0:
        lista[1].append(valor)
lista[0].sort()
print(f'Os valores pares digitados foram: {lista[0]}')
lista[1].sort()
print(f'Os valores impares digitados foram: {lista[1]}')
