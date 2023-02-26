peso = float(input('Qual é o seu peso? (Kg) '))
alt = float(input('Qual é a sua altura? (Cm) '))
imc = peso/(alt**2) .__ceil__()
print('O IMC dessa pessoa é de {:.2f}'.format(imc))
if imc <18.5:
    print('Você está abaixo do peso normal, cuidado!')
elif 18.5 <= imc <=25:
    print('Parabéns, você está no peso ideal!')
elif 25 <= imc <=30:
    print('Preste atenção, você está sobrepeso!')
elif 30 <= imc <=40:
    print('Vai se cuidar, você atingiu o nível de obesidade!')
else:
    print('Procure um médico urgente, você está em obesidade mórbida!!')
