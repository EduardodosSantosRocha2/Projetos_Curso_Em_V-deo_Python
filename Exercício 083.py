expressao = str(input('Digite uma expressão: '))
pilha = []
for simbolo in expressao:
  if simbolo == '(':
    pilha.append('(')
  elif simbolo == ')':
      if len(pilha) > 0:
        pilha.pop()
      else:
          pilha.append(')')
if len(pilha) == 0:
  print('Sua expressão está correta!')
else:
  print('Sua expressão está errada!')
print(len(pilha))