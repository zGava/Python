print('=='*20)
print('{:^40}'.format('Lojas Gava'))
print('=='*20)
comp = float(input('Preço das compras? R$ '))
print(''' FORMAS DE PAGAMENTO
[1] À vista no dinheiro ou cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
op = int(input('Qual é a opção? '))
d1 = comp - (comp* 10/100)
d2 = comp - (comp* 5/100)
j = comp + (comp * 20/100)
if op == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final!'.format(comp,d1))
if op == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final!'.format(comp, d2))
if op == 3:
    print('Ok, seu valor não sofre alteraçõe!')
if op == 4:
    p = int(input('Quantas parcelas? '))
    cj = j/p
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(p,cj))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final!'.format(comp,j))
else:
    print('Opção inválida, tente novamente!')

