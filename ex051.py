print('='*20)
print('10 TERMOS DE UMA P.A')
print('='*20)
pt=int(input('Primeiro termo: '))
r=int(input('Razao: '))
decimo= pt + (10-1) * r
for c in range(pt,decimo,r):
    print('{} '.format(c), end=' -> ')
print('ACABOU!')
