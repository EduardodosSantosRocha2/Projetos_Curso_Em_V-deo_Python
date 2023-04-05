primeiro = int(input('Digite o primeiro termo da PA:'))
razao = int(input('Digite a razão da PA:'))
contador = 1
termo = primeiro
mais = 10
total = 0
while mais != 0:
    total += mais
    while contador <= total:
        print('{} →'.format(termo), end=' ')
        termo += razao
        contador += 1
    print('Pausa')
    mais = int(input('Digite quantos termos a mais você quer: '))
print('Fim!')
