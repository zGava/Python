print('=-='*15)
print('Analisador de Triângulos')
print('=-='*15)
p = float(input('Primeiro segmento: '))
s = float(input('Segundo segmento: '))
t = float(input('Terceiro segmento: '))
if p < s + t and s < p + t and t < p + s:
    print('Os segmentos acima PODEM formar um triângulo',end='')
    if p == s == t:
        print(' e é EQUILÁTERO!')
    elif p != s != t != p:
        print(' e é ESCALENO!')
    else:
        print(' e é ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')