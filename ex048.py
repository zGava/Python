soma=0
cont = 0
for c in range(1,501):
    if c % 3 ==0 and c %2 == 1:
        soma = soma + c
        cont = cont + 1
print('A soma de todos os {} valores solicitados é {}'.format(cont,soma))