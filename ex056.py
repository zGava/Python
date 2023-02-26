maior = 0
menor = 0
maioridadehomem=0
nomevelho=''
totmulher20=0

for c in range(1, 5):
    print('------- {} pessoa ------- '.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip()
    if c == 1 and sexo in 'Mm':
        maior = idade
        menor = idade
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'Mm' and idade>maioridadehomem:
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'Ff' and idade<20:
        totmulher20+=1

media = (idade + idade + idade + idade) / 4

print('A media de idade do grupo e de {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem,nomevelho))
print('Ao todo sao {} mulher com menos de 20 anos.'.format(totmulher20))
