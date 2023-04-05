escolha = 0
maior = ''
n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
while escolha != 5:
    print('O que você deseja:\n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair do programa')
    escolha = int(input('Qual sua escolha:'))
    if escolha == 1:
        soma = n1 + n2
        print('O calculo de {} + {} é {}'.format(n1, n2, soma))
        print('=-==-='*5)
    elif escolha == 2:
        multiplicacao = n1 * n2
        print('A multiplicação {} x {} é {}'.format(n1, n2, multiplicacao))
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        elif n1 == n2:
            maior = ' nenhum os dois numeros são iguais.'
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif escolha == 4:
        n1 = int(input('Digite um valor:'))
        n2 = int(input('Digite outro valor:'))
    elif escolha == 5:
        print('Finalizando...')
    else:
        print('Opção inválida.Tente novamente')
print('Fim do programa! Volte sempre!')

