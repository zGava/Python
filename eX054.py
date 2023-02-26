from datetime import date
atual = date.today().year
totm=0
totme=0
for peo in range(1,8):
    nasc =int(input('Em que ano a {} pessoa nasceu? '.format(peo)))
    idade= atual -nasc
    if idade>=21:
        totm += 1
    else:
        totme += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totm))
print('Ao todo tivemos {} pessoas menores de idade'.format(totme))

