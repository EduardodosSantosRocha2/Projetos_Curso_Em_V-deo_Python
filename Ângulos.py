import math
ag = float(input('Digite o ângulo desejado:'))
sen = math.sin(math.radians(ag))
cos = math.cos(math.radians(ag))
tan = math.tan(math.radians(ag))
print('O seno de {}° é:{}\nO cosseno de {}° é:{}\nA tangente de {}° é:{}\n'.format(ag,sen, ag, cos, ag, tan))
