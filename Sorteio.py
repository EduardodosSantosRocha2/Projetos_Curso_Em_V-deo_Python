valorsalario = float(input("Escreva o seu salário:R$"))
if valorsalario < 500.00:
  aumento = (valorsalario*0.30)+ valorsalario
  print(f"Seu novo salario é:R$ {aumento} ") 
else:
  print("Você não tem direito ao aumento.")
