frase= str(input('Digite uma frase: ')).strip().upper()
palavras= frase.split()
junto= ''.join(palavras)
inverso= ''
for letra in range(len(junto)-1, -1, -1):
    inverso+=junto[letra]
print('O inverso de {} e {}'.format(frase,inverso))
if inverso==junto:
    print('Temos um palindromo')
else:
    print('Nao temos um palindromo')
