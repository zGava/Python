from time import sleep
v = int(input('Qual a velocidade atual do carro? '))
print('PROCESSANDO...')
sleep(3)
if v >80:
    print('MULTADO! Você execedeu o limite permitido que é de 80km/h')
    multa=(v-80)*7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('Tenha um bom dia! Dirija com segurança!')

