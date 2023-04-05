nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
nota = (nota1 + nota2) / 2
if nota < 5:
    print('Você foi \033[31mREPROVADO\033[m!')
elif nota >= 5 and nota <= 6.9:
    print('Você está de \033[33mRECUPERAÇÃO\033[m')
else:
    print('Você foi \033[32mAPROVADO\033[m')
