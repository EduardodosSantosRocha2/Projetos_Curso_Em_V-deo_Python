#ca = float(input('Qual é o cateto adjacente:'))
#co = float(input('Qual é o cateto oposto:'))
#hi = (co**2 + ca**2) **(1/2)
#print('A hipotenusa vai medir {:.2f}'.format(hi))
#
#Ou
import math
from math import hypot
co = float(input('Qual é o cateto oposto:'))
ca = float(input('Qual é o cateto adjacente:'))
hi = hypot(co, ca)
print('A hipotenusa vai medir:{:.2f}'.format(hi))