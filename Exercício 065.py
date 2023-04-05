resposta = 'Ss'
soma = media = total = maior = menor = 0
while resposta in 'Ss':
    num = int(input('Digite um número:'))
    soma += num
    total += 1
    if total == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Você deseja continuar [S/N]: ')).strip().upper()
media = soma / total
print('Você digitou {} números é a média foi {}'.format(total, media))
print('O maior número é {} e o menor número é {}'.format(maior, menor))
print('Fim!')
