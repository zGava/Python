casa = float(input('Valor da casa: R$ '))
salário = float(input('Salário do comprador: '))
financiamento = int(input('Quantos anos de financiamento: '))
meses= financiamento*12
prest= casa/meses
mínimo= salário * 30/100
print('Para pegar uma casa de R${:.2f} em {} anos, a prestação será de {:.2f}'.format(casa,financiamento,prest))
if prest >= mínimo:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')
