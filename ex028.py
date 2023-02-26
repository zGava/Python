from random import randint
from time import sleep
comp = randint(0,5)
print('=-='*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('=-='*20)
p = int(input('Em qual número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if p == comp:
    print('PROCESSANDO...')
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}!'.format(comp,p))