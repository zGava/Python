n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1+n2)/2 .__ceil__()
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1,n2,m))
if m>6:
    print('O aluno está APROVADO!')
elif m>=5 and m<7:
    print('O aluno está de RECUPERAÇÃO!')
else:
    print('O aluno está REPROVADO!')