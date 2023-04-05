primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
contador = 1
termo = primeiro
while contador <= 10:
    print('{} →'.format(termo), end=' ')
    termo += razao
    contador += 1
print('Fim!')

