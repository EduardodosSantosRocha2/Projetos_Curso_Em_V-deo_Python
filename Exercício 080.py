lista = []
for valor in range(0, 5):
    numero = int(input('Digite um número: '))
    if valor == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        pos = 0 #varredura
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                break
            pos += 1


print(f'Os valores em ordem são {lista}')








