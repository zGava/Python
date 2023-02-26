d = float(input('Qual a distância da sua viagem? '))
a = d*0.50 #ate 200km
e = d*0.45 #em diante
print('Você está prestes a começar uma viagem de {:.1f}km.'.format(d))
if d<200:
    print('E o preço da sua passagem será R${:.2f}'.format(d))
else:
    print('E o preço da sua passagem será R${:.2f}'.format(e))
