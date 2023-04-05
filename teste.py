salario = 1000.0
percentual = 0.015
salario = salario + percentual* salario
anoatual = int(input("Digite o ano atual: "))
for c in range(2007, anoatual+1, 1):
  percentual = percentual * 2
  salario = salario + percentual * salario
print("{}".format(salario))

