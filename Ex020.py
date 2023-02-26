import random
p = input('Primeiro aluno: ')
s = input('Segundo aluno: ')
t = input('Terceiro aluno: ')
q = input('Quarto aluno: ')
lista = [p,s,t,q]
random.shuffle(lista)
print('A ordem de apresentação do trabalho será')
print(lista)

