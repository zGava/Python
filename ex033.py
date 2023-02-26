n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
#VERIFICANDO QUEM E MENOR
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
#VERIFICANDO QUEM E MAIOR
maior = n3
if n1>n2 and n1>n3:
    maior= n1
if n3>n2 and n3>n1:
    maior= n3
print('O menor valor foi {}'.format(menor))
print('O maior valor foi {}'.format(maior))