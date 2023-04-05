#from random import choice
import random
n1 = str(input('Digite um nome:'))
n2 = str(input('Digite um nome:'))
n3 = str(input('Digite um nome:'))
n4 = str(input('Digite um nome:'))
lista1 = [n1, n2, n3, n4 ]
lista2 = [1, 2, 3, 4,]
escolha1 = random.choice(lista1)
escolha2 = random.choice(lista2)
print('O aluno(a) {},apresentará na {}° posição '.format(escolha1, escolha2))



