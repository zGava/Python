s = float(input('Qual é o salário do funcionário? R$'))
a1 = s + (s*10/100)
a2 = s + (s*15/100)
if s>1250.00:
    print('Quem ganhava R${:.2f} passa a ganhar R${} agora!'.format(s,a1))
if s<1250.00:
    print('Quem ganhava R${:.2f} passa a ganhar R${} agora!'.format(s,a2))
