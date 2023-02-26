n = str(input('Digite seu nome completo: ')).strip()
m = n.upper()
mi = n.lower()
t = len(n)-n.count(' ')
print('Seu nome em maiúsculo é {}.'.format(m))
print('Seu nome em minúsculo é {}.'.format(mi))
print('O total de letras do seu nome é {}.'.format(t))
print('Seu primeiro nome tem {} letras.'.format(n.find(' ')))




