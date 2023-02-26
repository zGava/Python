import math
an = float(input('Digite um ângulo que você deseja: '))
seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tang = math.tan(math.radians(an))
print('O angulo de {} tem seno de {:.2f}'.format(an,seno))
print('O angulo de {} tem cosseno de {:.2f}'.format(an,cos))
print('O angulo de {} tem tangente de {:.2f}'.format(an,tang))
