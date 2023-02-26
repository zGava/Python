from time import sleep
print('=-='*15)
print('{:^44}'.format('Contagem regressiva'))
print('=-='*15)
for c in range(10, 0, -1):
    sleep(1)
    print(c)
print('Acabou!')
