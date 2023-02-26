from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0,2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura ''')
jo = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('=-' * 15)
print('O computador jogou {}'.format(itens[comp]))
print('O jogador jogou {}'.format(itens[jo]))
print('=-' * 15)

if comp == 0: #pedra
    if jo == 0:
        print('Empate!')
    elif jo == 1:
        print('Jogador venceu!')
    elif jo == 2:
        print('Computador venceu!')
    else:
        print('Jogada invalida!')

elif comp == 1: #papel
    if jo == 0:
        print('Computador venceu!')
    elif jo == 1:
        print('Empate!')
    elif jo == 2:
        print('Jogador venceu!')
    else:
        print('Jogada invalida!')

elif comp == 2: #tesoura
    if jo == 0:
        print('Jogador venceu!')
    elif jo == 1:
        print('Computador venceu!')
    elif jo == 2:
        print('Empate!')
    else:
        print('Jogada invalida!')


