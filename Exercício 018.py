import math
ângulo = float(input('Digite o ângulo que voce deseja:'))
seno = math.sin(math.radians(ângulo))
print('O ângulo de {} tem o Seno de {}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângulo de {} tem o Cosseno de {}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem a Tangente de {}'.format(ângulo, tangente))
