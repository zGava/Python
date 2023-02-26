import random
p = input('Primeiro aluno: ')
s = input('Segundo aluno: ')
t = input('Terceiro aluno: ')
q = input('Quarto aluno: ')
lista = [p,s,t,q]
escolhido = random.choice(lista)
print('O aluno sorteado foi {}'.format(escolhido))
