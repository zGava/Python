n = int(input('Digite um numero para ver sua tabuada: '))
print('=-='*10)
for nu in range(1, 11):
    m = n * nu
    print('{} X {} = {}'.format(n,nu,m))
print('=-='*10)