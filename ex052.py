n=int(input('Digite um numero: '))
tot = 0
for c in range(1, n+1):
    if n % c ==0:
        print('\033[33m',end=' ')
        tot+=1
    else:
        print('\033[31m',end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(n, tot))
if tot>2:
    print('Esse numero nao e PRIMO')
else:
    print('Esse numero e PRIMO')


