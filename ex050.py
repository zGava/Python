soma=0
count=0
for c in range(1,7):
    num = int(input('Digite {} valor: '.format(c)))
    if num % 2 ==0:
        soma +=num
        count +=1
print('Voce informou {} numeros PARES e a soma foi {}.'.format(count,soma))
