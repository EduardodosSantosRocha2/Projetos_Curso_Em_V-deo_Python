matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maior = somacoluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para a posição [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if matriz[2][c] == 0:
            maior = matriz[2][c]
        else:
            if matriz[2][c] > maior:
                maior = matriz[2][c]
    print()
print(f'A soma dos pares é {somapar}')
print(f'O maior número da segunda linha é {maior}')
for l in range(0, 3):
    somacoluna += matriz[l][2]
print(f'A soma da terceira coluna é {somacoluna}')



