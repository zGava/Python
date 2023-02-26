import datetime
atual = datetime.date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
alistado = nasc + 18
ano = atual - alistado
saldo = 18 - idade
ano2= atual + saldo
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc,idade,atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade > 18:
    print('Você já devia ter se alistado há {} anos.'.format(ano))
    print('Seu alistamento foi em {}.'.format(alistado))
elif idade < 18:
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    print('Seu alistamento será em {}.'.format(ano2))



