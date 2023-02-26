from random import randint
from time import sleep
comp = randint(0,10)
acertou = False
palpite=0
print('=-='*20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('=-='*20)
print('PROCESSANDO...')
sleep(3)
while not acertou:
        p = int(input('Em qual número eu pensei? '))
        palpite+=1
        if p == comp:
            acertou=True
        else:
            if p < comp:
                print('Mais, tente mais uma vez...')
            elif p > comp:
                print('Menos, tente mais uma vez...')
print('Voce acertou com {} tentativas, parabens!'.format(palpite))



